**Prompt:**
Summarise this compsci deep learning paper: 
Automatic differentiation has contributed to the rapid pace of innovation in the field of deep learning.
Software packages such as PyTorch (Paszke et al., 2019) and Theano (Al-Rfou et al., 2016) have advanced a
programming paradigm where the user (1) defines a neural network architecture by composing differentiable
operators and (2) supplies training data. The package then automatically computes the gradient of the error
on the training data via recursive application of the chain rule. At this point, the user must become involved
again by (3) selecting one of numerous optimisation algorithms and (4) manually tuning its hyperparameters:
in particular, the initial learning rate and the learning rate decay schedule (Goodfellow et al., 2016).
But manually tuning hyperparameters is irksome. An abundance of hyperparameters makes it difficult to
rank the performance of different deep learning algorithms (Lucic et al., 2017; Schmidt et al., 2021) and
difficult to reproduce results in the literature (Henderson et al., 2018). Hyperparameters confound our efforts
to build a scientific understanding of generalisation in deep learning (Jiang et al., 2020; Farhang et al., 2022).
And, when training neural networks at the largest scale, in pursuit of stronger forms of artificial intelligence,
hyperparameter grid search can rack up millions of dollars in compute costs (Sharir et al., 2020).
Are hyperparameters just a fact of life? The thesis of this paper is that no: they are not. Deep learning
involves fitting a known function to known data via minimising a known objective. If we could characterise
these components both individually and in how they interact, then—in principle—there should be no leftover
degrees of freedom to be tuned (Orabona & Cutkosky, 2020). Taking this idea and running with it leads
to automatic gradient descent (AGD): a neural network optimiser without any hyperparameters. AGD is
complementary to automatic differentiation and could help to automate general machine learning workflows.
Two existing tools are central to our derivation, and it is their novel combination that presents the main
theoretical contribution of this paper. First, a classic tool from convex analysis known as the Bregman
divergence (Bregman, 1967; Dhillon & Tropp, 2008) is used to characterise how the neural network interacts
with the loss function. And second, a tool called deep relative trust (Bernstein et al., 2020) is used to
characterise the highly non-linear interaction between the weights and the network output. With these tools
2
Table 1: Comparing practical optimisers. Adam and momentum-SGD employ running estimates of gradient
statistics and thereby use more memory than AGD. In addition, Adam and SGD do not provide guidance on
scaling hyperparameters with network architecture, although muP fixes this for the case of width scaling.
in hand, we can apply the majorise-minimise meta-algorithm (Lange, 2016) to derive an optimiser explicitly
tailored to deep network objective functions. To summarise, the derivation of AGD follows three main steps:
Step 1: Functional expansion. We use a Bregman divergence to express the linearisation error of the objective
function Lpwq in terms of the functional perturbation ∆f to the network f .
Step 2: Architectural perturbation bounds. We use deep relative trust to relate the size and structure of the
weight perturbation ∆w to the size of the induced functional perturbation ∆f .
Step 3: Majorise-minimise. We substitute deep relative trust into the Bregman divergence to obtain an
explicitly architecture-dependent majorisation. Minimising with respect to ∆w yields an optimise
1.2 Preliminaries
Given a vector v in Rn, we will need to measure its size in three different ways:
Definition 1 (Manhattan norm) The Manhattan norm } ¨ }1 of a vector v is defined by }v}1 :“ ř
i |vi|.
Definition 2 (Euclidean norm) The Euclidean norm } ¨ }2 of a vector v is defined by }v}2 :“ ař
i v2
i .
Definition 3 (Infinity norm) The infinity norm } ¨ }8 of a vector v is defined by }v}8 :“ maxi |vi|.
For a matrix M in Rmˆn, the reader should be aware that it has a singular value decomposition:
Fact 1 (SVD) Every matrix M in Rmˆn admits a singular value decomposition (SVD) of the form M “
řminpm,nq
i“1 σipM q ¨ uivJ
i where the left singular vectors tuiu are orthonormal vectors in Rm, the right singular
vectors tviu are orthonormal vectors in Rm and the singular values tσipM qu are non-negative scalars.
The singular value decomposition allows us to measure the size of a matrix in two different ways:
Definition 4 (Frobenius norm) The Frobenius norm } ¨ }F of a matrix M is given by }M }F :“ ař
i σipM q2.
Definition 5 (Operator norm) The operator norm } ¨ }˚ of a matrix M is given by }M }˚ :“ maxi σipM q.
While the operator norm }M }˚ reports the largest singular value, the quantity }M }F {aminpm, nq reports
the root mean square singular value. Finally, we will need to understand two aspects of matrix conditioning:
Definition 6 (Rank) The rank of a matrix counts the number of non-zero singular values.
Definition 7 (Stable rank) The stable rank of a matrix M is defined by rankstable M :“ }M }2
F {}M }2
˚.
The stable rank provides an approximation to the rank that ignores the presence of very small singular values.
Let us consider the extremes. An orthogonal matrix O P Rmˆn has both full rank and full stable rank:
rank O “ rankstable O “ minpm, nq. A rank-one matrix P has unit stable rank and satisfies }P }˚ “ }P }F .
2 Majorise-Minimise for Generic Learning Problems
This section develops a framework for applying the majorise-minimise meta-algorithm to generic optimisation
problems in machine learning. In particular, the novel technique of functional expansion is introduced.
Section 3 will apply this technique to deep neural networks. All proofs are supplied in Appendix A.
Given a machine learning model and a set of training data, our objective is to minimise the error of the
model, averaged over the training data. Formally, we would like to minimise the following function:
Definition 8 (Composite objective) Consider a machine learning model f that maps an input x and a weight
vector w to output f px; wq. Given data S and a convex loss function `, the objective Lpwq is defined by:
Lpwq :“ 1
|S|
ÿ
px,yqPS
`pf px; wq, yq.
We refer to this objective as composite since the loss function ` is composed with a machine learning model
f . While the loss function itself is convex, the overall composite is often non-convex due to the non-linear
machine learning model. Common convex loss functions include the square loss and the cross-entropy loss:
Example 1 (Square loss) The square loss is defined by: `pf px; wq, yq :“ 1
2dL }f px; wq ´ y}2
2.
Example 2 (Xent loss) The cross-entropy (xent) loss is defined by: `pf pxq, yq :“ ´ logrsoftmaxpf pxqqsJy,
where the softmax function is defined by softmaxpf pxqq :“ exp f pxq{}exp f pxq}1.
2.1 Decomposition of linearisation error
First-order optimisers leverage the linearisation of the objective at the current iterate. To design such
methods, we must understand the realm of validity of this linearisation. To that end, we derive a very general
decomposition of the linearisation error of a machine learning system. The result is stated in terms of a
perturbation hierarchy. In particular, perturbing the weight vector of a machine learning model w Ñ w ` ∆w
induces perturbations to the model output f Ñ f ` ∆f , to the loss on individual data samples ` Ñ ` ` ∆`
and, at last, to the overall objective function L Ñ L ` ∆L. Formally, a weight perturbation ∆w induces:
∆f pxq :“ f px; w ` ∆wq ´ f px; wq; (functional perturbation)
∆`pf pxq, yq :“ `pf pxq ` ∆f pxq, yq ´ `pf pxq, yq; (loss perturbation)
∆Lpwq :“ 1
|S|
ř
px,yqPS ∆`pf pxq, yq. (objective perturbation)
We have adopted a compact notation where the dependence of f px; wq on w is at times suppressed. The
perturbation hierarchies of a generic machine learning model and a deep neural network are visualised in
Figures 2 and 3, respectively. The linearisation error of the objective perturbation ∆L decomposes as:
5

**Response:**
This paper discusses the issue of manually tuning hyperparameters in deep learning and proposes a solution called automatic gradient descent (AGD). The authors argue that hyperparameters are not necessary and can be eliminated by characterizing the components of deep learning and their interactions. They introduce two tools, Bregman divergence and deep relative trust, and use them to derive an optimiser explicitly tailored to deep network objective functions. The paper presents three main steps in the derivation of AGD: functional expansion, architectural perturbation bounds, and majorise-minimise. The authors also provide preliminaries on vector and matrix measurements and introduce the concept of stable rank. Finally, they discuss the decomposition of linearisation error in machine learning systems.

<details><summary>Metadata</summary>

- Duration: 4136 ms
- Datetime: 2023-10-05T16:13:33.345219
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

