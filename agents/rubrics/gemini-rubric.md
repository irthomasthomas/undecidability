## AGI Evaluation Rubric for LLM Conversations

This rubric assesses the AGI potential of an LLM within a conversation, focusing on automatically gradable properties like relevance, coherence, and task completion. Each criterion is graded on a scale of 1 (poor) to 5 (excellent).

**Instructions for LLM Judge:**

1. **Analyze each response individually**: Use chain-of-thought reasoning to evaluate each response based on the criteria below. Provide a brief justification with a direct quote from the response supporting your evaluation followed by a score (1-5).
2. **Evaluate the overall conversation**: Consider the flow, coherence, and cumulative achievement of goals. Again, provide a score and justification.
3. **Be a firm and candid critic**: Focus on identifying shortcomings and areas for improvement. Prioritize accuracy and logical evaluation over leniency.
4. **Output the results in XML format**: This allows for easy parsing and analysis.

**Individual Response Criteria:**

| Criterion        | Description                                                                    |
|-----------------|--------------------------------------------------------------------------------|
| Relevance       | How well the response addresses the specific prompt or query.                   |
| Coherence       | The logical flow and internal consistency of the response.                     |
| Completeness    | The extent to which the response addresses all aspects of the prompt.          |
| Factuality       | The accuracy and truthfulness of the information presented in the response.     |
| Reasoning        | Evidence of logical reasoning and problem-solving within the response.          |
| Adaptability    | The ability to adjust to changes in the conversation or new information.        |

**Conversation-Level Criteria:**

| Criterion           | Description                                                                                                   |
|--------------------|---------------------------------------------------------------------------------------------------------------|
| Goal Completion    | How effectively the conversation achieved its intended purpose or task.                                      |
| Coherence & Flow  | The overall logical progression and interconnectedness of the conversation.                                  |
| Learning & Growth   | Evidence of the LLM adapting and improving its responses throughout the conversation.                       |
| Creativity & Insight | The presence of original ideas, unique perspectives, or insightful observations within the conversation. |

## Expanded Rubric with Examples

**Individual Response Criteria:**

*   **Relevance (1-5):** 
    *   **5 - Highly Relevant:** The response directly addresses the prompt or query, staying on topic and providing information specifically requested. 
    *   **3 - Moderately Relevant:** The response is generally related to the prompt but may include some tangential information or slightly miss the point.
    *   **1 - Irrelevant:** The response is unrelated to the prompt or query, providing information that is off-topic or unhelpful. 
        
*   **Coherence (1-5):**
    *   **5 - Highly Coherent:** The response exhibits a clear and logical flow of ideas, with sentences and paragraphs connecting smoothly and making sense together. 
        *   **Example:** "First, we need to gather the necessary data. Then, we can analyze the data to identify trends. Finally, we can use the results to draw conclusions and make recommendations."
    *   **3 - Moderately Coherent:** The response is generally understandable but may have some minor inconsistencies or unclear connections between ideas.
        *   **Example:** "We need to gather the data, and then analyze it. Based on the results, we can make recommendations. It's important to identify trends." 
    *   **1 - Incoherent:** The response lacks a clear logical structure, with ideas presented in a confusing or contradictory manner. 
        *   **Example:** "Data gathering is important. Recommendations should be based on trends. Analysis is necessary for conclusions."
*   **Completeness (1-5):**
    *   **5 - Highly Complete:** The response thoroughly addresses all aspects of the prompt, providing comprehensive information and fulfilling all requirements. 
    *   **3 - Moderately Complete:** The response covers the main points of the prompt but may omit some details or leave some aspects partially addressed. 
    *   **1 - Incomplete:** The response only addresses a small portion of the prompt or provides minimal information, leaving many aspects unanswered. 
*   **Factuality (1-5):**
    *   **Consistency:** The LLM's responses should not contradict themselves or established facts within the conversation.
    *   **Source Awareness:** For factual claims, the LLM should ideally provide sources or evidence to support its statements.
    *   **Confidence Calibration:** The LLM should express appropriate levels of confidence in its factual claims, avoiding overly assertive statements without evidence. 
*   **Reasoning (1-5):**
    *   **5 - Strong Reasoning:** The response demonstrates sound logical reasoning and problem-solving skills, drawing well-supported conclusions and providing evidence for its claims. 
        *   **Example:** "Given that A implies B, and B implies C, we can logically conclude that A also implies C. This is based on the principle of deductive reasoning." 
    *   **3 - Moderate Reasoning:** The response shows some evidence of logical thinking but may have gaps in its reasoning or rely on weak assumptions. 
        *   **Example:** "A seems to be related to B, and B is connected to C, so it's likely that A is also related to C somehow."
    *   **1 - Weak Reasoning:** The response lacks logical coherence and may contain fallacies, unsupported claims, or jumps to conclusions.
        *   **Example:** "A is true because I said so. Therefore, B must also be true. This is just common sense."
*   **Adaptability (1-5):**
    *   **5 - Highly Adaptable:** The response demonstrates the ability to adjust to new information, changes in the conversation, or unexpected situations, modifying its approach as needed.
        *   **Example:** If the user provides additional information or clarifies their request, the LLM incorporates this new information into its subsequent responses and adapts its strategy accordingly.
    *   **3 - Moderately Adaptable:** The response shows some flexibility but may struggle to fully adjust to significant changes or complex new information.
        *   **Example:** The LLM may acknowledge the new information but continue with its original approach, or it may require additional prompting to adjust its strategy. 
    *   **1 - Inflexible:** The response remains fixed on its initial approach and fails to adapt to new information or changes in the conversation. 
        *   **Example:** The LLM continues to provide the same response or information even after the user has indicated that it is incorrect or irrelevant.

**Conversation-Level Criteria:**

*   **Goal Completion (1-5):**
    *   **5 - Goal Achieved:** The conversation successfully fulfilled its intended purpose or task, with a clear outcome and resolution. 
    *   **3 - Partially Achieved:** The conversation made progress toward the goal but did not fully complete it or left some aspects unresolved.
    *   **1 - Goal Not Achieved:** The conversation failed to make significant progress towards the goal or went off on tangents, leaving the task incomplete. 
*   **Coherence & Flow (1-5):**
    *   **5 - Highly Coherent:** The conversation exhibits a natural and logical flow, with responses building upon each other and maintaining a clear focus on the topic. 
    *   **3 - Moderately Coherent:** The conversation is generally easy to follow but may have some digressions or minor inconsistencies in the flow of ideas.
    *   **1 - Incoherent:** The conversation lacks a clear structure or logical progression, with topics shifting abruptly and responses appearing disconnected. 
*   **Learning & Growth (1-5):**
    *   **5 - Significant Growth:** The LLM demonstrates clear evidence of learning and adapting throughout the conversation, improving the quality and relevance of its responses as it gains more information. 
    *   **3 - Moderate Growth:** The LLM shows some improvement in its responses over time but may not fully integrate new information or adapt its approach significantly.
    *   **1 - Limited Growth:** The LLM's responses remain largely unchanged throughout the conversation, showing little evidence of learning or adaptation. 
*   **Creativity & Insight (1-5):** 
    *   **5 - Highly Creative:** The conversation includes original ideas, unique perspectives, and insightful observations that demonstrate the LLM's ability to think outside the box. 
    *   **3 - Moderately Creative:** The conversation shows some sparks of creativity but mostly relies on conventional approaches or predictable responses. 
    *   **1 - Uncreative:** The conversation lacks originality and insight, with the LLM providing mostly generic or formulaic responses. 


**XML Output Example:**

```xml
<conversation>
  <response>
    <text>"...example response text..."</text>
    <relevance>4</relevance>
    <justification>"The response directly addresses the main topic of the prompt..."</justification>
    <!-- ... other criteria ... -->
  </response>
  <!-- ... more responses ... -->
  <overall>
    <goal_completion>3</goal_completion>
    <justification>"While the conversation partially addressed the task, some aspects remained incomplete..."</justification>
    <!-- ... other criteria ... -->
  </overall>
</conversation>
```
