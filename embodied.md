

# Embodied

要实现更智能的“问”与“答”，以及更长的“记忆”与“推理”，是视觉对话导航（VDN）领域从“能用”迈向“好用”的关键。当前的研究正从依赖静态数据训练，转向构建能动态交互、持续学习的智能体。

围绕你的问题，我将当前的前沿方法分为“更智能的‘问’与‘答’”和“更长的‘记忆’与‘推理’”两个部分来展开。

---

### 🧠 更智能的“问”与“答”：从被动响应到主动求解

传统方法多依赖静态数据集，智能体只能被动地根据“历史对话”导航。实现更智能的交互，关键在于让智能体学会主动、高效地获取信息。

*   **策略性提问：学习“何时”与“何物”**
    这是实现智能交互的核心。代表性工作 **ELBA (Embodied Learning-By-Asking)**，通过让智能体学习“何时”以及“问什么”来动态获取完成任务所需的信息。它不再被动接受指令，而是主动识别信息缺口并提问。

*   **高效信息获取：像“二分查找”一样提问**
    “问什么”同样关键。**TSADE (Tree-Structured Strategy with Answer Distribution Estimator)**框架，受“分而治之”思想启发，通过设计问题，每轮**排除一半的候选对象**，能像最优搜索算法一样，用最少的问题锁定目标，避免无目的“闲聊”。

*   **迈向更复杂的交互：处理长程任务中的动态对话**
    更复杂的任务要求智能体进行持续、动态的对话。为此，研究者提出了**交互式实例目标导航（IION）** 等新任务，要求智能体不仅能导航，还能通过主动对话生成语言输出，以应对更复杂的交互场景。

### 🧩 更长的“记忆”与“推理”：从“金鱼”到“大象”

当前的模型，尤其是基于Transformer的模型，其**上下文窗口长度有限**，难以处理长序列。且其内部记忆是“隐式的”，缺乏明确的空间结构。因此，构建结构化的长时记忆是核心挑战。

*   **分层记忆系统：兼顾全局与局部**
    一个有效的方案是构建分层记忆系统。例如，**Mem4Nav**构建了一个“**分层空间认知长短时记忆系统**”，包含：
    *   **长期记忆（LTM）**：压缩并保留历史观测，存储环境的高级语义和拓扑结构。
    *   **短期记忆（STM）**：缓存最近的多模态信息，用于实时的避障和局部路径规划。
    该系统能将任何VLN导航模型作为“大脑”增强，在复杂城市环境中取得 **7-13个百分点** 的任务完成率提升。

*   **结构化空间记忆：让记忆“有章可循”**
    除了分层，记忆的结构化也至关重要。**PSC-AVDN**框架中的**结构化空间记忆（SSM）** 是一个典型。它整合了多尺度视觉观测、空间视觉记忆和结构化几何记忆三种信息，为导航提供全局空间上下文，确保长期一致性。

*   **记忆压缩与高效检索：应对信息过载**
    为了在有限的计算资源下存储海量信息，**记忆压缩**技术是关键。例如，**AstraNav-Memory**通过将每帧图像压缩为 **约30个token**，使模型能从处理“几十张”扩展到“数百张”图像。同时，**滑动窗口机制**等检索策略，可以只保留最近的决策历史，实现高效管理。

*   **增强推理能力：从“直觉”到“逻辑”**
    除了记忆，“推理”能力同样重要，特别是对空间关系的理解。
    *   **思维链（CoT）推理**：**PSC-AVDN** 通过“**解析-搜索-确认**”的三阶段推理流程，将复杂任务分解，逐步进行目标探索和精细验证。
    *   **专用空间推理模块**：**MSNav** 框架中的**空间模块（Spatial Module）**，专门负责空间推理和物体关系推断。为此，研究者还构建了**指令-对象-空间（I-O-S）数据集**，并微调出 **Qwen-Spatial (Qwen-Sp)** 模型，其空间推理能力超越了主流商业LLM。

### 💎 总结

总的来说，实现更智能的VDN，其演进方向是清晰的：

1.  **从“被动”到“主动”**：通过 **ELBA** 等方法，让智能体学会主动提问。
2.  **从“盲目”到“策略”**：采用 **TSADE** 等策略，让提问更高效。
3.  **从“短时”到“长时”**：利用 **Mem4Nav** 等分层记忆系统，构建持久的环境表征。
4.  **从“隐式”到“结构化”**：通过 **PSC-AVDN** 的SSM等，让记忆变得有结构、可检索。
5.  **从“直觉”到“逻辑”**：引入**思维链推理**和**专用空间模块（如MSNav）**，增强模型的逻辑推理能力。

这些技术并非孤立，而是相互增强的。例如，一个拥有长时记忆（如Mem4Nav）的智能体，才能基于历史提出更精准的问题（如ELBA）；而更强的推理能力（如PSC-AVDN），则能更好地利用这些记忆。未来，VDN智能体将不再是简单的指令跟随者，而是能主动探索、有效沟通并持续学习的自主agent。




- **Parse, Search, and Confirmation: Training-Free Aerial Vision-and-Dialog Navigation with Chain-of-Thought Reasoning and Structured Spatial Memory** & **CVPR 2026** & [(PDF)](https://openaccess.thecvf.com/content/CVPR2026/papers/Qi_Parse_Search_and_Confirmation_Training-Free_Aerial_Vision-and-Dialog_Navigation_with_Chain-of-Thought_CVPR_2026_paper.pdf)
  - 历史信息：结构化空间记忆（Structured Spatial Memory, SSM）
  - ANDH and ANDH-Full datasets
  - Training Free


- **Vision-and-Dialog Navigation** & Jesse Thomason, Michael Murray, Maya Cakmak, Luke Zettlemoyer & **Conference on Robot Learning (CoRL) 2019** & [(Arxiv)](https://arxiv.org/abs/1907.04957)


- **To Ask or Not to Ask? Detecting Absence of Information in Vision and Language Navigation** & Savitha Sam Abraham, Sourav Garg, Feras Dayoub & **WACV 2025** & [(PDF)](https://openaccess.thecvf.com/content/WACV2025/papers/Abraham_To_Ask_or_Not_to_Ask_Detecting_Absence_of_Information_WACV_2025_paper.pdf)

- **ELBA: Learning by Asking for Embodied Visual Navigation and Task Completion** & Ying Shen, Daniel Bis, Cynthia Lu, Ismini Lourentzou & **WACV 2025** & [(PDF)](https://openaccess.thecvf.com/content/WACV2025/papers/Shen_ELBA_Learning_by_Asking_for_Embodied_Visual_Navigation_and_Task_WACV_2025_paper.pdf)
  - 策略性提问

- **Divide-and-Conquer: Tree-structured Strategy with Answer Distribution Estimator for Goal-Oriented Visual Dialogue** & Shuo Cai & **AAAI 2025** & [(Web page)](https://ojs.aaai.org/index.php/AAAI/article/view/32187)
  - 高效信息获取