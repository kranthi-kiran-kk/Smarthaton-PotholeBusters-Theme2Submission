import cv2
import csv
import os

def area(path):
    imgOut = cv2.imread(path)
    gray = cv2.cvtColor(imgOut, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (3, 3), 0)
    edges = cv2.Canny(blurred, 150, 200) # Apply Canny edge detection
    thresh = cv2.adaptiveThreshold(edges,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 35, 2)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    dilate = cv2.dilate(thresh, kernel, iterations=1)

    contours, hierarchy = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(imgOut, contours, -1, (0,255,0), 3)

    # Area technique 1
    pothole_area = 0
    for contour in contours:
        pothole_area += cv2.contourArea(contour)
    # print("Summing contours method:")
    # print("Area of pothole:", pothole_area)

    # # Area technique 2
    # min_area_threshold = 1000
    # print("Minimum Threshold method:")
    # for contour in contours:
    #     area = cv2.contourArea(contour)
    #     if area > min_area_threshold:
    #         pothole_area = area
    #         break

    area_sqcm = (pothole_area * 0.02645)
    area_sqft = (area_sqcm * 0.00107)
    # print("Area of pothole (Pixels):", pothole_area)
    # print("Area of pothole (sqcm):", area_sqcm)
    # print("Area of pothole (sqft):", area_sqft)
    # # cv2.imshow("Blur", blurred)
    # cv2.imshow("Edged", edges)
    # cv2.imshow("Thresh", thresh)
    # cv2.imshow("Gray", gray)
    # cv2.imshow("Output", imgOut)
    
    # key = cv2.waitKey(0)
    # if key == ord('k'):
    #     cv2.destroyAllWindows()

    return area_sqft

def area_diff(path1, path2):
    x = abs(area(path2) - area(path1))
    return x

def createCSV(diffcsvList):
    if os.path.exists(r'C:\Users\vishwebh\Desktop\Smartathon\area_diff.csv'):
        with open("area_diff.csv", "a+") as f:
            writer = csv.writer(f)
            writer.writerow(diffcsvList)
            f.close
    else:
        with open("area_diff.csv", "w") as f:
            writer = csv.writer(f)
            writer.writerow(["Sl. no.", "File1", "File2", "PotholeArea file1", "PotholeArea file2", "Difference"])
            writer.writerow(diffcsvList)
            f.close

def createCSV_(diffcsvList_):
    if os.path.exists(r'C:\Users\vishwebh\Desktop\Smartathon\area_pothole.csv'):
        with open("area_pothole.csv", "a+") as f:
            writer = csv.writer(f)
            writer.writerow(diffcsvList_)
            f.close
    else:
        with open("area_pothole.csv", "w") as f:
            writer = csv.writer(f)
            writer.writerow(["Sl. no.", "Image File", "PotholeArea"])
            writer.writerow(diffcsvList_)
            f.close


parent = r'C:\Users\vishwebh\Desktop\Smartathon\top_view_extracted'
files = os.listdir(parent)
print(len(files))
print(range(len(files)))

# for file in files:
#     for i in range(len(files)-1):
#         path1 = os.path.join(parent,files[i])
#         path2 = os.path.join(parent,files[i+1])
#         diffcsvList = [str(i+1),str(files[i]),str(files[i+1]), str(area(path1)), str(area(path2)), str(area_diff(path1,path2))]
#         createCSV(diffcsvList)  

for i in range(len(files)-1):
    path1 = os.path.join(parent,files[i])
    path2 = os.path.join(parent,files[i+1])
    diffcsvList = [str(i+1),str(files[i]),str(files[i+1]), str(area(path1)), str(area(path2)), str(area_diff(path1,path2))]
    createCSV(diffcsvList)

for i in range(len(files)-1):
    # print(os.path.join(parent, files[i]))
    path = os.path.join(parent, files[i])
    diffcsvList_ = [str(i+1), str(files[i]), str(area(path))]
    createCSV_(diffcsvList_)


    # areadiff1 = area_diff(path1, path2)

    # print("Area difference: ", areadiff1)
