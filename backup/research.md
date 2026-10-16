

# Research

## 主要问题
> 主动推理与记忆压缩问题

> 如何高效利用历史信息？（记忆压缩）

heatmap，注意力机制

## 记忆机制

| Name | Public | Methods | Note |
| - | - | - | - |
|[OctMem-Agent]()|CVPR 2026|八叉树，体素||
|[OpenFly](https://arxiv.org/abs/2502.18041)|ICLR 2026|动作关键帧||
|[AerialVLA](https://ojs.aaai.org/index.php/AAAI/article/view/38878)|AAAI 2026|时空融合历史信息，全局地图，时序对应在全局对应|
|[NavAgent](https://arxiv.org/abs/2411.08579)||动态增长的场景拓扑地图，||
|[AerialVLN](https://arxiv.org/abs/2308.06735)|ICCV 2023|
|[LongFly](https://arxiv.org/abs/2512.22010)||槽压缩，固定槽位||
|[NaVid](https://arxiv.org/abs/2402.15852)|RSS 2024|两种 Token ，将历史帧作为视频处理||
|[NaVILA](https://arxiv.org/abs/2412.04453)|RSS 2025|间隔采样历史帧||
|[Uni-NaVid](https://arxiv.org/abs/2412.06224)|RSS 2025|长期记忆 + 短期记忆，不同的压缩比|
|[GA-VLN](https://arxiv.org/abs/2605.22036)|CVPR 2026|网格图|
|[CityNavAgent](https://arxiv.org/abs/2505.05622)|||
|[STMR](https://arxiv.org/abs/2410.08500v3)|
|[GVSMC](https://arxiv.org/abs/2503.11091)||BEV|


## UAV VLN（Visual Language Navigation）

- 输入：当前帧，历史帧，语言指令，历史动作？
- 唯一指令，低空，第一人称视角

- 构建图，或者节点，

- 对历史信息的使用方式。（动作，历史帧）

- 时序特征？空间特征？

### 记忆机制

- 拓扑图
- 鸟瞰图 BEV
- 全局地图
- 结构化记忆（长期记忆+短期记忆）


## UAV VDN（Visual Dialogue Navigation）

- 视觉对话导航，多轮对话，消除模糊
- 高空自上而下视角，

- 时序和空间特征融合

- 外加何时进行提问。

- 提问什么问题？


## UAV VLN (Object Search) (Object Navigation)
