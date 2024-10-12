

# Week7

This week I read the survey about continual learning's methods.

[1]. Wang, L., Zhang, X., Su, H., & Zhu, J. (2023). A Comprehensive Survey of Continual Learning: Theory, Method and Application. IEEE Transactions on Pattern Analysis and Machine Intelligence, 46, 5362-5383.

## Regularization-Based Approach
This direction is characterized by adding explicit regularization terms to balance the old and new tasks, which usually requires storing a frozen copy of the old model for reference.Depending on the target of regularization, such methods can be divided into two sub-directions.

![regularization-based](../images/continual-learning/regularization-based-approach.png)

- The first is **weight regularization**, which selectively regularizes the variation of network parameters. A typical implementation is to add a quadratic penalty in loss function that penalizes the variation of each parameter depending on its contribution or “importance” to performing the old tasks.
- The second is **function regularization**, which targets the intermediate or final output of the prediction function. This strategy typically employs the previously-learned model as the teacher and the currently-trained model as the student,while implementing knowledge distillation (KD) to mitigate catastrophic forgetting.

## Replay-Based Approach
It group the methods for approximating and recovering old data distributions into this category. Depending on the content of replay, these methods can be further divided into three sub-directions.

![replay-based](../images/continual-learning/replay-based.png)

- The first is **experience replay**, which typically stores a few old training samples within a small memory buffer.
- The second is **generative replay** or pseudo-rehearsal, which usually requires training an additional generative model to replay generated data.
- The third is **feature replay**, which maintains feature-level rather than data-level distributions enjoys numerous benefits in terms of efficiency and privacy.


## Optimization-Based Approach
Continual learning can be achieved by not only adding additional terms to the loss function, but also explicitly designing and manipulating the optimization programs.

![optimization-based](../images/continual-learning/optimization-based.png)

- A typical idea is to perform **gradient projection**.
- Another attractive idea is **meta-learning** or learning-to learn for continual learning, which attempts to obtain a
data-driven inductive bias for various scenarios, rather than designing it manually.
- Besides, some other works refine the optimization process from a loss landscape perspective.


## Representation-Based Approach


## Architecture-Based Approach