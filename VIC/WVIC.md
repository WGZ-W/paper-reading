

# WVIC
## Introduction
VCC refer to count the number of people in each frame
of a video.

VIC count the total number of people with unique 
identities appearing in a video.

This paper introduce Weakly supervised Video Individual
Counting wherein trajectory labels are not provided and
just provide two types labels to indicate inflow and 
outflow.

The apparent approach to crowd counting in VIC task 
is to count the people in the initial frame and add the
number of people who come into the camera's field of
view in later frames.

The WVIC task does not require accurately identify the 
same people in both frames. It just need to annotate
the inflow and outflow people. Thus it reduces annotation
costs compared to creating individual pairwise target
assosiations for each observed pedestrian between 
neighboring frames.
   
## Related Works
### VCC
VCC 是计数视频中的每一帧的人数， 
根据解决的问题分成两类方法， ROI 和 LOI.

ROI 检测行人在一个特定的区域，使用 
temporal context informationand, ROI
methods can not be used in the VIC task.

LOI 统计经过一个虚拟的线的行人数量，
由于行人来往各个方向，所以很难找到一个合适的虚拟的线。

### Multiple Object Tracking
inevitable ID switching problem, 
