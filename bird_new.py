# This code transforms the images of the Extracted potholes to Top view (Inverse Perspective) 

import cv2
import numpy as np
import os

directory = r'Path to the folder containing - Extracted Potholes'
save_dir = r'Path to the newly created folder where you want to store the transformed images'

files = os.listdir(directory)

for file in files:
    path = os.path.join(directory,file)
    img = cv2.imread(path)
    height, width, _ = img.shape

    top_left = [((width/2)/2)/2,0]
    top_right = [width-((width/2)/2)/2,0]
    bottom_left = [0,height]
    bottom_right = [width,height]

    pts1 = np.float32([top_left,top_right,bottom_left,bottom_right])
    pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

    matrix = cv2.getPerspectiveTransform(pts1,pts2)
    imgOut = cv2.warpPerspective(img, matrix,(width,height))

    for x in range(0,4):
        cv2.circle(img,(int(pts1[x][0]),int(pts1[x][1])),5,(0,0,255),cv2.FILLED)
    save_path = os.path.join(save_dir, "Birdview_" + file)
    cv2.imwrite(save_path, imgOut)
