
# Week 15

[1]. Han, Tao et al. “DR.VIC: Decomposition and Reasoning for Video Individual Counting.” 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) (2022): 3073-3082.

Video Individual Counting refer to the total number of pedestrians in a video and a person only counted once.

Single image counting and cross-line counting have some disadvantages at this task.

Multiple Object Tracking need more resource and it's accuracy has a little bit low.

So this paper proposed a end-to-end Decomposition and Reasoning Network (DRNet) to try to solve this task in a better way.

DRNet try to decompose the task to two stages:
1. counting the pedestrians of the initial frame.
2. reasoning the inflow pedestrians in the following frame.

### Method
DRNet has three modules, :
1. image representation module, which maps two input images to feature represetations.
2. Using the feature represetation to generate density maps, and extract the head discriptors from density maps.
3. Then the problem could be consider to a assignment problem and this paper choose Optimal Transport theory to solve this assignment problem.  