# Augmented Reality:
This augmented reality application uses OpenCV to overlay an image onto a live webcam feed by detecting keypoints and matching descriptors with the ORB algorithm and FLANN matcher. When enough matches are found, a homography matrix aligns the augmenting image with the input image's keypoints for a seamless overlay. 

## Table of Content
  * [Interface](#interface)
  * [Overview](#overview)
  * [Installation](#installation)
  * [Future scope of project](#future-scope)
  


## Interface

![aug1](https://github.com/Akbar-ds/Augmented-Reality/assets/172882659/819aae60-243b-45ae-9e15-91c80bdaf396)
![aug2](https://github.com/Akbar-ds/Augmented-Reality/assets/172882659/3dcb0838-230b-4ecc-805a-a48c0541db7c)
![aug3](https://github.com/Akbar-ds/Augmented-Reality/assets/172882659/6387f31b-b9a5-4510-a040-8c17510bc3e1)
![aug4](https://github.com/Akbar-ds/Augmented-Reality/assets/172882659/91fe1893-ece0-48da-9876-1a5adc0d057f)

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
