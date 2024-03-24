Variables:

{'$CORRECT_ANSWER', '$SOURCE_CODE', '$USER_QUESTION'}

************************

Prompt:
Here is the source code to be tested and refactored:

<source_code>
{$SOURCE_CODE}
</source_code>

The user question to test the source code with is:
<user_question>{$USER_QUESTION}</user_question>

The correct answer to the user question is:
<correct_answer>{$CORRECT_ANSWER}</correct_answer>

Please follow these steps to test and refactor the source code:

1. Execute the source code with the provided user question as input. Capture any exceptions or
failures that occur.

2. Analyze the source code execution and any exceptions/failures. Write down your suggestions for
refactoring the code to make it working and fully testable in <refactoring_suggestions> tags. Focus
on changes that will allow the code to execute correctly and be automatically tested, while also
optimizing for speed through techniques like multithreading and multitasking where possible. The
code does not need to be perfect, but it should be functional and efficient.

3. Refactor the source code based on your suggestions. Provide the refactored code inside
<refactored_code> tags.

4. Re-execute the refactored source code with the user question. If it still does not execute
correctly or return the correct answer, repeat steps 2-4 until it does.

5. Once the refactored source code is executing correctly, parse the answer it returns. Compare this
answer to the provided correct answer and assign a grade to indicate how close the returned answer
is to the correct one. Provide your reasoning and the grade inside <grading_reasoning> and <grade>
tags.

6. Provide the final refactored source code inside <final_refactored_code> tags. Summarize the test
results inside <test_results> tags, including the number of iterations required, the final answer
returned, and the grade. Provide the graded answer comparison inside <graded_answer> tags.

Remember, the goal is to refactor the source code so that it executes correctly and returns the
correct answer in the shortest time possible, while also being fully testable. Aim to minimize the
number of refactoring iterations required. Let me know if you have any other questions!
