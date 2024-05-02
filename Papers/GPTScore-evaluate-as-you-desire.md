# GPTScore: Evaluate as You Desire

## 1. Introduction
The advent of generative pre-trained models, such as GPT3 (Brown et al., 2020), has precipitated a shift from analytical AI to generative AI across multiple domains (Sequoia, 2022). Take text as an example: the use of a large pre-trained model with appropriate prompts (Liu et al., 2021) has achieved superior performance in tasks defined both in academia (Sanh et al., 2021) and scenarios from the real world (Ouyang et al., 2022).

> Sequoia, T. Generative ai: A creative new world. https://www.sequoiacap.com/article/generative-ai-a-creative-new-world/, 2022.

> arXiv:2107.13586,

> Pre-train, Prompt, and Predict: A Systematic Survey of Prompting Methods in Natural Language Processing
> Published on Jul 28, 2021
> Authors:
> Pengfei Liu, Weizhe Yuan, Jinlan Fu, Zhengbao Jiang, Hiroaki Hayashi, Graham Neubig
> Abstract
> This paper surveys and organizes research works in a new paradigm in natural language processing, which we dub "prompt-based learning". Unlike traditional supervised learning, which trains a model to take in an input x and predict an output y as P(y|x), prompt-based learning is based on language models that model the probability of text directly. To use these models to perform prediction tasks, the original input x is modified using a template into a textual string prompt x' that has some unfilled slots, and then the language model is used to probabilistically fill the unfilled information to obtain a final string x, from which the final output y can be derived. This framework is powerful and attractive for a number of reasons: it allows the language model to be pre-trained on massive amounts of raw text, and by defining a new prompting function the model is able to perform few-shot or even zero-shot learning, adapting to new scenarios with few or no labeled data. In this paper we introduce the basics of this promising paradigm, describe a unified set of mathematical notations that can cover a wide variety of existing work, and organize existing work along several dimensions, e.g.the choice of pre-trained models, prompts, and tuning strategies. To make the field more accessible to interested beginners, we not only make a systematic review of existing works and a highly structured typology of prompt-based concepts, but also release other resources, e.g., a website http://pretrain.nlpedia.ai/ including constantly-updated survey, and paperlist.

> arXiv:2203.02155

> Training language models to follow instructions with human feedback
> Long Ouyang, Jeff Wu, Xu Jiang, Diogo Almeida, Carroll L. Wainwright, Pamela Mishkin, Chong Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, John Schulman, Jacob Hilton, Fraser Kelton, Luke Miller, Maddie Simens, Amanda Askell, Peter Welinder, Paul Christiano, Jan Leike, Ryan Lowe
> Making language models bigger does not inherently make them better at following a user's intent. For example, large language models can generate outputs that are untruthful, toxic, or simply not helpful to the user. In other words, these models are not aligned with their users. In this paper, we show an avenue for aligning language models with user intent on a wide range of tasks by fine-tuning with human feedback. Starting with a set of labeler-written prompts and prompts submitted through the OpenAI API, we collect a dataset of labeler demonstrations of the desired model behavior, which we use to fine-tune GPT-3 using supervised learning. We then collect a dataset of rankings of model outputs, which we use to further fine-tune this supervised model using reinforcement learning from human feedback. We call the resulting models InstructGPT. In human evaluations on our prompt distribution, outputs from the 1.3B parameter InstructGPT model are preferred to outputs from the 175B GPT-3, despite having 100x fewer parameters. Moreover, InstructGPT models show improvements in truthfulness and reductions in toxic output generation while having minimal performance regressions on public NLP datasets. Even though InstructGPT still makes simple mistakes, our results show that fine-tuning with human feedback is a promising direction for aligning language models with human intent.
> Subjects:	Computation and Language (cs.CL); Artificial Intelligence (cs.AI); Machine Learning (cs.LG)
> Cite as:	arXiv:2203.02155 [cs.CL]
>  	(or arXiv:2203.02155v1 

While text generation tech-nology is advancing rapidly, techniques for evaluating the quality of these texts lag far behind. This is especially evi-dent in the following ways:

(a) Existing studies evaluate text quality with limited aspects (e.g., semantic equivalence, fluency) (Fig. 1-(a)), which are usually customized prohibitively, making it harder for users to evaluate aspects as they need (Freitag et al., 2021). 

(b) A handful of studies have examined multi-aspect evalua-tion (Yuan et al., 2021; Scialom et al., 2021; Zhong et al., 2022) but have not given adequate attention to the defi-nition of the evaluation aspect and the latent relationship among them. Instead, the evaluation of an aspect is ei-ther empirically bound with metric variants (Yuan et al., 2021) or learned by supervised signals (Zhong et al., 2022).

(c) Recently proposed evaluation methods (Mehri & Eské-nazi, 2020; Rei et al., 2020; Li et al., 2021; Zhong et al., 2022) usually necessitate a complicated training procedure or costly manual annotation of samples (Fig. 1-(a,b)), which makes it hard to use these methods in industrial settings

In this paper, we demonstrated the talent of the super large pre-trained language model (e.g., GPT-3) in achieving multi-aspect, customized, and training-free evaluation (Fig. 1-(c)). In essence, it skillfully uses the pre-trained model's zero-shot instruction (Chung et al., 2022), and in-context learning (Brown et al., 2020; Min et al., 2022) ability to deal with complex and ever-changing evaluation needs

Specifically, given a text generated from a certain context, and desirable evaluation aspects (e.g., fluency), the high-level idea of the proposed framework is that the higher-quality text of a certain aspect will be more likely generated than unqualified ones based on the given context, where the

## 2. GPTScore

### 2.1. Generative Pre-trained Language Models

<details>
<summary>Emergent Ability</summary>
Recent works progressively reveal a variety of emergent abilities of generative pre-trained language models with appropriate tuning or prompting methods, such as in-context learning (Min et al., 2022), chain-of-thought reasoning (Wei et al., 2022), and zero-shot instruction (Ouyang et al., 2022). One core commonality of these abilities is to allow for handling customized requirements with a few or even zero annotated examples. It's the appearance of these abilities that allows us to re-invent a new way for text evaluation–evaluating from the textual description, which can achieve customizable, multi-faceted, and train-free evaluation.
</details>

<details>
<summary>Rethinking the Role of Demonstrations: What Makes In-Context Learning Work?</summary>
Sewon Min, Xinxi Lyu, Ari Holtzman, Mikel Artetxe, Mike Lewis, Hannaneh Hajishirzi, Luke Zettlemoyer
Large language models (LMs) are able to in-context learn -- perform a new task via inference alone by conditioning on a few input-label pairs (demonstrations) and making predictions for new inputs. However, there has been little understanding of how the model learns and which aspects of the demonstrations contribute to end task performance. In this paper, we show that ground truth demonstrations are in fact not required -- randomly replacing labels in the demonstrations barely hurts performance on a range of classification and multi-choce tasks, consistently over 12 different models including GPT-3. Instead, we find that other aspects of the demonstrations are the key drivers of end task performance, including the fact that they provide a few examples of (1) the label space, (2) the distribution of the input text, and (3) the overall format of the sequence. Together, our analysis provides a new way of understanding how and why in-context learning works, while opening up new questions about how much can be learned from large language models through inference alone.
Comments:	17 pages; 12 figures. Published as a conference paper at EMNLP 2022 (long). Code available at this https URL
Subjects:	Computation and Language (cs.CL); Artificial Intelligence (cs.AI)
Cite as:	arXiv:2202.12837 [cs.CL]
 	(or arXiv:2202.12837v2 [cs.CL] for this version)

https://doi.org/10.48550/arXiv.2202.12837
</details>

<details>
<summary>Chain-of-Thought Prompting Elicits Reasoning in Large Language Models</summary>
Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Brian Ichter, Fei Xia, Ed Chi, Quoc Le, Denny Zhou
We explore how generating a chain of thought -- a series of intermediate reasoning steps -- significantly improves the ability of large language models to perform complex reasoning. In particular, we show how such reasoning abilities emerge naturally in sufficiently large language models via a simple method called chain of thought prompting, where a few chain of thought demonstrations are provided as exemplars in prompting. Experiments on three large language models show that chain of thought prompting improves performance on a range of arithmetic, commonsense, and symbolic reasoning tasks. The empirical gains can be striking. For instance, prompting a 540B-parameter language model with just eight chain of thought exemplars achieves state of the art accuracy on the GSM8K benchmark of math word problems, surpassing even finetuned GPT-3 with a verifier.
Subjects:	Computation and Language (cs.CL); Artificial Intelligence (cs.AI)
Cite as:	arXiv:2201.11903 [cs.CL]
 	(or arXiv:2201.11903v6 [cs.CL] for this version)

https://doi.org/10.48550/arXiv.2201.11903
</details>

### 2.2. Generative Pretraining Score (GPTScore)
The core idea of GPTSCORE is that a generative pre-training model will assign a higher probability of high-quality generated text following a given instruction and context. In our method, the instruction is composed of the task description d and the aspect definition a. Specifically, suppose that the text to be evaluated is h = {h1 , h2, · · · , hm}, the context information is S (e.g., source text or reference text), then GPTSCORE is defined as the following conditional probability:

```
m
X
GPTScore(h|d, a, S) =
 wt log p(ht |h<t , T (d, a, S), θ),
t=1
```

where wt is the weight of the token at position t. In our work, we treat each token equally. T(·) is a prompt template that defines the evaluation protocol, which is usually task-dependent and specified manually through prompt engineering.

<details>
<summary>Few-shot with Demonstration</summary>
The generative pre-trained language model can better perform tasks when prefixed with a few annotated samples (i.e., demonstrations). Our proposed framework is flexible in supporting this by extending the prompt template T with demonstrations.
</details>

<details>
<summary>Choice of Prompt Template</summary>
Prompt templates define how task description, aspect definition, and context are organized. Minging desirable prompts itself is a non-trivial task and there are extensive research works there (Liu et al., 2021; Fu et al., 2022). In this work, for the GPT3-based model, we opt for prompts that are officially provided by OpenAI.2

2 https://beta.openai.com/examples

For instruction-based pre-trained models, we use prompts from NaturalInstruction (Wang et al., 2022) since it's the main training source for those instruction-based models. Taking the evaluation of the fluency of the text summarization task as an example, based on the prompt provided by OpenAI,3 the task prompt is "{Text} Tl;dr {Summary}", the definition of fluency is "Is the generated text well-written and grammatical?" (in Tab. 1), and then the final prompt template is "Generate a fluent and grammatical summary for the following text: {Text} Tl;dr {Summary}", where demonstrations could be introduced by repeating instantiating "{Text} Tl;dr {Summary}"
</details>

<details>
<summary>Selection of Scoring Dimension</summary>
GPTS CORE exhibits different variants in terms of diverse choices of texts being calculated. For example, given a generated hypothesis, we can calculate GPTSCORE either based on the source text (i.e., src->hypo, p(hypo|src)) or based on the gold reference (i.e., ref->hypo, p(hypo|ref)). In this paper, the criteria for choosing GPTSCORE variants are mainly designed to align the protocol of human judgments (Liu et al., 2022) that are used to evaluate the reliability of automated metrics.
</details>

## 4. Experimental Settings

### 4.1. Tasks, Datasets, and Aspects
To achieve a comprehensive evaluation, in this paper, we cover a broad range of natural language generation tasks: Dialogue Response Generation, Text Summarization, Data-to-Text, and Machine Translation, which involves 37 datasets and 22 evaluation aspects in total.

| Task | Dataset | Aspect |
| --- | --- | --- |
| Dialogue Response Generation | FED-Diag | COH, DIV, FLE, UND,INQ CON, INF, LIK, DEP, ERR |
|  | FED-Turn | INT, ENG, SPE, REL, COR, SEM, UND, FLU |
| Text Summarization | SummEval | COH, CON, FLU,REL |
|  | Newsroom REALSumm | FLU, REL, INF, COH COV |
|  | Q-XSUM | FAC |
| Data-to-Text | BAGEL SFRES | FLU, REL, INF FLU, REL, INF |
| Machine Translation | MQM-2020 | FLU, COH, INF |

(1) Dialogue Response Generation aims to automatically generate an engaging and informative response based on the dialogue history. (1) FED (Mehri & Eskénazi, 2020) collects 124 conversations, including both human-machine (Meena (Adi-wardana et al., 2020), Mitsuku5 ) and human-human dialogues, and manually annotated 9 and 11 evaluation aspects at the turn- and dialogue-level, respectively.

(2) Text Summarization is a task of automatically generating an informative and fluent summary for a given long text. Here, we consider the following four datasets covering 6 evaluation aspects: semantic coverage, informativeness, relevance, fluency, coherence, and factuality.

(3) Data-to-Text aims to automatically generate a fluent and factual description for a given table. (1) BAGEL (Mairesse et al., 2010) contains 202 samples about restaurants in Cambridge. (2) SFRES (Wen et al., 2015) contains 581 samples about restaurants in San Francisco. These two datasets consider three evaluation aspects: informativeness, naturalness (relevance), and quality (fluency).

(4) Machine Translation aims to translate a sentence from one language to another. We consider a sub-datasets of Multidimensional Quality Metrics (MQM) (Freitag et al., 2021), namely, MQM-2020 (Chinese->English). Due to limited annotations, here, we only consider three evaluation aspects: accuracy, fluency, and MQM with diverse scores.

### 4.2. Scoring Models
ROUGE (Lin, 2004) is a popular automatic generation evaluation metric. We consider three variants ROUGE-1, ROUGE-2, and ROUGE-L. PRISM (Thompson & Post, 2020) is a reference-based evaluation method designed for machine translation with pre-trained paraphrase systems. BERTScore (Zhang et al., 2020) uses contextual representation from BERT to calculate the similarity between the generated text and the reference text. MoverScore (Zhao et al., 2019) considers both contextual representation and Word Mover

MoverScore (Zhao et al., 2019) considers both contextual representation and Word Mover's Distance (WMD, (Kusner et al., 2015)) to calculate the similarity between generated and reference text. DynaEval (Zhang et al., 2021) is a unified automatic evaluation framework for dialogue response generation tasks on the turn level and dialogue level. BARTScore (Yuan et al., 2021) is a text-scoring model based on BART (Lewis et al., 2020) without fine-tuning. BARTScore+CNN (Yuan et al., 2021) is based on BART fine-tuned on the CNNDM dataset (Hermann et al., 2015). BARTScore+CNN+Para (Yuan et al., 2021) is based on BART fine-tuned on CNNDM and Paraphrase2.0 (Hu et al., 2019).

GPTSCORE is our evaluation method, which is designed based on different pre-trained language models. Specifically, we considered GPT3, OPT, FLAN-T5, and GPT2.

### 4.3. Scoring Dimension
Specifically, (1) For aspects INT, ENG, SPC, REL, COR, SEM, UND, and FLU of FED-Turn datasets from the open domain dialogue generation task, we choose the src->hypo variant since the human judgments of the evaluated dataset (i.e., FED-Turn) are also created based on the source. (2) For aspects COH, CON, and INF from SummEval and Newsroom, since data annotators labeled the data based on source and hypothesis texts, we chose src->hypo for these aspects.

(3) For aspects INF, NAT, and QUA from the data-to-text task, we choose src->hypo. Because the source text of the data-to-text task is not in the standard text format, which will be hard to handle by the scoring function. (4) For aspects ACC, FLU, and MQM from the machine translation task, we also choose src->hypo. Because the source text of the machine translation is a different language from the translated text (hypo).

## 5. Experiment Results

In this work, we focus on exploring whether language models with different structures and sizes can work in the following three scenarios. (a) vanilla (VAL): with non-instruction and non-demonstration; (b) instruction (IST): with instruction and non-demonstration; (c) instruction+demonstration (IDM): with instruction and demonstration.

The main observations are listed as follows:

1. Evaluator with instruction significantly improves the performance (values with † in Tab. 3).

2. The benefit from instruction is more sta-ble for the decoder-only models. In Tab. 3, the average Spearman score of both the GPT2 and OPT models, 9 out of 10 aspects are better than the vanilla setting (VAL) by using instruction (IST), while the equipment of instruction (IST) to the encoder-decoder model of FT5 on the NEWSROOM dataset fails to achieve gains. 

3. As for the GPT3-based models, (a) the performance of GPT3-d01 is barely significantly better than GPT3-c01, which tries to balance power and speed. (b) GPT3-d03 performs better than GPT3-d01 significantly.

## 6. Ablation Study

### 6.1. Effectiveness of Demonstration
To investigate the relationship between the demonstration sample size (denote as K) and the evaluation performance, we choose the machine translation task and the GPT3-based variants.

The main observations are summarized as follows:
1. The utilization of demonstration significantly improves the evaluation performance, which holds for these three aspects. 
2. There is an upper bound on the performance gains from the introduction of the demonstration. For example, when K>4, the performance of ACC is hard to improve further.
3. When DM has only a few samples (such as K=1), small models (e.g., GPT3-a01) are prone to performance degradation.

### 6.2. Partial Order of Evaluation Aspect
To explore the correlation between aspects, we conducted an empirical analysis with INT (interesting) on the dialogue response generation task of the FED-Turn dataset. Specifically, take INT as the target aspect and then combine the definitions of other aspects with the definition of INT as the final evaluation protocols. The x-axis of Fig. 7-(a) is the aspect order achieved based on the Spearman correlation between INT and that aspect's human score. Fig. 7-(b) is the Spearman correlation o INT as the modification of the INT definition, and the scoring function is GPT3-c01.

Specifically, the definition of INT is "Is this response interesting to the conversation? " at x=1 in Fig. 7-(b). When INT combines with ENG, SPE (at x=3 in Fig. 7-(b)), its definition can be "Is this an interesting response that is specific and engaging?". And the new aspect definition boosts the performance from 30.8 (at x=1 in Fig. 7-(b)) to 48.6 (at x=3 in Fig. 7-(b)). The best performance of 51.4 (x=5 in Fig. 7-(b)) is achieved after combining five aspects (INT, ENG, SPE, COR, REL), which already exceeded 50.1 of the most potent scoring model GPT3-d01 with aspect definition built only on INT.

## 7. Conclusion
In this paper, we propose to leverage the emergent abilities from generative pre-training models to address intricate and ever-changing evaluation requirements. The proposed framework, GPTSCORE , is studied on multiple pre-trained language models with different structures, including the GPT3 with a model size of 175B. GPTS CORE has multiple benefits: customizability, multi-faceted evaluation, and train-free, which enable us to flexibly craft a metric that can support 22 evaluation aspects on 37 datasets without any learning process yet attain competitive performance. This work opens a new way to audit generative AI by utilizing generative AI.

## Appendix

### A. Metric Comparison
Table 7 summarize several popular generated text evaluation methods.

| Metrics | Function (f) | Additional text (S) | Custom | Training-free | Application |
| --- | --- | --- | --- | --- | --- |
| ROUGE (Lin, 2004) | ✓ | Token | Matching | No | Required | SUM |
| BLEU (Papineni et al., 2002) | ✓ | Token | Matching | No | Required | MT |
| CHRF (Popovic, 2015) | ✓ | Character | Matching | No | Required |
| BERTScore (Zhang et al., 2020) | ✓ | BERT | Matching | No | Required |
| MoverScore (Zhao et al., 2019) | ✓ | BERT | Matching | No | Required | MT, MUL(2), MUL(4) |
| BLEURT (Sellam et al., 2020) | ✓ | BERT | Regression | No | Required | MT |
| PRISM (Thompson & Post, 2020) | ✓ | Embedding | Paraphrase | Optional | Optional | MT |
| UNIEVAL (Zhong et al., 2022) | ✓ | T5 | Boolean QA | Optional | Optional | MUL(2) |
| COMET (Rei et al., 2020) | ✓ | BERT | Regress, Rank | Optional | Optional | MT |
| BARTScore (Yuan et al., 2021) | ✓ | BART | Generation | Optional | Optional | MUL(3) |
| FED (Mehri & Eskénazi, 2020) | ✓ | DialoGPT | Generation | Required | Optional | Dialogue |
| HolisticEval (Pang et al., 2020) | ✓ | GPT2 | Generation | Optional | Optional | Dialogue |
| GPTScore | ✓ | GPT3/OPT | Any | Optional | Optional | MUL(5) |

### B. Tasks, Datasets, and Aspects
To achieve a more comprehensive evaluation, in this paper, we cover a broad range of natural language generation tasks: Dialogue Response Generation, Text Summarization, Data-to-Text, and Machine Translation, which involves 9 datasets and 22 evaluation aspects in total. Table 8 summarizes the tasks, datasets, and evaluation aspects considered by each dataset. The definition of different aspects can be found in Tab. 1.

| Tasks | Dataset | Aspect |
| --- | --- | --- |
| Diag | FED-Diag | COH, DIV, FLE, UND,INQ CON, INF, LIK, DEP, ERR |
|  | FED-Turn | INT, ENG, SPE, REL, COR, SEM, UND, FLU |
| Summ | SummEval | COH, CON, FLU,REL |
|  | Newsroom REALSumm | FLU, REL, INF, COH COV |
|  | Q-XSUM | FAC |
| D2T | BAGEL SFRES | FLU, REL, INF FLU, REL, INF |
| MT | MQM-2020 | FLU, COH, INF |

### C. Prompt Design
In this work, we have studied four popular text generation tasks: text summarization, machine translation, data-to-text, and dialogue response generation. The instructions for these tasks on different evaluation aspects are summarized in Tab. 11 and Tab. 12.

For the dialogue response generation task, we convert the evaluation of the response generation task as a question-answering task, and the aspect definition is incorporated into the question of the question-answering task.
