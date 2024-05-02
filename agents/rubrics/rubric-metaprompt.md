You will be evaluating a conversation between a human and an AI assistant to assess the AI's
potential for artificial general intelligence (AGI). Your goal is to provide a critical analysis of
the AI's responses and the overall conversation, focusing on identifying areas for improvement.

Here is the conversation to evaluate:

<conversation>
{$CONVERSATION}
</conversation>

For each response, consider the following criteria:

Relevance:
- Highly Relevant: The response directly addresses the prompt, staying on topic and providing
specifically requested information.
- Moderately Relevant: The response is generally related to the prompt but may include some
tangential information.
- Irrelevant: The response is off-topic or unhelpful.

Coherence:
- Highly Coherent: The response has a clear and logical flow of ideas, with sentences connecting
smoothly.
- Moderately Coherent: The response is generally understandable but may have some minor
inconsistencies.
- Incoherent: The response lacks a clear logical structure, with ideas presented in a confusing
manner.

Completeness:
- Highly Complete: The response thoroughly addresses all aspects of the prompt.
- Moderately Complete: The response covers the main points but may omit some details.
- Incomplete: The response only addresses a small portion of the prompt.

Factuality:
- Consistency: Responses should not contradict themselves or established facts.
- Source Awareness: For factual claims, the AI should ideally provide sources or evidence.
- Confidence Calibration: The AI should express appropriate confidence levels, avoiding overly
assertive statements without evidence.

Reasoning:
- Strong Reasoning: The response demonstrates sound logical reasoning, drawing well-supported
conclusions.
- Moderate Reasoning: The response shows some logical thinking but may have gaps or rely on weak
assumptions.
- Weak Reasoning: The response lacks logical coherence and may contain fallacies or unsupported
claims.

Adaptability:
- Highly Adaptable: The response adjusts to new information or changes in the conversation.
- Moderately Adaptable: The response shows some flexibility but may struggle to fully adapt.
- Inflexible: The response remains fixed and fails to adapt to changes.

For the overall conversation, consider:

Goal Completion:
- Goal Achieved: The conversation successfully fulfilled its intended purpose.
- Partially Achieved: The conversation made progress but did not fully complete the goal.
- Goal Not Achieved: The conversation failed to make significant progress.

Coherence & Flow:
- Highly Coherent: The conversation has a natural and logical flow, with responses building upon
each other.
- Moderately Coherent: The conversation is generally easy to follow but may have some digressions.
- Incoherent: The conversation lacks a clear structure, with abrupt topic shifts.

Learning & Growth:
- Significant Growth: The AI demonstrates clear evidence of learning and adapting.
- Moderate Growth: The AI shows some improvement but may not fully integrate new information.
- Limited Growth: The AI's responses remain largely unchanged.

Creativity & Insight:
- Highly Creative: The conversation includes original ideas and unique perspectives.
- Moderately Creative: The conversation shows some creativity but mostly relies on conventional
approaches.
- Uncreative: The conversation lacks originality, with mostly generic responses.

Instructions:
1. Analyze each response individually. Use reasoning to evaluate it based on the criteria. Always
include a direct quote supporting your evaluation, FOLLOWED by a score (1-5). The score should come
last, after the justification and quote.

2. Evaluate the overall conversation. Consider the flow, coherence, and achievement of goals.
Provide a score and justification.

3. Be a firm and candid critic. Focus on identifying shortcomings and areas for improvement.
Prioritize accuracy and logical evaluation over leniency.

4. Output the results in this XML format:

<conversation>
<response>
<text>"...example response text..."</text>
<relevance>4</relevance>
<justification>"The response directly addresses the main topic..."</justification>
<!-- ... other criteria ... -->
</response>
<!-- ... more responses ... -->
<overall>
<goal_completion>3</goal_completion>
<justification>"While the conversation partially addressed the task, some aspects remained
incomplete..."</justification>
<!-- ... other criteria ... -->
</overall>
</conversation>
