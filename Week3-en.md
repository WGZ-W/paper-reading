# Week3
This week I will report two papers which I have read.

# Advances in edge-cloud collaboration and evolution for large-small models
The collaboration and evolution for large-small models mainly uses the global general knowledge of foundation models and the personalized and special knowledge of massive edge small models to improve the performance of large-small models in a collaboration and evolution way, and complete cloud-edge empowerment and edge reasoning.

## 1- Foundation models
Mainly include large language models and large multimodal models.

### 1.1- Large language models
Large language models are mostly based on Transformer architecture and use self-attention mechanism, and can be divided into encoder-based model, decoder-based model and encoder-decoder hybrid model.  
Pre-training is often unsupervised and includes:
- Random occlusion to predict the blank filling;
- Using autoregression, maximize the prediction probability of the next word based on the given sequence;
- Combine the first two ways.

Adjust parameters to the model:
- Adaptor tuning, design adaptor with few parameters embedded in the pre-trained large model.
- Prompt fine-tuning, adding task-related trainable prompts at input time.

### 1.2- Large multimodal models
Multi-modal information is trained together to realize cross-modal understanding and generation of large models.
The main methods include:
- Contrastive language-image pretraining (CLIP) model;
- DALL-E model based on VAE;
- And then there's the current diffusion model.

## 2- model compression
model compression includes:
- Model pruning, model pruning removes redundant parameters from models to reduce model size. Model pruning includes structured pruning and unstructured pruning;
  - Neural network channels or filter banks in structured pruning removal models.
  - Unstructured pruning includes pruning of neuronal connections or pruning of convolutional nuclei.
- model quantization, is to convert a floating-point model to a fixed-point model, using a low-precision data type to compress the number of parameters.
- knowledge distillation, transfer knowledge from a large model to a small model by guiding a small, lightweight model to mimic the behavior of a larger, more powerful model.

## 3- Large-small model collaboration
- The collaborative training is carried out by knowledge distillation and feature transmission among large and small models.
- Collaborative inference, segmentation of the model, deployment of sub-modules to the cloud side or edge side according to computing power constraints, through the coordination of sub-modules to complete specific tasks.
- Collaborative planning, it is difficult for a single model to complete the planning of complex tasks, and collaborative planning between models is needed.

## 4- Development trend and prospect
The large and small model collaboration technology is developed in the direction of heterogeneous model knowledge transfer and local model continuous enhancement. At the same time, the research on the reliability of generative large-small model has become increasingly prominent.

# Overview of YOLO series target detection algorithms
Yolo is a single-stage object detection algorithm. Object detection mainly includes the determination of object existence, classification, and location of object space.  
The development of new activation functions and attention mechanisms improves the target detection accuracy of Yolo algorithm.

## 1- Yolo network structure
It is mainly composed of backbone network, neck network and head network.  
The main task of backbone network is feature extraction. The neck network is a fusion of multi-layer features. The header network is the part used for target detection. At the same time, the choice of anchor frame will also affect the detection of the target.

## 2- Yolo loss function
It mainly consists of three parts: prediction frame coordinate loss, confidence loss and class loss.

## 3- Yolo data set and evaluation indicators
dataset:
- Some typical datasets for object detection are: `PASCAL VOC` dataset, `ImageNet` dataset, `Google Open Images` dataset, `MS COCO` dataset and `DOTA` dataset.

evaluation indicators:
- Generally, FPS is used to measure the algorithm speed and AP value is used to measure the algorithm precision.

## 4- Yolo problems and Prospects
problems:
- Yolo algorithm transforms the object detection problem into regression and classification problem, which has advantages in speed.
- However, the localization accuracy of small target is not as good as that of two-stage algorithm.
- At the same time, Yolo requires a lot of pictures to train.

prospects:
- Multi-task learning, integrated object detection and semantic segmentation;
- Edge computing, deploying Yolo to embedded edge computing devices;
- Multi-modal combination, language and sound are integrated into the algorithm to assist target detection.