# 🤖 RRPR Robot Arm (ROS2)

## 📌 Project Overview

This project implements a **RRPR (Revolute-Revolute-Prismatic-Revolute)** robotic arm based on **ROS2 (Humble)**.
It includes complete **URDF modeling, joint control, and RViz visualization**, and demonstrates open-loop kinematics and motion control.

---

## 🎯 Features

* ✔ RRPR robotic arm structure modeling (URDF)
* ✔ Real-time joint control via `/joint_states`
* ✔ RViz2 visualization
* ✔ Prismatic joint (linear motion) support
* ✔ Modular ROS2 architecture (easy to extend)
* ✔ Open-loop control demonstration

---

## 🛠️ Tech Stack

* ROS2 (Humble)
* Python (rclpy)
* URDF (Robot Description)
* RViz2

---

## 📁 Project Structure

```text
rrpr_ws/
├── src/
│   ├── rrpr_description/   # URDF model
│   │   └── urdf/
│   │       └── rrpr.urdf
│   ├── rrpr_controller/    # Joint controller
│   │   └── controller.py
│   └── ...
├── README.md
```

---

## 🚀 How to Run

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Zhao-123-GIT/rrpr-ros2-robot.git
cd rrpr-ros2-robot
```

---

### 2️⃣ Build workspace

```bash
cd rrpr_ws
colcon build
source install/setup.bash
```

---

### 3️⃣ Launch robot model (RViz)

```bash
ros2 launch urdf_tutorial display.launch.py model:=src/rrpr_description/urdf/rrpr.urdf
```

---

### 4️⃣ Run controller

```bash
ros2 run rrpr_controller controller
```

---

## 🎥 Demo

> (Add your demo video or GIF here)

---

## 📊 Functionality Demonstration

* Joint rotation (R joints)
* Linear extension (P joint)
* Continuous motion control
* Real-time visualization in RViz

---

## 🚧 Future Work

* [ ] Forward & Inverse Kinematics
* [ ] Trajectory Planning (MoveIt2)
* [ ] MQTT / Remote Control Integration
* [ ] Unity / VR Visualization
* [ ] Closed-loop control (feedback)

---

## 👤 Author

**Yiran Zhao**

* ROS2 Developer
* Robotics / AI / Simulation

---

## ⭐ Highlights (for Resume)

* Designed and implemented a **ROS2-based robotic arm system**
* Built complete **URDF model and TF tree**
* Developed **real-time joint control node**
* Achieved **dynamic visualization and control in RViz**
