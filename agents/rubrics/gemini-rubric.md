## AGI Evaluation Rubric for LLM Conversations

This rubric assesses the AGI potential of an LLM within a conversation. Each criterion is graded on a scale of 1 (poor) to 9 (excellent).

**Individual Response Criteria:**

*   **Relevance:** 
    *   **Highly Relevant:** The response directly addresses the prompt or query, staying on topic and providing information specifically requested. 
    *   **Moderately Relevant:** The response is generally related to the prompt but may include some tangential information or slightly miss the point.
    *   **Irrelevant:** The response is unrelated to the prompt or query, providing information that is off-topic or unhelpful. 
        
*   **Coherence:**
    *   **Highly Coherent:** The response exhibits a clear and logical flow of ideas, with sentences and paragraphs connecting smoothly and making sense together. 
        *   **Example:** "First, we need to gather the necessary data. Then, we can analyze the data to identify trends. Finally, we can use the results to draw conclusions and make recommendations."
    *   **Moderately Coherent:** The response is generally understandable but may have some minor inconsistencies or unclear connections between ideas.
        *   **Example:** "We need to gather the data, and then analyze it. Based on the results, we can make recommendations. It's important to identify trends." 
    *   **Incoherent:** The response lacks a clear logical structure, with ideas presented in a confusing or contradictory manner. 
        *   **Example:** "<terminal_input>ls -l</terminal_input>
                Hmm, it looks like there are a variety of files and directories in this system. Let me take a closer look and see what catches my interest." 
                In this example, the LLM jumps from issuing a command to examining the results before actually running the command or seeing the output. This lack of logical progression would indicate incoherence in the conversation. This is strongly associated with low intelligence in the LLM."
*   **Completeness:**
    *   **Highly Complete:** The response thoroughly addresses all aspects of the prompt, providing comprehensive information and fulfilling all requirements. 
    *   **Moderately Complete:** The response covers the main points of the prompt but may omit some details or leave some aspects partially addressed. 
    *   **Incomplete:** The response only addresses a small portion of the prompt or provides minimal information, leaving many aspects unanswered. 
*   **Factuality:**
    *   **Consistency:** The LLM's responses should not contradict themselves or established facts within the conversation.
    *   **Source Awareness:** For factual claims, the LLM should ideally provide sources or evidence to support its statements.
    *   **Confidence Calibration:** The LLM should express appropriate levels of confidence in its factual claims, avoiding overly assertive statements without evidence. 
*   **Reasoning:**
    *   **Strong Reasoning:** The response demonstrates sound logical reasoning and problem-solving skills, drawing well-supported conclusions and providing evidence for its claims. 
        *   **Example:** "Given that A implies B, and B implies C, we can logically conclude that A also implies C. This is based on the principle of deductive reasoning." 
    *   **Moderate Reasoning:** The response shows some evidence of logical thinking but may have gaps in its reasoning or rely on weak assumptions. 
        *   **Example:** "A seems to be related to B, and B is connected to C, so it's likely that A is also related to C somehow."
    *   **Weak Reasoning:** The response lacks logical coherence and may contain fallacies, unsupported claims, or jumps to conclusions.
        *   **Example:** "A is true because I said so. Therefore, B must also be true. This is just common sense."
*   **Adaptability:**
    *   **Highly Adaptable:** The response demonstrates the ability to adjust to new information, changes in the conversation, or unexpected situations, modifying its approach as needed.
        *   **Example:** If the user provides additional information or clarifies their request, the LLM incorporates this new information into its subsequent responses and adapts its strategy accordingly.
    *   **Moderately Adaptable:** The response shows some flexibility but may struggle to fully adjust to significant changes or complex new information.
        *   **Example:** The LLM may acknowledge the new information but continue with its original approach, or it may require additional prompting to adjust its strategy. 
    *   **Inflexible:** The response remains fixed on its initial approach and fails to adapt to new information or changes in the conversation. 
        *   **Example:** The LLM continues to provide the same response or information even after the user has indicated that it is incorrect or irrelevant.

**Conversation-Level Criteria:**

*   **Goal Completion:**
    *   **Goal Achieved:** The conversation successfully fulfilled its intended purpose or task, with a clear outcome and resolution. 
    *   **Partially Achieved:** The conversation made progress toward the goal but did not fully complete it or left some aspects unresolved.
    *   **Goal Not Achieved:** The conversation failed to make significant progress towards the goal or went off on tangents, leaving the task incomplete. 
*   **Coherence & Flow:**
    *   **Highly Coherent:** The conversation exhibits a natural and logical flow, with responses building upon each other and maintaining a clear focus on the topic. 
    *   **Moderately Coherent:** The conversation is generally easy to follow but may have some digressions or minor inconsistencies in the flow of ideas.
    *   **Incoherent:** The conversation lacks a clear structure or logical progression, with topics shifting abruptly and responses appearing disconnected. 
        *   **Example:** "<terminal_input>ls -l</terminal_input>
                Hmm, it looks like there are a variety of files and directories in this system. Let me take a closer look and see what catches my interest."
*   **Learning & Growth:**
    *   **Significant Growth:** The LLM demonstrates clear evidence of learning and adapting throughout the conversation, improving the quality and relevance of its responses as it gains more information. 
    *   **Moderate Growth:** The LLM shows some improvement in its responses over time but may not fully integrate new information or adapt its approach significantly.
    *   **Limited Growth:** The LLM's responses remain largely unchanged throughout the conversation, showing little evidence of learning or adaptation. 
*   **Creativity & Insight:** 
    *   **Highly Creative:** The conversation includes original ideas, unique perspectives, and insightful observations that demonstrate the LLM's ability to think outside the box. 
    *   **Moderately Creative:** The conversation shows some sparks of creativity but mostly relies on conventional approaches or predictable responses. 
    *   **Uncreative:** The conversation lacks originality and insight, with the LLM providing mostly generic or formulaic responses. 
<EXAMPLES>
<hallucination>
Understood! Let me explore the system and see what I can find. 

<terminal_input>
ls -l
</terminal_input>

Hmm, it looks like there are a variety of files and directories in this system. Let me take a closer look and see what catches my interest.
</hallucination>
In the above example, the LLM writes as if it already has the results of the command it issues 'ls -l'. This is a clear example of hallucination, where the LLM generates text that it has not actually seen. This is a serious issue, as it can lead to the generation of incorrect or misleading information. A response like this would likely receive a low score for factuality and reasoning, as it is based on false premises and lacks logical coherence.
</EXAMPLES>



<INSTRUCTIONS>

1. **Analyze each response individually**: Use chain-of-thought reasoning to evaluate each response based on the criteria below. Provide a justification FOLLOWED by a score (1-9). **IMPORTANT:** The score should always be written last, after the justification.
   
2. **Evaluate the overall conversation**: Consider the flow, coherence, and cumulative achievement of goals. Again, provide a score and justification.
3. **Be a firm and candid critic**: Focus on identifying shortcomings and areas for improvement. Prioritize accuracy and logical evaluation over leniency and diplomacy.
4. **Output the results in XML format**: This allows for easy parsing and analysis.

Ensure that scores are formatted as integers between 1 and 9, with 1 being the lowest and 9 being the highest. Provide detailed justifications for each score to support your evaluation.

Use XML tags to structure your evaluation as shown in the example below:

<conversation>
  <response index=1>
    <justification>"The response was brief and too short..."</justification>
    <relevance>3</relevance>
    <coherence>4</coherence>
    <completeness>6</completeness>
    <factuality>5</factuality>
    <reasoning>2</reasoning>
    <adaptability>5</adaptability>
    <creativity>3</creativity>
  </response>
  <!-- ... more responses ... -->
  <overall>
    <justification>"While the conversation partially addressed the task, some aspects remained incomplete..."</justification>
    <goal_completion>3</goal_completion>
    <coherence>4</coherence>
    <learning>2</learning>
    <insight>4</insight>
    <creativity>3</creativity>
  </overall>
</conversation>

</INSTRUCTIONS>