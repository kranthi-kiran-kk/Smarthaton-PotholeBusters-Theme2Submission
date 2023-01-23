import cv2
import numpy as np
import os
# directory = (r'C:\Users\vishwebh\Desktop\Smartathon\extracted_frames\Frame-1-1.png')
# img = cv2.imread(directory)
# height, width, _ = img.shape
# top_left = [((width/2)/2)/2,0]
# top_right = [width-((width/2)/2)/2,0]
# bottom_left = [0,height]
# bottom_right = [width,height]
# pts1 = np.float32([top_left,top_right,bottom_left,bottom_right])
# # Sample2.png
# # pts1 = np.float32([[33,82],[587,82],[33,253],[587,253]])
# pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

# matrix = cv2.getPerspectiveTransform(pts1,pts2)
# imgOut = cv2.warpPerspective(img, matrix,(width,height))

# for x in range(0,4):
#     cv2.circle(img,(int(pts1[x][0]),int(pts1[x][1])),5,(0,0,255),cv2.FILLED)

# cv2.imshow('Original',img)
# cv2.imshow('Output', imgOut)

# key = cv2.waitKey(0)

# if key == ord('k'):
#     cv2.destroyAllWindows()


directory = r'C:\Users\vishwebh\Desktop\Smartathon\extracted_frames'
save_dir = r'C:\Users\vishwebh\Desktop\Smartathon\top_view_extracted'
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
