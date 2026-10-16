# 梳理一下，目前视觉对话导航的研究现状以及发展的过程

> 梳理一下，目前视觉对话导航的研究现状以及发展的过程

<details><summary>4 previous messages</summary>

> 我会把“视觉对话导航”按具身智能中的 Vision-and-Dialog Navigation（VDN）来梳理：先理清任务从 VLN、CVDN 到更开放交互式导航的演进，再总结数据集、方法路线、评测现状和当前瓶颈。考虑到“目前”涉及近年的新进展，我会核对论文与官方项目页。
>
> <details><summary>Searched the web</summary>
>
> Searched the web for `Vision-and-Dialog Navigation CVDN paper CVPR 2020 official ...`
>
> Searched the web for `CVDN navigation dialog history transformer paper ...`
>
> Searched the web for `RMM recursive mental model dialog navigation CVDN paper arxiv ...`
>
> </details>
>
> 初步看，这个方向的主线不是简单“把对话文本喂给导航器”，而是经历了三次明显转向：静态利用历史对话 → 在线决定何时/问什么 → 双方都不全知、把定位与沟通纳入闭环。接下来我再补齐 2022–2026 年几个扩展分支，避免把相关任务混成一类。
>
> <details><summary>Searched the web</summary>
>
> Searched the web for `DialFRED dialog embodied navigation benchmark official paper ...`
>
> Searched the web for `Talk the Walk navigation dialog benchmark ACL anthology 2018 ...`
>
> Searched the web for `site:openaccess.thecvf.com/content/ICCV2025 "Navigation only" "DialNav" "13.9" ...`
>
> </details>
</details>

下面按具身智能中的“视觉—对话导航”（Vision-and-Dialog Navigation，VDN）来梳理。截至 2026 年 9 月，这个方向已经从“读取一段历史对话来导航”，逐渐发展到“智能体主动提问、远程人类定位智能体、双方通过多轮对话协作完成导航”的完整闭环。

一个核心判断是：传统视觉语言导航 VLN 的技术已经相对成熟，但真正的开放式、多轮、双向视觉对话导航仍处于早期阶段。当前瓶颈已经不只是视觉—语言融合，而是空间记忆、不确定性判断、提问策略、协作者建模和系统级误差传播。

## 1. 任务是什么

传统 VLN 通常是：

> 人类给出一次完整指令 → 智能体观察环境 → 执行动作 → 到达目标。

视觉对话导航则是：

> 人类给出可能模糊的目标 → 智能体边看、边走、边判断是否需要帮助 → 主动提问 → 根据回答继续行动。

因此，完整 VDN 至少包含五项能力：

1. 视觉与语言的空间 grounding；
2. 对话历史和访问轨迹记忆；
3. 判断何时需要提问；
4. 生成有信息量的问题；
5. 根据回答更新空间信念并执行导航。

要特别区分两种常被混用的设置：

- **静态对话历史导航**：完整对话已经给定，智能体只负责预测路线，如 NDH。
- **在线交互式导航**：智能体自己决定什么时候问、问什么，Guide 现场回答，如 RMM、DialNav。

前者更接近“长文本条件下的 VLN”，后者才是严格意义上的交互式 VDN。

## 2. 发展过程

| 阶段 | 代表工作 | 核心变化 |
|---|---|---|
| 2017–2018：基础任务形成 | R2R、EmbodiedQA | 建立真实图像室内仿真、视觉语言导航和主动视觉探索 |
| 2018：具身对话雏形 | Talk the Walk | 两个智能体通过语言完成定位与导航 |
| 2019–2020：VDN 正式提出 | CVDN / NDH | 将人—人多轮导航对话引入 Matterport3D |
| 2020–2021：记忆、预训练与 Transformer | CMN、PREVALENT、VISITRON、HAMT | 从 LSTM 转向跨模态记忆、预训练和长历史 Transformer |
| 2020–2021：从被动理解转向主动提问 | Just Ask、RMM、SCoA | 联合学习“是否问、问什么、如何利用回答” |
| 2021：重新审视任务与指标 | NDH-Full | 从局部对话—子路径改为完整对话—完整轨迹 |
| 2022–2023：任务扩展 | TEACh、DialFRED、AVDN | 从纯导航扩展到操作、家务任务和连续空间无人机导航 |
| 2024–2025：协作定位与真实对话闭环 | DiaLoc、ELBA、DialNav | 将协作者定位、自由提问和完整系统评测纳入任务 |
| 2026：多模态大模型与免训练推理 | PSC-AVDN | MLLM、显式空间记忆和分阶段推理成为新路线 |

### 2.1 前史：从 VLN 到具身对话

2018 年的 R2R 建立了基于 Matterport3D 真实室内全景图像的经典 VLN 范式，但语言是单向、一次性给出的。[R2R 论文](https://openaccess.thecvf.com/content_cvpr_2018/html/Anderson_Vision-and-Language_Navigation_Interpreting_CVPR_2018_paper.html)

同年的 Talk the Walk 已经出现“双智能体协作”的思想：Tourist 看到街景，Guide 掌握地图，双方通过对话完成定位和导航。不过环境是结构化的纽约街区，导航和感知真实性有限。[Talk the Walk](https://arxiv.org/abs/1807.03367)

### 2.2 2019–2020：CVDN 奠定标准任务

CVDN 是该方向最具标志性的起点。它包含：

- 2,050 段人—人导航对话；
- 7,000 多段导航轨迹；
- 83 个 Matterport3D 房屋；
- Navigator 根据第一视角图像行动并提问；
- Guide 能访问通往目标的最短路径信息。

在此基础上，论文定义了 Navigation from Dialog History（NDH）：给定目标物体和已有对话历史，让智能体预测后续路线。[CVDN/NDH 原始论文](https://proceedings.mlr.press/v100/thomason20a.html)

但 NDH 有一个根本局限：虽然数据来自交互过程，模型评测时的对话却是预先给定的。智能体并不真正生成问题，也不能根据运行时状态改变交流过程。

### 2.3 2020–2021：解决跨模态历史建模

早期方法主要研究如何从长对话和视觉轨迹中找到当前决策所需的信息。

- CMN 分别维护语言记忆和视觉记忆，通过跨模态注意力关联历史对话、过去视觉状态和当前观察。[CMN，CVPR 2020](https://openaccess.thecvf.com/content_CVPR_2020/html/Zhu_Vision-Dialog_Navigation_by_Exploring_Cross-Modal_Memory_CVPR_2020_paper.html)
- PREVALENT 把大规模视觉—语言—动作预训练迁移到 CVDN，确立了“预训练再微调”的路线。
- VISITRON 使用物体语义作为视觉和对话之间的锚点，同时增加是否交互的预测头。[VISITRON](https://arxiv.org/abs/2105.11589)
- HAMT 使用层次化 Transformer 显式编码过去的全景观察，在 CVDN 以及多种长程 VLN 任务上验证了长历史建模的价值。[HAMT，NeurIPS 2021](https://papers.nips.cc/paper/2021/hash/2e5c2cb8d13e8fba78d95211440ba326-Abstract.html)

这一阶段主要回答的是：

> 已有对话很多时，怎样正确记忆和利用它？

### 2.4 从“理解回答”转向“主动提问”

另一条路线开始研究智能体的主动交流能力。

- Just Ask 根据动作不确定性决定何时请求帮助，并用强化学习控制交流成本。[Just Ask，AAAI 2020](https://ojs.aaai.org/index.php/AAAI/article/view/5627)
- RMM 引入类似 Theory of Mind 的递归心理模型：Navigator 模拟 Guide 可能如何回答，Guide 又模拟 Navigator 将如何行动，并用最终导航进展联合优化导航、问题和回答。[RMM](https://arxiv.org/abs/2005.00728)
- SCoA 将问题分成 whether-to-ask 和 what-to-ask 两个策略，希望减少对固定提问位置和人工对话标注的依赖。[SCoA，ICCV 2021](https://openaccess.thecvf.com/content/ICCV2021/html/Zhu_Self-Motivated_Communication_Agent_for_Real-World_Vision-Dialog_Navigation_ICCV_2021_paper.html)

这使问题从“怎样利用语言”转向：

> 当前信息是否足够？如果不足，问什么最有价值？

### 2.5 NDH-Full：任务定义和评测反思

NDH 将一段完整对话切成多个子路径实例，主要指标是 Goal Progress。但研究发现，局部 Goal Progress 与完整轨迹质量、nDTW 等指标可能并不一致，也不能充分监督最终到达目标。

NDH-Full 因而把完整对话和完整导航路径作为一个实例，并尝试预训练、课程学习和数据增强。[NDH-Full，EMNLP 2021](https://aclanthology.org/2021.emnlp-main.518/)

这揭示了该领域长期存在的问题：**模型可能在某个局部指标上提高，却没有学会完整的协作导航。**

### 2.6 2022–2023：向更复杂任务扩展

随后，视觉对话不再局限于室内图导航。

- TEACh 收集了 3,000 多段人—人交互对话，Follower 不仅需要导航，还要操作物体、完成做咖啡或准备早餐等长程任务。[TEACh，AAAI 2022](https://ojs.aaai.org/index.php/AAAI/article/view/20097)
- DialFRED 在 ALFRED 上加入主动提问，提供约 53,000 个任务相关问答，问题涉及物体位置、外观和方向。[DialFRED](https://arxiv.org/abs/2202.13330)
- AVDN 将任务扩展到连续空间无人机导航，包含 3,000 多条轨迹和异步人—人对话，并利用人类视觉注意信息辅助预测航点。[AVDN，ACL 2023](https://aclanthology.org/2023.findings-acl.190/)

这说明 VDN 正在与更广义的 embodied instruction following、任务规划和机器人操作融合。

### 2.7 2024–2026：远程协作与多模态大模型

2024 年的 DiaLoc 强调：Guide 如果不知道智能体的位置，就必须通过多轮描述逐步更新位置分布。它把对话定位从“一次性读取完整历史”改为更自然的迭代信念更新。[DiaLoc，CVPR 2024](https://openaccess.thecvf.com/content/CVPR2024/html/Zhang_DiaLoc_An_Iterative_Approach_to_Embodied_Dialog_Localization_CVPR_2024_paper.html)

2025 年 DialNav 进一步建立完整闭环：

- Navigator 决定是否提问并生成问题；
- Guide 不知道 Navigator 的真实位置；
- Guide 必须先根据对话定位 Navigator，再给出路线；
- 同时评测导航、提问、定位和回答；
- 配套 RAIN 数据集包含 2,231 个 episode。

这比 CVDN 中的“全知 Guide”更接近真实远程协作。论文也表明，Guide 定位误差会沿着回答和导航链条传播，成为系统主要瓶颈。[DialNav，ICCV 2025](https://openaccess.thecvf.com/content/ICCV2025/papers/Han_DialNav_Multi-turn_Dialog_Navigation_with_a_Remote_Guide_ICCV_2025_paper.pdf)

到 2026 年，MLLM 开始直接承担对话解析、场景理解和策略推理。例如 PSC-AVDN 将无人机对话导航分为解析、搜索和确认三个推理阶段，并结合显式结构化空间记忆，在不专门训练模型的情况下完成 AVDN。[PSC-AVDN，CVPR 2026](https://openaccess.thecvf.com/content/CVPR2026/html/Qi_Parse_Search_and_Confirmation_Training-Free_Aerial_Vision-and-Dialog_Navigation_with_Chain-of-Thought_CVPR_2026_paper.html)

## 3. 当前主要研究路线

目前可以归纳为五条路线：

1. **跨模态状态与长程记忆**

   从循环隐状态发展到完整轨迹 Transformer、拓扑图和显式空间记忆，解决历史遗忘、指代消解和重复探索。

2. **主动提问与不确定性估计**

   研究何时问、问什么，以及如何在成功率和人类交流成本之间权衡。2025 年的研究开始专门判断“指令缺失的信息是否足以影响行动”，而不再只看动作分布熵。[To Ask or Not to Ask，WACV 2025](https://openaccess.thecvf.com/content/WACV2025/html/Abraham_To_Ask_or_Not_to_Ask_Detecting_Absence_of_Information_WACV_2025_paper.html)

3. **Guide/Navigator 双方建模**

   从全知 Oracle 发展到远程 Guide。双方需要维护对彼此知识、位置和意图的估计，本质上接近多智能体部分可观测决策问题。

4. **自由语言生成**

   早期大量工作使用模板问题或有限问题候选；现在逐步转向自由形式问题和回答。ELBA 已在 TEACh 上探索 answer-aware 的自由问题生成。[ELBA，WACV 2025](https://openaccess.thecvf.com/content/WACV2025/papers/Shen_ELBA_Learning_by_Asking_for_Embodied_Visual_Navigation_and_Task_WACV_2025_paper.pdf)

5. **基础模型与显式空间结构结合**

   当前趋势不是单纯依赖 MLLM 端到端输出动作，而是让大模型负责语义解析和高层决策，同时保留拓扑地图、几何记忆、目标确认和低层控制模块。

## 4. 仍未解决的关键问题

- **数据规模小且分散**：CVDN、RAIN 等只有数千段交互，远少于通用视觉语言预训练数据。
- **对话有时并非真正必要**：静态 NDH 可以把全部对话当成一条长指令，模型可能绕过在线协作。
- **Guide 权限不现实**：很多设置默认 Guide 知道精确位置或最短路径，现实用户通常没有这种全局信息。
- **空间推理仍弱**：左右方向、跨房间拓扑、回退、楼层关系和长时指代仍容易出错。
- **模块误差累积**：错误定位会产生错误回答，错误回答又会导致错误路线和后续问题。
- **交流成本缺少统一定义**：问题数量少不一定好，关键是每个问题带来的信息增益。
- **生成指标与任务成功不一致**：BLEU、ROUGE 高并不代表问题有用；模仿人类轨迹也不必然意味着任务完成。
- **仿真到现实差距明显**：真实机器人还要处理连续控制、遮挡、动态人员、语音识别错误、网络延迟和安全约束。
- **MLLM 幻觉与空间记忆问题**：大模型语言能力很强，但容易给出流畅却空间上错误的指令，因此仍需可验证地图和确认机制。

## 5. 总体判断

这个领域可以概括为：

> 已经从“多模态序列建模问题”发展成“多智能体、部分可观测、带通信成本的协作决策问题”。

CVDN/NDH 奠定了基础，但已不足以代表最前沿。现在更值得关注的是：

- DialNav 式远程、非全知 Guide；
- 自由形式、以信息增益为目标的主动提问；
- 对话驱动的概率定位与空间信念更新；
- MLLM 与显式拓扑/几何记忆结合；
- 从室内图导航扩展到连续控制、无人机、物体操作和真实机器人；
- 用任务成功、路径效率、交流成本、鲁棒性和安全性进行联合评测。

换句话说，VDN 的视觉编码和语言理解模块进步很快，但“什么时候应该承认自己不知道、怎样提出最有价值的问题、怎样让一个并不全知的人真正帮助自己”仍是核心研究空白。
