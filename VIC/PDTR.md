


## PDTR
[1]. Rui Li, Yishu Liu, Huafeng Li, Jinxing Li, and Guangming Lu. 2024. Prototype-Guided Dual-Transformer Reasoning for Video Individual Counting.(MM '24).10258–10267.


此文使用 Transformer 将两张相邻的帧中的相似部分计算出来，然后对每张图求各自私有的部分，从而预测出流入和流出的人数。

## 内容大概
Multi-receptive field feature fusion module 接受不同规模的特征，通过特征对齐金字塔进行对其，然后经过特征融合编码器生成特征 *F*
DynamicPrototypeGeneration module 通过对迭代的聚集相似的信息，生成 *X*
PrototypeCross-guidedDecoder module 使用 transformer 对 *X* 和 *F* 进行操作，生成共享特征 *Z*
最后，使用Privacy-decouplingModule 对 F 和 Z 进行操作，求出帧中私有的特征，然后根据特征预测出坐标。


## 方法对比

DRNet 对每个行人都生成一个描述符，用作在推理阶段进行匹配，DRNet 使用特征匹配推理，对于每个行人都进行各自特征匹配。

CGNet 使用两种标签，用于表示流入和流出，然后使用群水平匹配方法，将行人分成四个集合，进行群匹配。

PDTR 使用标签，是否在此帧中，然后直接利用 transformer 生成相似特征，则每帧中私有的特征就可以推理出来。

整体来看，都是对特征进行匹配，DRNet 是对于每个个体进行匹配，后两种都是进行群匹配。再者，前两种都是对数据进行一些预处理，然后使用匹配算法，PDTR则是端到端对的方式预测。

另外有一点，对于在 DRNet 中提出的一个出去重新进入的行人的问题，DRNet 认为这类人数较少，采用直接忽略这类行人的方法，CGNet 则使用 Memory-based Count Predictor 进行预测，提出使用一个因素 TTL 对行人进行更新。至于 PDTR，由于都是对相邻两帧进行直接处理，也并未考虑这个问题。

 






