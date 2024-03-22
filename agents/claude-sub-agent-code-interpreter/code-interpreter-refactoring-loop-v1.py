import os
import sys
import re
import logging
import traceback
from langchain.llms import Anthropic
from langchain.prompts import PromptTemplate

def run_code(code, question=None):
    # Execute the code and capture stdout, stderr, and any exceptions
    old_stdout = sys.stdout
    old_stderr = sys.stderr
    stdout_capture = sys.stdout = StringIO()
    stderr_capture = sys.stderr = StringIO()
    
    exception = None
    try:
        exec(code)
        if question:
            # Hacky way to pass input into the code
            sys.stdin = StringIO(question.strip() + "\n")  
            exec(code)
    except Exception as e:
        exception = e
    finally:
        sys.stdout = old_stdout
        sys.stderr = old_stderr
        
    stdout = stdout_capture.getvalue()
    stderr = stderr_capture.getvalue()
        
    return stdout, stderr, exception
            

def grade_answer(user_question, assistant_answer, ideal_answer, model):
    prompt = f"""
Here is a user question:
<question>
{user_question}
</question>

Here is the research assistant's answer to the question:
<answer>  
{assistant_answer}
</answer>

On a scale of A (best) to F (worst), grade the research assistant's answer. 
Importantly, do NOT compare it to any "ideal" answer - grade it based only on 
how well it directly answers the original question.

Grade (A, B, C, D or F): """

    grade = model(prompt).strip()
    grade = grade.split("\n")[0]  # Get first line of model output
    
    prompt += grade + "\n\nIn 1-2 sentences, briefly justify your grade:\n"
    justification = model(prompt)
    
    return grade, justification


template = """
Here is the research assistant source code to refactor and test:

<source_code>
{source_code}  
</source_code>

The research assistant should be able to answer this user question:

<user_question>
{user_question}
</user_question>

The ideal answer the research assistant should produce for that question is:

<ideal_answer>
{ideal_answer}
</ideal_answer>

First, execute the source code and capture any exceptions or failures.

Next, in a <suggestions> block, provide specific suggestions on how to refactor 
the source code to make it functional and fully testable. Focus on the minimum
necessary changes to get it working and testable, rather than perfection.

Then, in a <refactored_code> block, refactor the source code based on your suggestions.

Execute the refactored code, using the user question as input. Parse out the research 
assistant's <answer> from the output.

Grade the research assistant's answer against the ideal answer using a strong language 
model like Claude or GPT-4. Importantly, do not reveal the ideal answer to the model 
doing the grading.

In a <justification> block, briefly explain the key reasons for the grade you assigned.
Aim for 2-3 sentences.

Finally, output the following:  
<refactored_code>
The refactored source code
</refactored_code>

<research_assistant_answer>
The answer produced by the refactored research assistant 
</research_assistant_answer>

<grade>
The letter grade (A, B, C, D or F) you assigned to the research assistant's answer
</grade>

<justification>
Your brief justification for the grade
</justification>

Remember, the goal is to refactor the code to be testable and to produce a correct 
answer in the shortest time possible. Perfection is not required as long as it works. 
Let me know if you have any other questions!
"""

prompt = PromptTemplate(template=template, 
            input_variables=["source_code", "user_question", "ideal_answer"]) 

def main():
    model = Anthropic(model="claude-v1")
    
    # source_code = "..."
    with open('code-interpreter-refactoring-loop-v1.py') as f:
        source_code = f.read()
        
    user_question = """Using authoritative web sources to answer: who is the original author of this quote:
    There is not any present moment that is unconnected with some future one.
    The life of every man is a continued chain of incidents, each link of which hangs upon the former. 
    The transition from cause to effect, from event to event, is often carried on by secret steps, which our foresight cannot divine, and our sagacity is unable to trace. 
    Evil may at some future period bring forth good; and good may bring forth evil, both equally unexpected."""
    
    ideal_answer = "Hugh Blair"

    llm_output = model(prompt.format(source_code=source_code, 
                                     user_question=user_question, 
                                     ideal_answer=ideal_answer))

    # Parse the LLM output to extract the refactored code, assistant answer, grade, etc.
    refactored_code = re.search(r'<refactored_code>(.*?)</refactored_code>', 
                                llm_output, re.DOTALL).group(1)
    assistant_answer = re.search(r'<research_assistant_answer>(.*?)</research_assistant_answer>',
                                 llm_output, re.DOTALL).group(1) 
    grade = re.search(r'<grade>\s*(.*?)\s*</grade>', llm_output, re.DOTALL).group(1)
    justification = re.search(r'<justification>(.*?)</justification>', 
                              llm_output, re.DOTALL).group(1)

    # Run the refactored code
    stdout, stderr, exception = run_code(refactored_code, user_question)
    
    if exception:
        logging.error(f"Error running refactored code: {traceback.format_exc()}")
        # Go back to the LLM for debugging help
        debug_prompt = f"""
        The refactored code threw this exception when executed:
        {traceback.format_exc()} 

        Here is the refactored code:
        <refactored_code>
        {refactored_code}
        </refactored_code>

        Please debug the code and provide an updated version in a new <refactored_code> block.
        Explain the error and your fix in a <debugging_notes> block.
        """
        debug_output = model(debug_prompt)
        
        refactored_code = re.search(r'<refactored_code>(.*?)</refactored_code>',
                                    debug_output, re.DOTALL).group(1)
        debugging_notes = re.search(r'<debugging_notes>(.*?)</debugging_notes>',
                                    debug_output, re.DOTALL).group(1)
        logging.info(f"Debugging Notes: {debugging_notes}")

    # Extract the research assistant's answer from the stdout  
    assistant_answer = stdout
    
    # Grade the answer
    grade, justification = grade_answer(user_question, assistant_answer, 
                                        ideal_answer, model)

    logging.info(f"""
    Refactored Code: 
    {refactored_code}

    Research Assistant Answer:
    {assistant_answer}
    
    Grade: {grade}
    
    Justification: {justification}
    """)

if __name__ == "__main__":
    main()


# The key steps:

# 1. Define the LLM prompt template with the instructions 
# 2. Call the LLM with the prompt filled in with the source code, user question and ideal answer
# 3. Parse the LLM output to extract the refactored code, assistant answer, grade and justification 
# 4. Run the refactored code, capturing stdout, stderr and any exceptions
# 5. If there was an exception, go back to the LLM for debugging help and retry
# 6. Extract the assistant's answer from the refactored code's stdout output
# 7. Grade the assistant's answer using the LLM (without revealing the ideal answer)
# 8. Log the final refactored code, answer, grade and justification 

# It automates the process of refactoring the code via LLM suggestions, executing it to get an answer, and grading that answer via LLM while keeping the ideal answer hidden.

# The run_code function allows executing arbitrary code strings and capturing stdout/stderr. 

# The grade_answer function constructs a prompt to have the LLM grade the assistant's answer without comparing to the ideal.

# The exec statements are used to dynamically execute the source code strings, but should be used with caution.

# Let me know if you have any other questions!