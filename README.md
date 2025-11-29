# 🚗 Self-Driving Car Using Behavioral Cloning (NVIDIA End-to-End Model)

A deep learning based **autonomous driving system** built using the **NVIDIA behavioral cloning architecture**, trained on camera images captured from a car simulator.

This project uses **end-to-end CNN learning** to predict the **steering angle** directly from raw images — just like modern self-driving car systems.

---

<img width="1024" height="767" alt="image" src="https://github.com/user-attachments/assets/dadc7268-3772-41e9-98e5-b00d8a6421b4" />

<img width="624" height="393" alt="lake_track" src="https://github.com/user-attachments/assets/92c29eb4-5da5-401c-bf37-39002f1bffad" />

---

## ⭐ Features
- End-to-End CNN model (NVIDIA architecture)
- Predicts real-time steering angle from camera feed
- Data augmentation (shadow, brightness, flip, shift)
- Image preprocessing (crop, resize, normalize)
- Training pipeline with Keras/TensorFlow
- Supports Udacity Self-Driving Car Simulator
- Live inference & steering control via SocketIO

---

## 🧠 Algorithm Overview (Behavioral Cloning)

This project trains a deep neural network to **clone** the behavior of a human driver.

### Steps:
1. **Collect driving data** from simulator  
2. **Preprocess images**  
3. **Augment for robustness**  
4. **Train NVIDIA CNN model**  
5. **Predict steering angle**  
6. **Drive autonomously**

---



---

## 🛠️ Tech Stack

- **Python**
- **TensorFlow / Keras**
- **OpenCV**
- **NumPy**
- **Pandas**
- **SocketIO**
- **Udacity Self-Driving Car Simulator**

---

## 📁 Dataset

Collected from:
- Udacity Self-Driving Car Simulator (Windows/Linux/Mac)

Contents:
- `IMG/` → camera images  
- `driving_log.csv` → steering, throttle, brake, and speed

---

## 📦 Installation

```bash
git clone https://github.com/mdShakil2004/CNN-based-self-driving-car.git
cd CNN-based-self-driving-car
download simulator from : https://shorturl.at/1v2KB  # and Scroll up 
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
Train the Model
python model.py -d data

Open Udacity simulator → Autonomous Mode → Enjoy the ride 🚗💨

🎮 Run Autonomous Mode
python drive.py model.h5

## 🏗️ Model Architecture (NVIDIA CNN)




