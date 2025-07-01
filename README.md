#Mars_Terrain – Gazebo Simulation Environment for Safe Spot Detection

This repository contains a custom-built Martian terrain simulation environment developed using Gazebo, ROS 2, and the ros-gz bridge. It is designed for testing and training autonomous drone models to perform safe landing spot detection and navigation in Martian-like conditions.

#Features

- Custom Martian terrain world (`.sdf`) modeled with rocks, slopes, and varied elevation.
- Integrated with ROS 2 Humble and Gazebo Fortress.
- Supports safe spot detection, landing, hovering, and takeoff missions.
- Includes required sensors such as:
  - Depth Camera
  - IMU
  - Light Source
  - Gravity settings
- Supports ros-gz bridge for communication between ROS 2 and Gazebo.

#Requirements

- ROS 2 Humble
- Gazebo Fortress (Ignition Gazebo)
- ros-gz bridge
- colcon (for building ROS 2 packages)
- Python 3.8+

#How to Launch the Simulation

1. Clone the Repository:
    - git clone https://github.com/s-e-j-a-l/Mars_Terrain.git
    - cd Mars_Terrain

2. Build and Source Your Workspace:
    - colcon build
    - source install/setup.bash

3. Launch the Mars Terrain World:
    - ros2 launch launch/bridge.launch.py
 
#Use Cases

This simulation environment is designed for:
Training RL models (e.g., Soft Actor-Critic) for landing decision-making.
Testing safe spot detection using depth sensing and terrain analysis.
Developing autonomous Martian exploration drones.






