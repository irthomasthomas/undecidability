Variables:

{'$CORRECT_ANSWER', '$SOURCE_CODE', '$USER_QUESTION'}

************************

Prompt:
Your task is to refactor the source code for a research_assistant_agent so that it can be fully
tested and executed automatically. The goal is to modify the code to make it testable and optimized
while still producing the correct answer to a given user question.

Here is the current source code for the research_assistant_agent:

<source_code>
{$SOURCE_CODE}
</source_code>

To test the refactored code, you will need two inputs:
<user_question>
{$USER_QUESTION}
</user_question>

This is the question that will be answered by the research_assistant_agent. It will be retrieved
from a file at runtime, so it will not be directly passed to the language model doing the software
testing.

<correct_answer>
{$CORRECT_ANSWER}
</correct_answer>

This is the known correct answer to the user question, which will be used to evaluate if the
refactored research_assistant_agent is working properly.

Please refactor the source code using the following steps:

1. Execute the current source code or test code and capture any exceptions, failures, or incorrect
outputs.

2. Analyze the results and brainstorm suggestions for refactoring the code to resolve any issues and
make it more suitable for testing. Provide your suggestions inside <refactoring_suggestions> tags.

<refactoring_suggestions>
3. Refactor the source code based on your suggestions. Aim to optimize the code for correctness,
testability, and speed. Use multithreading and multitasking wherever possible to improve
performance. Print the refactored code inside <refactored_code> tags.

<refactored_code>
4. Re-execute the refactored code and repeat steps 1-3 as needed until the research_assistant_agent
is able to produce the correct answer without any exceptions or failures.

5. Once the refactored code is executing successfully, parse the research_assistant_agent's final
answer and compare it to the known correct answer using a strong language model. Provide the
comparison inside <answer_comparison> tags, and then state whether the answer is correct or not
inside <is_answer_correct> tags.

<answer_comparison>
<is_answer_correct>

Remember, the ultimate goal is to refactor the code so that the research_assistant_agent produces
the correct answer in the shortest amount of time, while being fully testable and optimized. Let me
know if you have any other questions!
