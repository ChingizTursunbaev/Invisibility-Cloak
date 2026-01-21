# 🧙‍♂️ OpenCV Invisibility Cloak

> A real-time computer vision application that creates an "Invisibility Cloak" effect using color segmentation and background subtraction.

<<<<<<< Updated upstream
##  Overview
This project mimics the famous "Invisibility Cloak" from Harry Potter. It works by capturing a static background frame and then processing the live video feed to detect a specific color (currently **Red**). When the target color is detected, the program replaces those pixels with the saved background pixels, creating the illusion of transparency.

##  Technical Concepts
=======
## 📝 Overview
This project mimics the famous "Invisibility Cloak" from Harry Potter. It works by capturing a static background frame and then processing the live video feed to detect a specific color (currently **Red**). When the target color is detected, the program replaces those pixels with the saved background pixels, creating the illusion of transparency.

## 🔧 Technical Concepts
>>>>>>> Stashed changes
This project demonstrates proficiency in several key Computer Vision concepts using **OpenCV**:
* **Color Space Conversion:** Converting BGR (Blue-Green-Red) frames to HSV (Hue-Saturation-Value) for robust color detection that is less sensitive to lighting changes.
* **Image Segmentation:** Creating binary masks to separate the foreground object (the cloak) from the rest of the scene.
* **Morphological Operations:** (Optional) Refining the mask to remove noise and smooth edges.
* **Bitwise Arithmetic:** Using `bitwise_and` and `add` operations to seamlessly blend the background and foreground layers.

<<<<<<< Updated upstream
## Prerequisites
=======
## 🛠️ Prerequisites
>>>>>>> Stashed changes
* Python 3.x
* OpenCV (`opencv-python`)
* NumPy

<<<<<<< Updated upstream
##  Installation
1.  **Clone the repository:**
    ```bash
    git clone https://github.com/ChingizTursunbaev/Invisibility-Cloak.git
    cd Invisibility-Cloak
=======
## 📦 Installation
1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/invisible-cloak.git](https://github.com/your-username/invisible-cloak.git)
    cd invisible-cloak
>>>>>>> Stashed changes
    ```
2.  **Install dependencies:**
    ```bash
    pip install opencv-python numpy
    ```

## 🚀 How to Run
1.  Connect your webcam (ensure no other apps like Zoom/Teams are using it).
2.  Run the script:
    ```bash
    python main.py
    ```
3.  **Step away from the frame immediately!** The program captures the background for the first 30 frames (approx. 1-2 seconds) to establish the "empty room" reference.
4.  Once the video feed appears, re-enter the frame holding your **Red** object (cloth, towel, etc.).
5.  Watch as the object becomes "invisible."
6.  Press **`q`** to quit the application.

<<<<<<< Updated upstream
## Configuration
=======
## ⚙️ Configuration
>>>>>>> Stashed changes
You can adjust the color sensitivity in `main.py` if your object isn't being detected perfectly.
* **Target Color:** Currently set to detect **Red**.
* **Hue Ranges:**
    * Lower Red: `H: 0-10`
    * Upper Red: `H: 170-180`

<<<<<<< Updated upstream
## Contributing
=======
## 🤝 Contributing
>>>>>>> Stashed changes
Feel free to fork this project and submit pull requests. Future improvements could include:
* Adding a trackbar to adjust color sensitivity in real-time.
* Implementing automatic background updates to handle lighting changes.

<<<<<<< Updated upstream
## License
[MIT](https://choosealicense.com/licenses/mit/)
=======
## 📜 License
[MIT](https://choosealicense.com/licenses/mit/)
>>>>>>> Stashed changes
