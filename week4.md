# Week 4
This week I have read a paper about navigation for UAVs.

[1]. Liu, S., Zhang, H., Qi, Y., Wang, P., Zhang, Y., & Wu, Q. (2023). AerialVLN: Vision-and-Language Navigation for UAVs. 2023 IEEE/CVF International Conference on Computer Vision (ICCV), 15338-15348.

## Existing tasks introduce
There are a bunch of vision-and-language navigation tasks, such as R2R, RxR, Touch-Down..., however, all these VLN tasks are designed for ground-based agents. This paper introduce a new task for the exploration of vision-and-language navigation in the sky.

## Complexity
First of all, unmanned aerial vehicles(UAVs) is becoming increasingly popular recently. Navigation in the sky is significantly different from that on the ground in several aspects. **First**, UAVs has a large action space. **Second**, the environments of UAVs are much bigger and more complex. **Third**, UAVs has a much longer path than ground VLNs. **Fourth**, intelligent agents must learn to avoid getting stuck on objects in 3D space. 

## The AerialVLN task
The agent is placed in an initial pose, and the agent need to fly to the destination by following a given natural language instruction and its first-person view visual perceptions provided by the simulator.

## Dataset
The path were made by experienced multirotor manipulators. And the language instructions were through Amazon Mechanical Turk to collect.  
Then divide dataset into the train, val_seen, val_unseen, and test splits. The word "seen" means the visual environment that have been seen in the train split.

## Baseline
Cross-Modal Attention(CMA) is a classical baseline model for VLN tasks. The CMA is based on a bi-directional LSTM and divides the whole process into two parts.
![Cross-Modal-Attention](./images/cross-modal-attention.png)

## Results

CMA achieve success rate 1.0% ~ 1.6% on unseen splits of the full dataset(Val_Unseen and Test_Unseen).The success rate is still rather low compared to human performance(~80%).
