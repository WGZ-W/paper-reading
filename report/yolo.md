

# YOLO系列目标检测算法综述

- [YOLO系列目标检测算法综述](#yolo系列目标检测算法综述)
  - [YOLO算法系列横向对比](#yolo算法系列横向对比)
    - [yolo网络结构比较](#yolo网络结构比较)
    - [锚框设置对比](#锚框设置对比)
    - [损失函数设计](#损失函数设计)
  - [YOLO算法数据集及评价指标](#yolo算法数据集及评价指标)
  - [难点与展望](#难点与展望)


目标检测是计算机视觉领域的一项关键任务，其核心目标是从图像或视频序列中准确地确定物体的存在、种类及其空间位置。目标检测任务既包含分类问题，即将物体划分到预定义的类别中，又包含回归问题，即定位物体的准确位置。
## YOLO算法系列横向对比
新的激活函数和注意力机制的发展使基于YOLO算法的目标检测精度大大提高。
### yolo网络结构比较
YOLO算法流程是，将图片划分为网格，每个网格预测生成两个长宽比不同的边界框，每个边界框有 5 个参数。然后根据阈值去除置信度比较低的边界框，最后用非极大值抑制算法去除重合的边界框，得到最终的预测结果。
- 骨干网络主要作用是特征提取，它的改进部分，主要为设计网络结构降低计算复杂度同时提升算法精度、使用新的激活函数防止过拟合。
- 颈部层主要作用是汇聚和融合多层特征，
- 头部层是用来进行目标检测的部分。主要是加强对小目标的检测，将分类任务和回归任务分离。
### 锚框设置对比
从k-means聚类算法代替手工设计获得锚框的先验尺寸，到固定3种不同尺度、3种不同宽高比，再到无锚框设计。
### 损失函数设计
基本分为预测框坐标损失、置信度损失以及类别损失。
## YOLO算法数据集及评价指标
DOTA主要针对无人机领域的目标识别检测任务。
YOLO算法评价指标主要使用：
- FPS 度量算法速度。
- AP 度量算法精度。
## 难点与展望
难点：
- 小目标的定位精度不足
- 算法正负样本不均衡
- 算法训练需要大量的图片保证模型的泛化能力
展望：  
- 多任务学习，将目标检测、语义分割等多个视觉任务集成到同一模型上训练，提高模型对多个任务的综合理解能力和泛化能力。
- 边缘计算，使用剪枝技术减少冗余参数，使用模型蒸馏技术，训练简化的网络模型。
- 多模态结合，将语言和声音等融入YOLO算法，设计新的网络，通过注意力等融合机制，使模型全面感知周围环境。