# Pothole Detection and Severity Classification using Computer Vision 


## The model can perform the following tasks: 🔍🛠️🚧

**a)** Detect potholes from Video and Image input with bounding boxes using the custom trained Yolov7 Object detection model. 

**b)** Crop and save the region of pothole from images as new image which can be used for further processing and analytics. 

**c)** Perform image processing and perspective transformation to enable improved contouring for area estimation. 

**d)** Use midas model (Robust Monocular Depth Estimation) for depth estimation of potholes. The value returned corresponds to the mean depth intensity which correlates to the Severity of the pothole in the image. 

[![Flowchart-removebg-preview.png](https://i.postimg.cc/QdBqsCn7/Flowchart-removebg-preview.png)](https://postimg.cc/ZWSNxbmY) 


## Instructions to use the model: 🔍🛠️🚧

> We will be running the Pothole Detection code that employs the Yolov7 model for detection on *Google Colab*. Upon obtaining the video or image result, the same can be downloaded and the further image processing can be performed on local machine using the instructions provided below. 
> Although, you are free to continue on Google colab for the Area estimation and Depth estimation for which you will have to follow the package installation procedures and other changes accordingly.

### *Instructions to run Pothole Detection Code on Google Colab:* 

1. Open the '.ipynb' in google colab, change path for the input video either by mounting your Google drive which has the video or upon directly uploading the test video to the Google colab workspace. Incase you do not want to mount Google drive you can skip that line of code in the '.ipynb' notebook. 
2. Upload the 'best.pt' from this repository onto your Google colab workspace and use it as weight for detection by changing the path in the code.
3. Once the detection is done, we can download the output video along with the labels folder from runs folder in Yolov7 directory from Google Colab Workspace. 

> In case you want to use your own image dataset and train the Yolo model: Use any annotation tools such as Label-Studio for annotations and render the output of your annotations in the Yolo format. Train the model on your dataset and use the weights that are generated post training for testing.

### *Using Local Machine for Area Estimation and Depth Estimation of Potholes from Images:*

Packages to be installed:

1. OpenCV
2. Numpy

**a)** 'pothole_extration.py' - for extracting region of pothole from frames obtained post-detection.

**b)** 'bird_new.py' - for applying perspective transformation (warp perspective/Bird view/Top view) to all the pothole regions and saving the top views of potholes in a new folder.

**c)** 'postwarp.py' - for *area estimation and CSV creation*.



### *Youtube Video (Model Demo)* - https://youtu.be/MO6h2W1zYjM


## Results: 🔍🛠️🚧

### Detection:

[![image.png](https://i.postimg.cc/5trWPnkz/image.png)](https://postimg.cc/bG15rHPY) [![image.png](https://i.postimg.cc/BbMggwm9/image.png)](https://postimg.cc/dZZrQnM4)

### Cropped Pothole Images:

[![image.png](https://i.postimg.cc/3wtmzDgm/image.png)](https://postimg.cc/HJ7rynvk) [![image.png](https://i.postimg.cc/yxZc4vHt/image.png)](https://postimg.cc/V0zdX95W)

### Warp Perspective (Top View):

[![image.png](https://i.postimg.cc/Y94mYbh0/image.png)](https://postimg.cc/Ppjxkbbn) [![image.png](https://i.postimg.cc/0Qmy93zY/image.png)](https://postimg.cc/CBhgNcH5)

### CSV with Area result: 

> Area is returned in pixels, sqcm and sqft.
> CSV contains Area rendered in sqft.

[![image.png](https://i.postimg.cc/WpXQh80g/image.png)](https://postimg.cc/0rKt4pWy)





