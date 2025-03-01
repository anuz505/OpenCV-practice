# Finger Counter

This is a practice project that uses OpenCV and a custom hand tracking module to count the number of fingers shown to the camera. The project displays the count of fingers on the screen.

## Features

- Real-time hand tracking using OpenCV.
- Detection and counting of fingers.
- Display of frames per second (FPS) on the screen.

## Requirements

- Python 3.x
- OpenCV
- Custom hand tracking module (`handtrackingmodule`)

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/anuz505/OpenCV-practice.git
   cd finger-counter
   ```

2. Install the required packages:

   ```sh
   pip install opencv-python
   ```

3. Ensure that the [handtrackingmodule] is available in the `modules` directory.

## Usage

1. Place your images in the [images] directory.
2. Run the [fingercounter.py] script:
   ```sh
   python fingercounter.py
   ```

## Code Explanation

The main script [fingercounter.py] performs the following tasks:

1. Imports necessary libraries and modules.
2. Initializes the video capture from the webcam.
3. Loads images from the [images] directory.
4. Initializes the hand detector from the custom [handtrackingmodule].
5. Continuously captures frames from the webcam and processes them to detect hands and count fingers.
6. Displays the count of fingers
7. Shows the FPS on the screen.

Landmarks
The hand tracking module uses landmarks to identify key points on the hand. These landmarks are used to determine the position and orientation of the fingers. Below is an image from MediaPipe showing the landmarks on a hand:

<img alt="Hand Landmarks" src="https://ai.google.dev/static/mediapipe/images/solutions/hand-landmarks.png">

## Example

When you run the script, it will open a window showing the webcam feed. The number of fingers detected will be displayed on the screen.
