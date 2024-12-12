

image-level pedestrian counting, cross-line crowd counting,
Multiple Object Tracking, 
end-to-end Decomposition and Reasoning Network (DRNet).

Significant challenges in the city management: 
such as transport management, public space design...

SICC and VCC 

- image-level pedestrian counting, 
  - over-counting
- cross-line crowd counting,
  - manual annotation
- Multi-Object Tracking,
  - operates on each frame
- DRNet
  - Three components
# DRNet
## Introduction
Existing work about pedestrian counting either only focus on image-level counting or are constrained to the manual annotation of lines.

This paper propose a new perspective - Video Individual Counting (VIC), which counts the total number of indiviudal pedestrian in the given video (a person is only counted once).

The method to solve the problem is to decompose all the pedestrians into the initial pedestrians who existed in the first frame and new pedestrians with separate identities. 

