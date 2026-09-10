# 视觉—语言导航（VLN）研究趋势综述

> 更新时间：2026-09-10  
> 范围：以 2023–2026 年通用/地面 VLN 与 UAV-VLN 为重点；会议论文与仍处于 arXiv 阶段的工作会明确区分。本文关注研究方向，不追求穷举模型或复述排行榜。

## 1. 结论先行

视觉—语言导航正在从一个相对封闭的“根据自然语言在离散导航图上选下一个节点”的任务，演变为更完整的具身智能问题：智能体需要在未知、动态且连续的三维环境中，把视觉与语言理解、空间记忆、长期规划、运动控制、安全约束和人机交互组成闭环。

当前最明显的研究趋势可以概括为：

1. **专用策略模型向 VLM/MLLM/VLA 基础模型迁移**，目标从单任务最优变为跨任务、跨平台的通用导航能力。
2. **纯端到端反应式决策重新吸收显式地图、场景图和层次化规划**，形成“语义推理 + 几何执行”的混合架构。
3. **长时程记忆成为关键瓶颈**，研究重点从“保留全部历史”转向任务相关检索、压缩、分层表达与失败恢复。
4. **评测从静态、短路径、离散动作走向开放世界、动态人群、多轮交互和连续控制**。
5. **数据与仿真平台持续扩张**，但研究焦点已从单纯扩大样本量转向数据真实性、任务多样性和物理可执行性。
6. **世界模型和生成式预测开始进入导航决策**，即先预测/想象未来观测或潜在状态，再据此规划动作。
7. **真实部署的安全、时延和算力约束进入模型设计本身**，特别是在无人机和移动机器人场景。

总体判断是：**VLN 的前沿正在从“跨模态匹配”转向“空间智能系统工程”**。其中，VLM 提供开放词汇语义与推理能力，显式空间表征提供几何可靠性，低层控制器保证可执行性；短期内，三者协作的层次化系统比完全统一的端到端模型更接近真实部署。

## 2. 研究范式的演进

| 阶段 | 主要设定 | 代表性能力 | 主要局限 |
|---|---|---|---|
| 早期 VLN | 室内、静态、离散导航图、逐步指令 | 视觉—语言对齐、动作分类 | 依赖预定义连通图，泛化与实机能力弱 |
| 预训练与数据扩展 | 更大规模场景和轨迹、跨任务预训练 | 未见场景泛化、多任务迁移 | 数据仍主要来自仿真，动作和物理约束较弱 |
| LLM/VLM 导航 | 零样本推理、自然语言计划、视频历史 | 常识、指令分解、可解释推理 | 三维空间推理、稳定性、时延和幻觉仍突出 |
| VLA 与开放世界 | 连续动作、跨任务统一、实机闭环 | 从观测和指令直接产生可执行动作 | 数据昂贵，安全性与跨本体迁移尚未解决 |
| 世界模型与具身智能体 | 预测未来、主动感知、长期记忆、自我纠错 | 规划—执行闭环、失败恢复 | 尚处早期，评测标准与可复现性不足 |

这一演进也改变了研究问题：过去的核心是“当前视角与指令是否匹配”，现在则是“智能体应主动观察什么、记住什么、如何判断进度、下一段轨迹在物理上是否安全”。

## 3. 当前七条主要趋势

### 3.1 从专用 VLN 模型走向导航基础模型与 VLA

LLM/VLM 首先以高层推理器进入 VLN。[NavGPT](https://arxiv.org/abs/2305.16986) 展示了利用 LLM 进行零样本子目标分解、地标识别和进度跟踪的可能性；[NavGPT-2（ECCV 2024）](https://arxiv.org/abs/2407.12366) 进一步把视觉表征对齐到冻结语言模型，并与导航策略结合，缩小大模型导航与专用模型之间的性能差距。

随后，研究从“把视觉转成文字再让 LLM 选动作”转向原生视频与动作建模。[NaVid（RSS 2024）](https://www.roboticsproceedings.org/rss20/p079.pdf) 仅使用单目 RGB 视频流输出下一步动作，不依赖地图、里程计或深度；[Uni-NaVid（RSS 2025）](https://www.roboticsproceedings.org/rss21/p013.html) 则统一了指令跟随、目标搜索、问答和人员跟随等多类导航任务。对于腿式机器人，[NaVILA（RSS 2025）](https://navila-bot.github.io/) 采用“高层 VLA 命令 + 实时低层运动策略”的两级结构。

这条路线的实质是：

- 输入由单帧/全景图扩展为视频、历史轨迹与多传感器信息；
- 输出由离散候选点扩展为速度、位姿或轨迹等连续动作；
- 目标由单一 benchmark 最优扩展为多任务统一和跨本体迁移；
- 训练由监督模仿学习扩展到多任务预训练、指令微调、强化学习和测试时适应。

但“统一”不等于完全端到端。2026 年一项系统性实机评估报告，在其测试配置中，单体 RGB 方法的成功率从仿真的 61% 降到实机的 22%，而层次化系统实机达到 51%，说明模块化语义规划与可靠低层控制目前仍有明显现实优势（结果只适用于该论文的测试平台与场景）[[Wang et al., 2026, arXiv]](https://arxiv.org/abs/2607.09792)。

### 3.2 显式空间表征回归：地图、图记忆与 3D token

大模型擅长语义与常识，但并不天然具备精确、持续一致的三维几何认知。因此，前沿方法普遍不再把“是否使用地图”看成二选一，而是探索**什么样的地图最适合被 VLM 查询和推理**。

典型做法包括拓扑记忆、语义场景图、占据/可通行地图、对象—区域—房间层次图，以及将 RGB-D 历史压缩成 3D token。[Dynam3D（NeurIPS 2025）](https://proceedings.neurips.cc/paper_files/paper/2025/hash/e1a1847e39a7b79b41199176b152f0e6-Abstract-Conference.html) 用动态分层 3D token 增强视频 VLM；[HSGM（CVPR 2026）](https://openaccess.thecvf.com/content/CVPR2026/html/Li_Bridging_the_2D-3D_Gap_A_Hierarchical_Semantic-Geometric_Map_for_Vision_CVPR_2026_paper.html) 把几何、语义和决策信息组织为层次化俯视地图，由 VLM 选择高层 waypoint、经典规划器执行无碰撞运动。

这反映出一个重要共识：**语义模型负责“去哪里、为什么”，几何模块负责“能否到达、怎样安全到达”**。纯语言化场景描述会丢失距离、尺度和遮挡信息；纯几何 SLAM 又难以理解开放词汇目标与模糊指令。语义—几何耦合将长期是 VLN 的核心架构问题。

### 3.3 长时程导航：从无限历史到选择性、分层和可恢复记忆

短路径中，简单拼接若干历史帧尚可工作；当任务延伸到数百步和多个子任务时，会出现上下文膨胀、重复探索、进度遗忘和误差累积。[LHPR-VLN（CVPR 2025）](https://openaccess.thecvf.com/content/CVPR2025/html/Song_Towards_Long-Horizon_Vision-Language_Navigation_Platform_Benchmark_and_Method_CVPR_2025_paper.html) 包含 3,260 个任务，平均约 150 个动作步，并引入针对子任务连续完成情况的指标，体现评测正在从“最终是否到达”转向“整个任务链是否一致完成”。

方法上有四种趋向：

- **短期/长期双记忆**：当前局部细节与长期关键事件分开存储；
- **选择性记忆与检索**：只保存动作突变、地标出现、失败或高不确定性片段；
- **结构化记忆**：把视频历史转换为拓扑图、语义图或几何地图，而非原始 token 堆叠；
- **失败恢复**：显式判断偏航、循环、错过目标和错误停止，再回退或重规划。

[COSMO（ICCV 2025）](https://openaccess.thecvf.com/content/ICCV2025/html/Zhang_COSMO_Combination_of_Selective_Memorization_for_Low-cost_Vision-and-Language_Navigation_ICCV_2025_paper.html) 把选择性记忆与低成本建模结合；[ProFocus（CVPR 2026）](https://openaccess.thecvf.com/content/CVPR2026/html/Xue_ProFocus_Proactive_Perception_and_Focused_Reasoning_in_Vision-and-Language_Navigation_CVPR_2026_paper.html) 则只对高价值历史 waypoint 进行重点推理。研究重点已从“让模型看到更多”转向“让模型只看到决策真正需要的信息”。

### 3.4 从封闭集指令跟随走向开放世界、主动感知与交互

真实用户通常不会给出完整、无歧义的逐步路线，而可能只说“去找红色维修车”“带我到适合轮椅通行的出口”。因此，任务正从固定词表和单轮指令扩展到：

- 开放词汇 ObjectNav 与目标描述；
- 未见环境和未见指令组合的零样本导航；
- 主动转头、回看、搜索和验证，而非被动接受固定视野；
- 在信息不足时向人提问，利用反馈进行测试时更新；
- 根据机器人尺寸、爬楼、开门等本体能力判断路线可行性。

[TANGO（CVPR 2025）](https://openaccess.thecvf.com/content/CVPR2025/html/Ziliotto_TANGO_Training-free_Embodied_AI_Agents_for_Open-world_Tasks_CVPR_2025_paper.html) 用 LLM 组合导航与探索原语，在多种开放世界任务中实现免训练推理；[ATENA（NeurIPS 2025）](https://proceedings.neurips.cc/paper_files/paper/2025/hash/3f510f82323c1293ae3e343893dd77b1-Abstract-Conference.html) 根据不确定结果主动获取人类反馈；[CapNav（CVPR 2026）](https://openaccess.thecvf.com/content/CVPR2026/html/Su_CapNav_Benchmarking_Vision_Language_Models_on_Capability-conditioned_Indoor_Navigation_CVPR_2026_paper.html) 进一步显示，当行动能力约束变严格时，现有 VLM 的导航判断会明显退化。

由此，VLN 正逐渐从“语言条件分类”转变为带有**信息获取、可行性判断和不确定性管理**的交互式智能体问题。

### 3.5 Benchmark 从静态离散仿真走向动态、连续与真实部署

经典 R2R 等基准仍是重要的可比性锚点，但越来越不足以代表真实机器人。新的评测维度包括：

- 连续空间而非预定义导航节点；
- 动态行人、遮挡和环境变化；
- 长任务链与多阶段目标；
- 多语言、对话式或不完整指令；
- 不同机器人本体及其运动约束；
- 真实世界闭环、碰撞、安全裕度、能耗、时延和恢复能力。

[HA-VLN（NeurIPS 2024 Datasets and Benchmarks）](https://proceedings.neurips.cc/paper_files/paper/2024/hash/d8087deaf34bb07ddd41c65f8a9fe9b5-Abstract-Datasets_and_Benchmarks_Track.html) 将动态人类活动纳入导航环境；[NavBench（NeurIPS 2025）](https://proceedings.neurips.cc/paper_files/paper/2025/hash/8932bbe603280f51d425e2781cd6ea6e-Abstract-Conference.html) 专门探测 MLLM 的零样本具身导航能力。趋势是用多维指标替代单一 SR/SPL，例如任务分段成功率、碰撞率、轨迹平滑性、语言一致性、询问成本、推理时延和失败恢复率。

### 3.6 数据规模化之后：自动生成、质量控制与真实数据混合

[ScaleVLN（ICCV 2023）](https://openaccess.thecvf.com/content/ICCV2023/papers/Wang_Scaling_Data_Generation_in_Vision-and-Language_Navigation_ICCV_2023_paper.pdf) 使用 1,200 多个可遍历场景生成 490 万条指令—轨迹对，说明场景多样性和具身域内数据规模可以显著改善未见环境泛化。近期平台进一步把自动场景构建、轨迹采样、指令生成、质量筛选与多引擎渲染连成工具链。

但下一阶段的数据问题不是简单的“更多”：

- 合成指令是否真正具有人类表达的歧义、多样性和纠错行为；
- 视觉逼真度之外，动力学、传感器噪声和交互对象是否真实；
- 训练轨迹是否覆盖失败、恢复、犹豫和安全边界等长尾状态；
- 大模型生成的标注是否引入模板偏差、幻觉或测试集泄漏；
- 能否混合仿真、互联网视频、遥操作轨迹和少量实机数据，并保持动作空间一致。

因此，高价值方向是**可验证的数据生成闭环**：自动生成任务，经可达性/动力学检查、模型难度筛选和少量人工审查后再进入训练，而不是直接堆积语言模型合成样本。

### 3.7 世界模型、安全约束与实时部署成为新前沿

反应式策略根据当前观测直接出动作，容易在遮挡或局部最优中失败。世界模型路线则学习“采取某动作后会看到什么”，以未来观测或潜在状态辅助规划。[Do Visual Imaginations Improve VLN Agents?（CVPR 2025）](https://openaccess.thecvf.com/content/CVPR2025/html/Perincherry_Do_Visual_Imaginations_Improve_Vision-and-Language_Navigation_Agents_CVPR_2025_paper.html) 用文本到图像模型生成指令中子目标的视觉想象，并报告了小幅但一致的导航提升。到 UAV 场景，[ImagineUAV（2026，arXiv）](https://arxiv.org/abs/2606.01205) 进一步用潜在视频扩散模型生成指令条件下的未来观测，再恢复 6-DoF 运动并结合运动学规划。

与此同时，真实机器人不能让大模型以低频率、不可预测地直接接管每个控制周期。工程上正在形成两种方案：

- **异步快慢系统**：低频 VLM 负责语义目标、进度和纠错，高频轻量策略/规划器持续执行；
- **安全过滤层**：对大模型建议的目标点或轨迹进行深度、碰撞和控制屏障函数等几何验证。

这使评价标准从“能否到达”扩展到“能否在给定算力、频率与安全约束下持续到达”。

## 4. UAV-VLN：增长最快的专项方向

空中 VLN 放大了地面 VLN 的所有难点：场景尺度更大、路径更长、视角和目标尺度变化更剧烈，动作空间具有高度、俯仰和侧移等额外自由度，而且碰撞后果更严重。

[AerialVLN（ICCV 2023）](https://openaccess.thecvf.com/content/ICCV2023/html/Liu_AerialVLN_Vision-and-Language_Navigation_for_UAVs_ICCV_2023_paper.html) 建立了室外城市级 UAV-VLN 任务与连续模拟环境；[OpenUAV/TravelUAV（ICLR 2025）](https://proceedings.iclr.cc/paper_files/paper/2025/file/15ce8e7afe5ee95bad56e3b9be28d3d1-Paper-Conference.pdf) 将现实飞行动力学、6-DoF 轨迹和目标导向指令纳入闭环；[OpenFly（2026，arXiv）](https://arxiv.org/abs/2502.18041) 则继续推进多引擎工具链和大规模空中 VLN 基准。

UAV-VLN 当前有五条鲜明路线：

1. **从路线复现到自主搜索。** [UAV-ON（ACM MM 2025）](https://arxiv.org/abs/2508.00288) 用高层对象描述替代详细逐步指令，要求无人机在开放世界中主动探索。
2. **方向、尺度与三维空间推理。** [LookasideVLN（CVPR 2026）](https://openaccess.thecvf.com/content/CVPR2026/html/Ning_LookasideVLN_Direction-Aware_Aerial_Vision-and-Language_Navigation_CVPR_2026_paper.html) 显式建模指令中的方向线索和地标关系，以更低成本改善空中空间推理。
3. **面向大场景的分层 3D 记忆。** [OctMem-Agent（CVPR 2026）](https://openaccess.thecvf.com/content/CVPR2026/html/Zhou_Memory-Augmented_Scene_Understanding_and_Exploration_for_Open-World_Aerial_Object-Goal_Navigation_CVPR_2026_paper.html) 用自适应八叉树聚合 RGB-D 历史；[APEX（CVPR 2026）](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_APEX_A_Decoupled_Memory-based_Explorer_for_Asynchronous_Aerial_Object_Goal_CVPR_2026_paper.html) 将三维语义地图、RL 控制和开放词汇目标定位异步组合，以降低 VLM 时延影响。
4. **长时程连续 6-DoF 控制。** [FLIGHT（2026，arXiv）](https://arxiv.org/abs/2606.06836) 将多阶段语义指令与稠密 6-DoF 轨迹结合，表明未来基准会同时要求高层推理与平滑、物理可行的飞行控制。
5. **全机载、实时与安全。** [OnFly（2026，arXiv）](https://arxiv.org/abs/2603.10682) 将高频目标生成、低频进度监控、语义—几何校验和滚动规划组合起来，并报告了全机载实飞验证。

UAV-VLN 的下一步不会只是把地面 VLN 模型换到航拍图上，而是形成“开放词汇目标理解—全局探索—三维记忆—动力学规划—安全控制”的专用技术栈。

## 5. 尚未解决的核心问题

| 问题 | 当前症结 | 值得关注的研究方向 |
|---|---|---|
| 三维空间 grounding | VLM 对左右、远近、遮挡、尺度和朝向不稳定 | 语义—几何联合预训练、可验证空间推理、3D token/场景图 |
| 长时程一致性 | 历史过长、进度遗忘、循环探索、错误停止 | 事件化记忆、分层检索、显式任务状态、失败诊断与恢复 |
| 开放世界泛化 | 新场景、新目标、新措辞和新本体同时变化 | 多域数据、测试时适应、开放词汇检测、能力条件化规划 |
| Sim2Real | 外观、动力学、噪声和交互模式均有差异 | 实机闭环评测、数字孪生、域随机化、少样本在线校准 |
| 连续动作可靠性 | 语义决策频率低，直接回归控制难以保证平滑安全 | 分层/异步 VLA、轨迹 token、模型预测控制与安全过滤 |
| 评测有效性 | SR/SPL 难反映安全、交互成本和恢复能力 | 多维指标、失败类型标注、能耗/时延/碰撞与实机复现 |
| 数据可信度 | 合成指令同质化、成功轨迹偏置、潜在泄漏 | 自动可达性校验、失败数据、人工抽检和数据谱系记录 |

## 6. 对选题的判断

按研究成熟度与潜在价值，可以作如下判断：

- **较成熟、竞争激烈：** 在 R2R/REVERIE 上继续改进单点指标；通用视觉—语言编码器替换；常规数据增强。
- **活跃且仍有空间：** 任务相关的空间记忆、长时程进度建模、语义—几何混合规划、开放世界 ObjectNav、低成本/低时延导航。
- **高风险高潜力：** 可学习世界模型驱动的导航、多机器人协同、跨本体统一 VLA、实机在线适应和带形式化保证的安全 VLA。
- **适合 UAV-VLN 的切入口：** 方向与尺度鲁棒 grounding、固定算力下的长历史压缩、失败感知恢复、异步规划执行、真实飞行中的安全指标与数据闭环。

如果以“容易形成清晰论文贡献”为标准，建议把问题定义为一个可测量的闭环，而不是泛泛地“用更强 MLLM 做导航”。例如：在固定显存与时延预算下，比较不同事件化记忆对长航程成功率、重复探索率和恢复率的影响；或将 VLM 的语义 waypoint 与可证明安全的局部规划器结合，系统评估语义成功和物理安全之间的权衡。

## 7. 一句话展望

未来两三年，VLN 最可能形成的主流系统不是单一巨型网络，而是一个以 VLM/VLA 为语义中枢、以结构化三维记忆为长期状态、以世界模型辅助预测、以实时规划控制器保证可执行和安全的分层具身智能体；真正拉开差距的将是开放环境中的闭环可靠性，而不只是静态 benchmark 上的路径指标。

