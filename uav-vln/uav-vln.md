
# UAV-VLN

- **AerialVLN: Vision-and-Language Navigation for UAVs** & Shubo Liu, Yuankai Qi. **ICCV 2023** & [(arxiv)](https://arxiv.org/abs/2308.06735)
  - **提出新任务 AerialVLN**：首个面向无人机的、室外城市级视觉-语言导航任务。
  - **开发高保真模拟器**：基于 Unreal Engine 4 和 AirSim，
  - **构建大规模数据集**：
  - **提出基线模型**：评估了随机、动作采样、LingUNet、Seq2Seq、CMA，并改进提出 Look-ahead Guidance (LAG) 策略。

- **CityNav: A Large-Scale Dataset for Real-World Aerial Navigation** & Jungdae Lee, Nakamasa Inoue & **ICCV 2025** & [(arxiv)](https://arxiv.org/abs/2406.14240)（不怎么熟悉）
  - **CityNav数据集**：
  - 地理语义地图（GSM）表示

- **Towards Realistic UAV Vision-Language Navigation: Platform, Benchmark, and Methodology（OpenUAV）（TravelUAV）** & Xiangyu Wang, Si Liu & **ICLR 2025** & [(arxiv)](https://arxiv.org/abs/2410.07087)
  - OpenUAV platform （基于 UE4 + AirSim；6自由度（DoF）连续轨迹）
  - 数据集：目标导向的 UAV VLN 数据集（TravelUAV）
  - 基准：UAV-Need-Help

- **OpenFly: A comprehensive platform for aerial vision-language navigation** & Yunpeng Gao, Bin Zhao. **ICLR 2026** & [(arxiv)](https://arxiv.org/abs/2502.18041)
  - **OpenFly平台**：
    - 集成 4 大渲染引擎/技术
    - 全自动数据生成工具链
  - **大规模数据集**：
  - **OpenFly-Agent**：基于OpenVLA，引入**关键帧选择**（根据动作突变 + 地标定位模块）和**视觉令牌合并**（减少冗余）。）

- **LookasideVLN: Direction-Aware Aerial Vision-and-Language Navigation** & **CVPR 2026** & [Arxiv](https://arxiv.org/abs/2604.17190)


- **RecoverFly: A Failure-Aware Reinforcement Learning Post-Training Framework for Aerial Vision-Language Navigation** & Boxiong Wang, Daxin Tian & [(arxiv)](https://arxiv.org/abs/2608.09467)
  - 提出**首个面向端到端无人机 VLA 的失败感知 RL 后训练框架**，统一处理动作优化、失败利用、长尾适应和策略稳定问题。
  - 设计**动态失败重播**，有效利用稀疏失败反馈，提升样本效率。
  - 引入**两阶段场景课程 + 参考策略 KL 正则化**，改善稀有场景学习并防止策略漂移。
  - 在 TravelUAV 基准上验证了方法的**有效性、鲁棒性和泛化能力**，显著超越现有方法。




- **SkyVLN: Vision-and-Language Navigation and NMPC Control for UAVs in Urban Environments** & **IROS 2025** & [arxiv](https://arxiv.org/abs/2507.06564)

- **Towards Autonomous UAV Visual Object Search in City Space: Benchmark and Agentic Methodology** & & **AAAI 2026** & [Web](https://ojs.aaai.org/index.php/AAAI/article/view/38898)


- **Memory-Augmented Scene Understanding and Exploration for Open-World Aerial Object-Goal Navigation** & **CVPR 2026**. 
  - 历史信息：八叉树
  - UAV-ON benchmark


- **UAV-ON: A Benchmark for Open-World Object Goal Navigation with Aerial Agents** & Jianqiang Xiao, Xiang Deng & **ACM MM Dataset Track 2025** & [(arxiv)](https://arxiv.org/abs/2508.00288)
  - UAV-ON benchmark



- **LongFly: Long-Horizon UAV Vision-and-Language Navigation with Spatiotemporal Context Integration.** Wen Jiang, Xiangyang Ji & [(arxiv)](https://arxiv.org/abs/2512.22010)
  - 历史信息：使用槽压缩（固定存储）
  - 

- **NavAgent: Multi-scale Urban Street View Fusion For UAV Embodied Vision-and-Language Navigation** & & [(arxiv)](https://arxiv.org/abs/2411.08579) &

- **CityNavAgent: Aerial Vision-and-Language Navigation with Hierarchical Semantic Planning and Global Memory** &&[(arxiv)](https://arxiv.org/abs/2505.05622)&

- **Exploring Spatial Representation to Enhance LLM Reasoning in Aerial Vision-Language Navigation** & & [(arxiv)](https://arxiv.org/abs/2410.08500v3)

- **Aerial Vision-and-Language Navigation with Grid-based View Selection and Map Construction** & & [(arxiv)](https://arxiv.org/abs/2503.11091)

- **GeoNav: Empowering MLLMs with dual-scale geospatial reasoning for language-goal aerial navigation** & & **Pattern Recognition (2026)** & [(arxiv)](https://arxiv.org/abs/2504.09587)
  - CityNav



- **UAV Visual Navigation in the Large-Scale Outdoor Environment: A Semantic Map-Based Cognitive Escape Reinforcement Learning Method** & [Web](https://ieeexplore.ieee.org/document/10847926)


- **UAV-FlowColosseo: A Real-World Benchmark for Flying-on-a-Word UAV Imitation Learning** & **NeurIPS 2025 Datasets and Benchmarks Track** & [PDF](https://proceedings.neurips.cc/paper_files/paper/2025/file/92cfa104db7fdd053492df3589ddfd49-Paper-Datasets_and_Benchmarks_Track.pdf)


- **FlySearch: Exploring how vision-language models explore** & **NeurIPS 2025 Datasets and Benchmarks** & [arxiv](https://arxiv.org/abs/2506.02896)


- **SA-GCS: Semantic-Aware Gaussian Curriculum Scheduling for UAV Vision-Language Navigation** & [arxiv](https://arxiv.org/abs/2508.00390)



- **OpenVLN: Open-world Aerial Vision-Language Navigation** & [arxiv](https://arxiv.org/abs/2511.06182)

- **ASMA: An Adaptive Safety Margin Algorithm for Vision-Language Drone Navigation via Scene-Aware Control Barrier Functions** & **RAL 2025** & [arxiv](https://arxiv.org/abs/2409.10283)

- **AirNav: A Large-Scale UAV Vision-and-Language Navigation Dataset with Natural and Diverse Instructions** & [arxiv](https://arxiv.org/abs/2601.03707)

- **AirUniNav: Unified Vision-Language Navigation for UAVs in Indoor and Outdoor Scenes** & [Web](https://forhumble.github.io/AirUni/)

- **AutoFly: Vision-Language-Action Model for UAV Autonomous Navigation in the Wild** & **ICLR 2026** & [arxiv](https://arxiv.org/abs/2602.09657)

- **Fly0: Decoupling Semantic Grounding from Geometric Planning for Zero-Shot Aerial Navigation** & [arxiv](https://arxiv.org/abs/2602.15875)

- **APEX: A Decoupled Memory-based Explorer for Asynchronous Aerial Object Goal Navigation** & **CVPR 2026** & [arxiv](https://arxiv.org/abs/2602.00551)

- **OnFly: Onboard Zero-Shot Aerial Vision-Language Navigation toward Safety and Efficiency** & [Arxiv](https://arxiv.org/abs/2603.10682)

- **SpatialFly: Implicit 3D Prior-Guided Visual Reparameterization for Continuous UAV Vision-and-Language Navigation** & [Arxiv](https://arxiv.org/abs/2603.21046)

- **AerialVLA: A Vision-Language-Action Model for UAV Navigation via Minimalist End-to-End Control** & [Arxiv](https://arxiv.org/abs/2603.14363)

- **History-Enhanced Two-Stage Transformer for Aerial Vision-and-Language Navigation** & **AAAI 2026** & [Arxiv](https://arxiv.org/abs/2512.14222)


- **AirHunt: Bridging VLM Semantics and Continuous Planning for Efficient Aerial Object Navigation** & [Arxiv](https://arxiv.org/abs/2601.12742)


- **Aerial Vision-Language Navigation with a Unified Framework for Spatial, Temporal and Embodied Reasoning** & **TCSVT 2026** & [Arxiv](https://arxiv.org/abs/2512.08639)

- **How Far Are Large Multimodal Models from Human-Level Spatial Action? A Benchmark for Goal-Oriented Embodied Navigation in Urban Airspace** & [Arxiv](https://arxiv.org/abs/2604.07973)

- **HTNav: A Hybrid Navigation Framework with Tiered Structure for Urban Aerial Vision-and-Language Navigation** & **CVPR 2026** & [Arxiv](https://arxiv.org/abs/2604.08883)


