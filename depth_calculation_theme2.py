import numpy as np
import cv2
import time
import os
import csv
from matplotlib import pyplot as plt

# enter the model path
path_models = r"D:\Smarathon\Midas\\"

# Read Network
model_name = "model-f6b98070.onnx";  # MiDaS v2.1 Large

# Load the DNN model
model = cv2.dnn.readNet(path_models + model_name)

if (model.empty()):
    print("Could not load the neural network")


# Set backend and target to CUDA to use GPU
# model.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
# model.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)


def image_input(path):
    img = cv2.imread(path)

    imgHeight, imgWidth, channels = img.shape
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img, (300, 300))

    # start time to calculate FPS
    start = time.time()
    #
    blob = cv2.dnn.blobFromImage(img, 1 / 255., (384, 384), (123.675, 116.28, 103.53), True, False)

    # Set input to the model
    model.setInput(blob)
    # Make forward pass in model
    output = model.forward()

    output = output[0, :, :]
    # output = cv2.resize(output,(imgWidth,imgHeight))
    # output = cv2.resize(output, (640, 480))

    # Normalize the output
    output = cv2.normalize(output, None, 0, 1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
    # End time
    end = time.time()
    # calculate the FPS for current frame detection
    fps = 1 / (end - start)
    # Show FPS
    # cv2.putText(img, f"{fps:.2f} FPS", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 2)

    return output, img


def image_input_path(input_path):
    # Read in thr image
    img = cv2.imread(input_path)

    img_height, img_width, channels = img.shape
    img_inv = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    ret_, img = cv2.threshold(img_inv, 160, 255, cv2.THRESH_BINARY)

    # start time to calculate FPS
    start = time.time()
    #
    blob = cv2.dnn.blobFromImage(img, 1 / 255., (384, 384), (123.675, 116.28, 103.53), True, False)

    # Set input to the model
    model.setInput(blob)
    # Make forward pass in model
    output = model.forward()

    output = output[0, :, :]
    # output = cv2.resize(output,(img_width,img_height))
    # output = cv2.resize(output, (640, 480))

    # Normalize the output
    output = cv2.normalize(output, None, 0, 1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
    # End time
    end = time.time()
    # calculate the FPS for current frame detection
    # fps = 1 / (end - start)
    # Show FPS
    # cv2.putText(img, f"{fps:.2f} FPS", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 2)
    # cv2.putText(img, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 2)

    # output = (output * 255)

    return output


def depth_intensity(img_path):
    test = cv2.imread(img_path)
    # cv2.imshow('test', test)
    # cv2.waitKey(0)
    test = cv2.resize(test, (300, 300))
    test_arr = np.asarray(test)
    depth_int = np.average(test_arr)
    # average depth intensity  of the pothole which can be converted into required units
    return depth_int


def tresh_write(dir_path, output_dir):
    img_lst = os.listdir(dir_path)
    for i in range(0, len(img_lst)):
        img_path = dir_path + "\\" + img_lst[i]
        print(img_path)
        img = cv2.imread(img_path)
        img_inv = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        ret_, thresh = cv2.threshold(img_inv, 160, 255, cv2.THRESH_BINARY)
        output = cv2.resize(thresh, (300, 300))
        # output = image_input_path(img_path)
        os.chdir(output_dir)
        status = cv2.imwrite(f"{img_lst[i]}.jpg", output)
        print(f"{img_path} : {status}")


def intensity_dict(dir_path):
    img_lst = os.listdir(dir_path)
    print(img_lst)
    for i in range(0, len(img_lst)):
        img_path = dir_path + "\\" + img_lst[i]
        #print(img_path)
        depth_int = depth_intensity(img_path)
        k = [i+1,img_lst[i],depth_int]
        createCSV(k)

    # return dict_int
def output_write(dir_path, output_dir):
    img_lst = os.listdir(dir_path)
    for i in range(0, len(img_lst)):
        img_path = dir_path + "\\" + img_lst[i]
        print(img_path)
        output = image_input_path(img_path)
        os.chdir(output_dir)
        status = cv2.imwrite(f"{img_lst[i]}.jpg", output)
        #print(f"{img_path} : {status}")

# def csv_write(dictonary_of_intensities):
#     import csv
#
#     # data rows as dictionary objects
#     mydict = dictonary_of_intensities
#
#     # field names
#     fields = ['SNo', 'Name-of-Pothole', 'depth_intensity']
#
#     with open('EstimatedDepthIntensities.csv', 'w', newline='') as file:
#         writer = csv.DictWriter(file, fieldnames=fields)
#         writer.writeheader()
#         writer.writerows(mydict)

def createCSV(diffcsvList):
    if os.path.exists(r'C:\Users\Kranthi Kiran\Desktop\Smartathon-Theme2-Submission\Scene_2\EstimatedDepthIntensities.csv'):
        with open("EstimatedDepthIntensities.csv", "a+") as f:
            writer = csv.writer(f)
            writer.writerow(diffcsvList)
            f.close
    else:
        with open("EstimatedDepthIntensities.csv", "w") as f:
            writer = csv.writer(f)
            writer.writerow(['SNo', 'Name-of-Pothole', 'depth_intensity'])
            writer.writerow(diffcsvList)
            f.close


images_path = r"C:\Users\Kranthi Kiran\Desktop\Smartathon-Theme2-Submission\Scene_2\Scene2-Extracted-Potholes"
output_img_dir = r"C:\Users\Kranthi Kiran\Desktop\Smartathon-Theme2-Submission\Scene_2\Scene2-Depthimages"
converted_img_dir = r"C:\Users\Kranthi Kiran\Desktop\Smartathon-Theme2-Submission\Scene_2\Tresholded images"
path_of_csv = r'C:\Users\Kranthi Kiran\Desktop\Smartathon-Theme2-Submission\Scene_2\\'


tresh_write(images_path, converted_img_dir)
output_write(converted_img_dir, output_img_dir)
directory = path_of_csv
os.chdir(directory)
#intensity_dict(output_img_dir)
#csv_write(k)
#print(type(k))
#print(k)

# #np.mean(test1_arr))



