# Week 13

[1]. L. Chen, P. Wu, K. Chitta, B. Jaeger, A. Geiger and H. Li, "End-to-End Autonomous Driving: Challenges and Frontiers," in IEEE Transactions on Pattern Analysis and Machine Intelligence, vol. 46, no. 12, pp. 10164-10183, Dec. 2024, doi: 10.1109/TPAMI.2024.3435937.


## *1* Introduction
End-to-end systems, in comparison to modular pipelines, benefit from joint feature optimization for perception and planning. This field has flourished due to the availability of large-scale datasets closed-loop evaluation, and the increasing need for autonomous driving algorithms to perform effectively in challenging scenarios.  
The classical pipeline may not be aligned with a unified target. 

## *2* Methods
### Imitation Learning
Imitation Learning trains an agent to learn the policy by imitating the behavior of an expert.

#### Behavior Cloning
In BC, matching the agent's policy with the expert's is accomplished by minimizing planning loss as supervised learning over the collected dataset.

#### Inverse Optimal Control
Traditional IOC algorithms learn an unknown reward function from expert demonstrations, where the expert’s reward function can be represented as a linear combination
of features.   
Recently, several works propose
optimizing a cost volume or cost function with auxiliary perceptual tasks.

### Reinforcement Learning
RL requires significantly more
data to train than IL. Meeting these requirements in the real world presents
great challenges. Therefore, almost all papers that use RL in
driving have only investigated the technique in simulation.

## *3* BenchMarking
### Real-world Evaluation
However,
such academic ventures have not been widely employed for
end-to-end systems due to a lack of data and vehicles. In
contrast, industries with the resources to deploy fleets of
driverless vehicles could rely on real-world evaluation to
benchmark improvements in their algorithms.

### Online/Closed-loop Simulation
Closed-loop evaluation involves building a simulated
 environment that closely mimics a real-world driving en
vironment. The evaluation entails deploying the driving
 system in simulation and measuring its performance. The
 system has to navigate safely through traffic while progress
ing toward a designated goal location.
### Offline/Open-loop Evaluation
Open-loop evaluation mainly assesses a system's performance against pre-recorded expert driving behavior.

## *4* Challenges
- Various sensors possess distinct perspectives, data distributions, and huge price gaps, thereby posing challenges in
 effectively designing the sensory layout and fusing them to
 complement each other for autonomous driving.
- Language as Input
- ......

## *5* Future Trends
- Zero-shot and Few-shot Learning
- Modular End-to-end Planning
- Data Engine
- Foundation Model