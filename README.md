# To change the body type of one person to body type of another person given two images

<img src="https://github.com/andrewdcampbell/seam-carving/blob/master/demos/visuals/lake_shrink.gif" width="900">

A fast Python implementation of [Seam Carving for Content-Aware Image Resizing ](https://inst.eecs.berkeley.edu/~cs194-26/fa18/hw/proj4-seamcarving/imret.pdf) (2007), including the improved energy algorithm described in [Improved Seam Carving for Video Retargeting](http://www.eng.tau.ac.il/~avidan/papers/vidret.pdf) (2008).

## Requirements
* OpenCV
* scipy
* numba
* numpy

## Usage
```
python seam_carving.py (-resize | -remove) -im <IM_PATH> -out <OUTPUT_IM_NAME> [-dx <DX>] 
```


For both modes:
* `-im`: The path to the image to be processed.
* `-out`: The name for the output image.
* `-mask`: (Optional) The path to the protective mask. The mask should be binary and have the same size as the input image. White areas represent regions where no seams should be carved (e.g. faces).
* `-vis`: If present, display a window while the algorithm runs showing the seams as they are removed.
* `-backward_energy`: If present, use the backward energy function (i.e. gradient magnitude) instead of the forward energy function (default).


# Algorithm used: 
1. **Mediapie** library used for **key point detection**
2. Left and right shoulders detected, distances between shoulder measured. Say distance between lt and rt shoulder for person 1 is 15 while for person 2 it is 20. So if 5 pixels are removed from the middle of the person then we get person 2 looking like person 1 
3. The difference in above distance, the number of pixels removed as the seam through an algorithm called **seam carving algorithm**

# Key-point Detection
To detect essential features of the images to determine by what amount to reduce or increase the width of the given image

 
#Seam-carving Algorithm
An effective method to resize images by removing pixels without cropping images or resulting in loss of information

## Acknowledgements
Many parts of the code are adapted/optimized versions of functionality from other implementations:
* https://github.com/axu2/improved-seam-carving
* https://github.com/vivianhylee/seam-carving
* https://karthikkaranth.me/blog/implementing-seam-carving-with-python/
* Seam carving for content-aware image resizing(2007) [link](https://dl.acm.org/doi/10.1145/1275808.1276390#:~:text=By%20repeatedly%20carving%20out%20or,defined%20by%20the%20energy%20function)
* [Mediapie for key point detection](https://www.analyticsvidhya.com/blog/2022/03/pose-detection-in-image-using-mediapipe-library/)

