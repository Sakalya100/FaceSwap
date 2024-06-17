---
title: FaceSwap
emoji: 🚀
colorFrom: blue
colorTo: purple
sdk: streamlit
sdk_version: 1.35.0
app_file: app.py
pinned: false
---

# FaceSwap
An OpenCV Based application that allows you to swap faces between 2 images with OpenCV and dlib.

# Try it out!

You can try out the Application [Here](https://huggingface.co/spaces/Sakalya122/FaceSwap)


## Overview
FaceSwap is an application that leverages computer vision techniques to swap faces between images. It uses OpenCV for image processing and Dlib for face detection and landmark prediction.

## Features
- **Face Detection**: Accurately detects faces in the source and target images using Dlib.
- **Landmark Prediction**: Identifies key facial landmarks for precise face alignment and swapping.
- **Face Swapping**: Seamlessly swaps faces between images using advanced image processing techniques.
- **Color Correction**: Ensures the swapped face blends naturally with the target image.


## How It Works
1. **Face Detection**: Dlib is used to detect faces in both the source and target images.
2. **Landmark Detection**: Facial landmarks are identified to facilitate accurate alignment.
3. **Face Alignment**: The source face is aligned to match the orientation and size of the target face.
4. **Seamless Cloning**: The aligned face is seamlessly cloned onto the target image using OpenCV's seamlessClone function.


   
## Installation

### Get Started 
```sh
python main.py --src imgs/test6.jpg --dst imgs/test7.jpg --out results/output6_7.jpg --correct_color
```

| Source | Destination | Result |
| --- | --- | --- |
|![](imgs/test6.jpg) | ![](imgs/test7.jpg) | ![](results/output6_7.jpg) |

```sh
python main.py --src imgs/test6.jpg --dst imgs/test7.jpg --out results/output6_7_2d.jpg --correct_color --warp_2d
```

| Source | Destination | Result |
| --- | --- | --- |
|![](imgs/test6.jpg) | ![](imgs/test7.jpg) | ![](results/output6_7_2d.jpg) |

### Requirements
* `pip install -r requirements.txt`
* OpenCV 3: `conda install opencv` (If you have conda/anaconda)

Note: See [requirements.txt](requirements.txt) for more details.
### Git Clone
```sh
git clone https://github.com/wuhuikai/FaceSwap.git
```
### Swap Your Face
```sh
python main.py ...
```
Note: Run **python main.py -h** for more details.


### Real-time camera
```sh
python main_video.py --src_img imgs/test7.jpg --show --correct_color --save_path {*.avi}
```
### Video
```sh
python main_video.py --src_img imgs/test7.jpg --video_path {video_path} --show --correct_color --save_path {*.avi}
```

### Run Locally on Streamlit
To run this project locally, follow these steps:

1. **Clone the Repository**
    ```bash
    git clone https://github.com/yourusername/FaceSwap.git
    cd FaceSwap
    ```

2. **Install Dependencies**
    Make sure you have the following dependencies installed:

    - Python 3.7+
    - OpenCV
    - Dlib

    You can use the provided `requirements.txt` file to install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. **Install Dlib**
    In case the dblib installation is not working through `requirements.txt`, download the dblib wheel file from [here](https://github.com/sachadee/Dlib)
   Ensure you have the Dlib wheel file in your project directory:

    ```bash
    pip install dlib-19.24.1-cp311-cp311-win_amd64.whl
    ```

## Usage
To use the FaceSwap application, follow these steps:

1. **Run the Application**
    ```bash
    streamlit run app.py
    ```

2. **Upload Images**
    - Upload the source image (the face to be swapped).
    - Upload the target image (the image where the face will be swapped).

3. **View and Download the Result**
    - The swapped face will be displayed on the right.
    - Use the download button to save the output image.


## More Results
| From | To |
| --- | --- |
| ![](imgs/test4.jpg) | ![](results/output6_4.jpg) |
| ![](imgs/test3.jpg) | ![](results/output6_3.jpg) |
| ![](imgs/test2.jpg) | ![](results/output6_2_2d.jpg) |
| ![](imgs/test1.jpg) | ![](results/output6_1.jpg) |
| ![](imgs/test4.jpg) | ![](results/output7_4.jpg) |

## Author
[<img src="https://github.com/Sakalya100.png" width="60px;"/>](https://github.com/Sakalya100)

