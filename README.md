# Augmented Reality:
This augmented reality application uses OpenCV to overlay an image onto a live webcam feed by detecting keypoints and matching descriptors with the ORB algorithm and FLANN matcher. When enough matches are found, a homography matrix aligns the augmenting image with the input image's keypoints for a seamless overlay. The real-time output can be terminated with the 'Esc' key.

## Table of Content
  * [Interface](#interface)
  * [Overview](#overview)
  * [Installation](#installation)
  * [Future scope of project](#future-scope)
  


## Interface
![augment](https://github.com/Akbar-ds/Augmented-Reality/assets/172882659/16d9c6ce-8146-46ce-99b3-549b79478ed1)
![augment 1](https://github.com/Akbar-ds/Augmented-Reality/assets/172882659/bf4c0ebb-01cb-458e-abf9-a6e73a8180cd)
![augment 3](https://github.com/Akbar-ds/Augmented-Reality/assets/172882659/9eba6106-1353-4420-a217-ba924e19ef38)


## Overview
This augmented reality application uses OpenCV to overlay a predefined image onto a live webcam feed. ORB detects keypoints and computes descriptors, while FLANN finds matches. A homography matrix aligns the augmenting image with the input. The real-time augmented output can be terminated with the 'Esc' key.

## Motivation
The motivation behind this augmented reality application is to explore and demonstrate the potential of computer vision in creating interactive and immersive experiences. By leveraging feature detection, descriptor matching, and homography transformations, this project showcases how digital information can be seamlessly integrated into the real world.

## Installation
The Code is written in Python 3.10.0. If you don't have Python installed you can find it [here](https://www.python.org/downloads/). If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. To install the required packages and libraries, run this command in the project directory after [cloning](https://www.howtogeek.com/451360/how-to-clone-a-github-repository/) the repository:
```bash
pip install -r requirements.txt
```

## Future Scope

* Improved Feature Detection
* Mobile and AR Glasses Integration
* Multiple Image Recognition
* 3D Object Augmentation
