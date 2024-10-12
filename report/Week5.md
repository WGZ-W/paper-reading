

# Week5

This week I have read a survey about continual learning's basic knowledge.

[1]. Wang, L., Zhang, X., Su, H., & Zhu, J. (2023). A Comprehensive Survey of Continual Learning: Theory, Method and Application. IEEE Transactions on Pattern Analysis and Machine Intelligence, 46, 5362-5383.

## 1. Related concept
**Continual learning** is to learn a sequence of contents one by one and behave as if they were observed simultaneously. Continual learning is also referred to as **incremental learning** or **lifelong learning** in much of the literature, without a strict distinction.

## 2. The problems
### 2.1 Catastrophic Forgetting
Catastrophic forgetting is when model adapts to a new distribution generally results in a largely reduced ability to capture the old ones.  
Catastrophic forgetting is an inherent characteristic of neural network models, and in fact cannot be completely solved by using neural networks. It can be simply understood that their information is recorded in the network parameters, and after learning a new task, the previous parameters will be overwritten. However, we can still mitigate this problem by introducing anti-forgetting mechanisms to keep the model as effective as it was on the old task. The design of various anti-forgetting mechanisms is also the main goal of continuous learning.

### 2.2  Stability-Plasticity trade-off 
This dilemma is a facet of the trade-off between
learning plasticity and memory stability: an excess of the former interferes with the latter, and vice versa. 

### 2.3 Generalizability
Beyond simply balancing the “proportions” of the  stability-plasticity aspects, a desirable solution for continual learning should obtain
strong generalizability to accommodate distribution differences within and between tasks.

### 2.4 Backward Transfer and Forward Transfer
Backward Transfer(BWT) evaluates the average influence of learning the k-th task on all old tasks.
Forward Transfer(FWT) evaluates the average influence of all old tasks on the current k-th task.

## 3. Task: Classification
Current advances mainly focus on visual classification.
According to the division of incremental batches and the availability of task identities, we describe continual learning scenarios as follows:
![typical-scenario](./typical-scenario.png)

## 4. Methods
- Regularization-Based Approach
- Replay-Based Approach
- Optimization-Based Approach
- Representation-Based Approach
- Architecture-Based Approach