import openai
import os
import subprocess
import sys
import tempfile

openai.api_key = "YOUR_API_KEY"

def get_llm_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1000,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

def main():
    user_question = sys.argv[1] 
    ideal_answer = sys.argv[2]
    source_code = sys.argv[3]
    
    prompt = f"""
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
"""
    
    while True:
        llm_response = get_llm_response(prompt)
        
        # Extract refactored code
        refactored_code_start = llm_response.find("<refactored_code>") + len("<refactored_code>")
        refactored_code_end = llm_response.find("</refactored_code>")
        refactored_code = llm_response[refactored_code_start:refactored_code_end].strip()
        
        # Write refactored code to temp file and execute
        with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as temp:
            temp.write(refactored_code)
            temp_path = temp.name
        
        try:
            output = subprocess.check_output([sys.executable, temp_path, user_question], stderr=subprocess.STDOUT,
                                             universal_newlines=True)
        except subprocess.CalledProcessError as e:
            output = e.output
        
        # Extract assistant answer from output  
        answer_start = output.find("<answer>") + len("<answer>")
        answer_end = output.find("</answer>")
        if answer_start != -1 and answer_end != -1:
            answer = output[answer_start:answer_end].strip()
        else:
            answer = ""
        
        # Grade answer
        grading_prompt = f"""
Grade the following research assistant answer to the user question against the ideal answer.
Do not reveal the ideal answer in your response.

User question: {user_question}

Research assistant answer: {answer}  
"""
        grading_response = get_llm_response(grading_prompt)

        grade_start = grading_response.find("<grade>") + len("<grade>") 
        grade_end = grading_response.find("</grade>")
        grade = grading_response[grade_start:grade_end].strip()

        justification_start = grading_response.find("<justification>") + len("<justification>")
        justification_end = grading_response.find("</justification>")  
        justification = grading_response[justification_start:justification_end].strip()

        print(f"<refactored_code>\n{refactored_code}\n</refactored_code>")
        print(f"\n<research_assistant_answer>\n{answer}\n</research_assistant_answer>") 
        print(f"\n<grade>\n{grade}\n</grade>")
        print(f"\n<justification>\n{justification}\n</justification>")
        
        if grade.startswith("A"):
            # Success, exit loop
            break
        else:
            # Append previous attempt to prompt for next iteration  
            prompt += f"\n\nPrevious attempt:\n{llm_response}\n\nThe research assistant's answer based on the refactored code was:\n{answer}\n\nThis attempt received a grade of {grade} for the following reason: {justification}"

        os.remove(temp_path)
        
if __name__ == "__main__":
    main()

# To run it:

# ```
# python script.py "USER_QUESTION" "IDEAL_ANSWER" "SOURCE_CODE" 
# ```

# This script will:
# 1. Take in the user question, ideal answer, and source code as command line arguments 
# 2. Construct the prompt for the LLM
# 3. Enter a loop where it:
#     - Gets the LLM's response with refactored code and suggestions
#     - Extracts the refactored code 
#     - Executes it with the user question as input
#     - Extracts the assistant's answer from the output
#     - Grades the answer against the ideal using the LLM
#     - Prints the refactored code, answer, grade, and justification 
#     - If the grade is an A, exits the loop. Otherwise appends the attempt to the prompt for the next iteration.

# The loop will continue refining the code until the LLM determines the research assistant's answer matches the ideal answer sufficiently to receive an A grade.

# Let me know if you have any other questions!
