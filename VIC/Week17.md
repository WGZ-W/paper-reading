
## Week17
[1]. Rui Li, Yishu Liu, Huafeng Li, Jinxing Li, and Guangming Lu. 2024. Prototype-Guided Dual-Transformer Reasoning for Video Individual Counting.(MM '24).10258–10267.

This paper uses Transformer to calculate the similar parts of two adjacent frames, and then finds its own private parts for each frame to predict the number of inflow and outflow people.

## General content
The Multi-receptive field feature fusion module accepts features of different scales, takes them through a feature alignment pyramid, and then generates features *F* through a feature fusion encoder.  
Dynamic Prototype Generation module based on iterative clustering similar information, generate *X*.   
The Prototype Cross-guided Decoder module uses Transformer to operate on *X* and *F* to generate shared features *Z*.  
Finally, using the Privacy-decoupling module to operate on *F* and *Z*, find out the private features in the frame, and then predict the coordinates based on the features.


## Comparison of methods
DRNet generates a descriptor for each pedestrian, which is used for matching in the inference stage. DRNet uses feature matching inference to match each pedestrian with its own feature.  
CGNet uses two kinds of labels, which are used to represent inflow and outflow, and then uses a group-level matching method to divide pedestrians into four sets for group matching.  
PDTR uses the label which is whether in this frame, and then directly use Transformer to generate similar features, then the private features in each frame can be inferred.  
As a whole, both are used to match features, DRNet is used to match each individual, and the latter two are used to match groups. In addition, the first two are some pre-processing of the data, and then the matching algorithm is used, but PDTR is an end-to-end prediction.  

## Problem
Another point is that DRNet considers the number of pedestrians who go out and re-enter to be small, so it ignores them directly. CGNet uses Memory-based Count Predictor for prediction. A factor TTL is proposed to update pedestrians. As for PDTR, this problem is not considered because it is directly processed for two adjacent frames.