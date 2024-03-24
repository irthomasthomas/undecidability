Variables:

{'$CORRECT_ANSWER', '$SOURCE_CODE', '$USER_QUESTION'}

************************

Prompt:
Your task is to refactor the research assistant agent source code provided in the {$SOURCE_CODE}
tags below to make it fully and automatically testable. The goal is to ensure the refactored code
can correctly answer the {$USER_QUESTION} and match the {$CORRECT_ANSWER} in the shortest time
possible.

<source_code>
{$SOURCE_CODE}
</source_code>

To test and refactor the code, follow these steps:

1. Execute the source code with the provided user question:
<user_question>{$USER_QUESTION}</user_question>
Capture any exceptions, failures, or output produced.

2. Compare the output to the correct answer:
<correct_answer>{$CORRECT_ANSWER}</correct_answer>
Assess whether the code produced the expected result.

3. In a <suggestions> block, provide detailed suggestions on how to refactor the source code to make
it functional and fully testable. Consider improvements to error handling, modularity, and
testability.

4. Refactor the source code based on your suggestions. Aim to make the code as clean, efficient, and
testable as possible. Place the refactored code inside <refactored_code> tags.

5. Re-execute the refactored code with the {$USER_QUESTION}. Parse the answer and compare it to the
{$CORRECT_ANSWER}. In an <assessment> block, provide a detailed assessment of the refactored code's
correctness and performance. Assign a numeric grade between 0 and 100.

6. In an <optimization> block, suggest further optimizations to improve the code's correctness,
speed, and efficiency. Consider techniques like multithreading and multitasking to enhance
performance.

7. Provide your final output in the following format:
<result>
<suggestions>
Your suggestions for refactoring the code.
</suggestions>

<refactored_code>
Your refactored version of the source code.
</refactored_code>

<assessment>
Your assessment of the refactored code's correctness and performance.
Grade: [numeric grade]
</assessment>

<optimization>
Your suggestions for further optimizing the code.
</optimization>
</result>

Remember, the primary goals are correctness and speed. The code does not need to be perfect, but it
should be functional, testable, and optimized for performance. Use your best judgment to balance
these objectives as you refactor and optimize the research assistant agent source code.
