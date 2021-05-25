import glob
import cv2
import numpy as np
w = 1200
h = 750
images = glob.glob("./*.jpg", recursive=False)

for image_path in images:
    image = cv2.imread(image_path) 
    resized = cv2.resize(image, (w, h), interpolation = cv2.INTER_AREA)
    filename = image_path.split("/")[-1].split(".")[0] + "_resize.png"
    cv2.imwrite(filename, resized)