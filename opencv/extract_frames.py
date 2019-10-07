```py
# Program To Read video
# and Extract Frames
import cv2, os
import numpy as np
_OUTPUT_PATH = './images'

def variance_of_laplacian(image):
	# compute the Laplacian of the image and then return the focus
	# measure, which is simply the variance of the Laplacian
	return cv2.Laplacian(image, cv2.CV_64F).var()

# Function to extract frames
def capture_frames(path, frames_i):
    frames = []
    for i, frame_num in enumerate(frames_i):
        vidObj = cv2.VideoCapture(path)
        vidObj.set(cv2.CAP_PROP_POS_FRAMES, frame_num)
        #print('frame', vidObj.get(cv2.CAP_PROP_POS_FRAMES))
        success, image = vidObj.read()
        if success == False:
            print('failed to read video file')
            break
        blur = round(variance_of_laplacian(image), 4)
        print("frame_{0}_blur_{1}.jpg".format(frame_num, blur))
        if blur > 40:
            cv2.imwrite(os.path.join(_OUTPUT_PATH, "frame_{0}_blur_{1}.jpg".format(frame_num, blur)), image)
            frames.append(image)
    return frames

if __name__ == '__main__':
    images = capture_frames("D:/Dev/ManLab/videos/Beach_Family/video.mp4", [1803, 1855, 1889, 1905, 1908])
    print('x')
```
