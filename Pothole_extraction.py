import os
import cv2
import numpy as np
import math

# Scene1
path_of_predicted_video = r"Path to video (Potholes Detected) - Scene1-Predicted.mov"
# path_of_original_video = r'Path to original video (potholes undetected) input.mp4'
path_of_labels = r"Path to labels (Scene 1)"
path_of_images = r"Path to scene 1 frames"
path_of_extraction = r"Path to scene 1 extracted frames (pothole region extracted)"


# Scene2
# path_of_predicted_video = r"Path to video (Potholes Detected) - Scene1-Predicted.mov"
# path_of_original_video = r'Path to original video (potholes undetected) input.mp4'
# path_of_labels = r"Path to labels (Scene 2)"
# path_of_images = r"Path to scene 2 frames"
# path_of_extraction = r"Path to scene 2 extracted frames (pothole region extracted)"


# returns list of frame labels
def frame_label(path_of_predicted_labels):
    frame_with_label = os.listdir(path_of_predicted_labels)
    frame_lst = []
    # print(frame_with_label)
    for ele in frame_with_label:
        m = ((ele.split("_")[1]).split(".")[0])
        frame_lst.append(int(m))
    return sorted(frame_lst)


# returns the list of labels with potholes
def labels_read(path_of_predicted_labels):
    frame_with_label = os.listdir(path_of_predicted_labels)
    return frame_with_label


# shows the required freame
def show_frame(videopath, frame_number, wait_time):
    cap = cv2.VideoCapture(videopath)
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number - 1)
    # cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)  # float `width`
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)  # float `height
    # print(width, height)
    res, frame = cap.read()
    line = "Frame: " + str(frame_number)
    font = cv2.FONT_HERSHEY_PLAIN
    cv2.putText(frame, str(line), (20, 40), font, 2, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.imshow('frame', frame);
    cv2.waitKey(wait_time)


# calculates the depth and width of frame
def w_h(videopath):
    cap = cv2.VideoCapture(videopath)
    cap.set(cv2.CAP_PROP_POS_FRAMES, 1)
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)  # float `width`
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)  # float `height
    return width, height


# reads the text files with labels

def read_labels(file, path_of_labels_folder):
    filepath = path_of_labels_folder + file
    bbox = []
    with open(filepath, 'r') as fp:
        lines = len(fp.readlines())
        # print('Total Number of lines:', lines)
    with open(filepath, 'r') as fp:
        temp = fp.read().splitlines()
    for i in range(0, lines):
        content = temp[i].split(" ")
        content = [float(j) for j in content]
        bbox.append(content)
    return bbox


# to extract the potholes

def pothole_extracton(img_path, x, y, h, w, path_to_save, name):
    img = cv2.imread(img_path)
    if x < 0:
        x = 0
    if y < 0:
        y = 0
    crop_img = img[y:y + h, x:x + w]
    print(x, y, img.shape, crop_img.shape, w, h)
    directory = path_to_save
    os.chdir(directory)
    cv2.imwrite(name + ".png", crop_img)


# to show video along with frames
def show_video_with_frames(path_of_video):
    video = cv2.VideoCapture(path_of_video)
    while video.isOpened():
        ret, frame = video.read()
        line = "Frame-" + str(video.get(cv2.CAP_PROP_POS_FRAMES))

        if ret:
            font = cv2.FONT_HERSHEY_PLAIN
            cv2.putText(frame, str(line), (20, 40),
                        font, 2, (255, 255, 255), 2, cv2.LINE_AA)

            cv2.imshow('Frame', frame)
            # cv2.waitKey(0)

            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

        else:
            break

    video.release()

    # Closes all the frames
    cv2.destroyAllWindows()


# To save frames from the video
def save_frames(path_of_video):
    video = cv2.VideoCapture(path_of_video)
    while video.isOpened():
        ret, frame = video.read()
        line = "Frame-" + str(video.get(cv2.CAP_PROP_POS_FRAMES))

        if ret:
            font = cv2.FONT_HERSHEY_PLAIN
            cv2.putText(frame, str(line), (20, 40),
                        font, 2, (255, 255, 255), 2, cv2.LINE_AA)

            directory = path_of_images
            os.chdir(directory)
            cv2.imwrite(line + ".png", frame)

        else:
            break

    video.release()

    # Closes all the frames
    cv2.destroyAllWindows()


# show_video_with_frames(path_of_predicted_video)
save_frames(path_of_predicted_video)

# Making a dictionary of frames and corresponding potholes

frame_width, frame_height = w_h(path_of_predicted_video)

files = labels_read(path_of_labels)
frame_with_labels = {}
for file in files:
    m = int(((file.split("_")[1]).split(".")[0]))
    contents = read_labels(file, path_of_labels)
    frame_with_labels[m] = contents

k = sorted(list(frame_with_labels.keys()))
print(k)
for i in range(0, len(k)):
    img_path = path_of_images
    img_path = img_path + "\\" + "Frame-" + str(k[i]) + ".0.png"
    for j in range(0, len(frame_with_labels[k[i]])):
        print(k[i])
        c1 = frame_with_labels[k[i]][j]
        print(c1)
        x_c = int(c1[1] * frame_width)
        y_c = int(c1[2] * frame_height)
        h = int(c1[4] * frame_height)
        w = int(c1[3] * frame_width)
        x = int(x_c - (w / 2))
        y = int(y_c - (h / 2))
        name = "Frame-" + str(k[i]) + "-" + str(j + 1)
        print(x_c,y_c)

        pothole_extracton(img_path, x, y, h, w, path_of_extraction, name)
