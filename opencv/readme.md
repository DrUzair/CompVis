# Image Descriptors
## SIFT, SURF
```sh
pip install opencv-python==3.4.2.16
pip install opencv-contrib-python==3.4.2.16
```

```py
import cv2
from cv2 import xfeatures2d
sift = xfeatures2d.SIFT_create(nfeatures=1000)
surf = xfeatures2d.SURF_create(hessianThreshold=400)

def root_desc(descs):
    eps = 1e-7
    descs /= (descs.sum(axis=1, keepdims=True) + eps)
    descs = np.sqrt(descs)
    return descs

def desc(img, method='sift'):
    if method == 'surf':
        kp, des = surf.detectAndCompute(img, None)
    if method == 'sift':
        kp, des = sift.detectAndCompute(img, None)
    return kp, des
```


# References
http://opencvpython.blogspot.com/
https://www.pyimagesearch.com/
