English| [简体中文](./README_cn.md)

# Function Introduction

Get the images published by the camera and save them locally, divided into obstacle detection dataset and track detection dataset. The track detection dataset takes the bottom 224 rows of the image.

# How to Use

## Preparation

Have a real robot or a robot simulation module, including a camera and RDK suite, and ensure they can operate normally.

## Install Package

**1. Install Package**

After starting the robot, connect to the robot via SSH or VNC in the terminal, click the "One-click Deployment" button on this page's upper right corner, copy and run the following commands on the RDK system to complete the installation of related Nodes.

```bash
sudo apt update
sudo apt install -y tros-racing-image-collect
```

**2. Run MIPI camera to publish bgr8 image**

```shell
source /opt/tros/local_setup.bash
ros2 launch mipi_cam mipi_cam_640x480_bgr8.launch.py
```

**3. Run dataset collection function**

```shell
source /opt/tros/local_setup.bash
ros2 run racing_image_collect racing_image_collect
```

# Interface Specification

## Topics

### Sub Topics
| Name                          | Message Type                                                | Description                                                  |
| ----------------------------- | ----------------------------------------------------------- | ------------------------------------------------------------ |
| /image_raw                    | sensor_msgs/msg/Image                                       | Name of the topic that receives the image messages published by the camera |

## Parameters

| Parameter Name          | Type   | Description                                                                                     |
| ----------------------- | ------ | --------------------------------------------------------------------------------------------- |
| sub_img_topic          | string | Name of the image topic received, please configure according to the actual received topic name, default value is /image_raw || track_img_folder   | string | Path to store the track detection dataset, default value is ./track_image |
| obstacle_img_folder   | string | Path to store the obstacle detection dataset, default value is ./obstacle_image |
| fps   | float | Frame per second for saving images, default value is 2.0 |