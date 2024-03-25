[English](./README.md) | 简体中文

# 功能介绍

获取摄像头发布的图片并保存在本地，分为障碍物检测数据集以及赛道检测数据集，赛道检测数据集取图片最下方的224行

# 使用方法

## 准备工作

具备真实的机器人或机器人仿真模块，包括相机及RDK套件，并且能够正常运行。

## 安装功能包

**1.安装功能包**

启动机器人后，通过终端SSH或者VNC连接机器人，点击本页面右上方的“一键部署”按钮，复制如下命令在RDK的系统上运行，完成相关Node的安装。

```bash
sudo apt update
sudo apt install -y tros-racing-image-collect
```

**2.运行MIPI相机发布bgr8图像**

```shell
source /opt/tros/local_setup.bash
ros2 launch mipi_cam mipi_cam_640x480_bgr8.launch.py
```

**3.运行数据集采集功能**

```shell
source /opt/tros/local_setup.bash
ros2 run racing_image_collect racing_image_collect
```


# 接口说明

## 话题

### Sub话题
| 名称                          | 消息类型                                                     | 说明                                                   |
| ----------------------------- | ------------------------------------------------------------ | ------------------------------------------------------ |
| /image_raw                    | sensor_msgs/msg/Image                                    | 接收相机发布的图片消息的名称               |

## 参数

| 参数名                | 类型        | 说明    |
| --------------------- | ----------- | --------------------------------------------------------- |
| sub_img_topic       | string |     接收的图片话题名称，请根据实际接收到的话题名称配置，默认值为/image_raw |
| track_img_folder   | string | 存放赛道检测数据集的路径，默认值为./track_image |
| obstacle_img_folder   | string | 存放障碍物检测数据集的路径，默认值为./obstacle_image |
| fps   | float | 保存图片的速率，默认值为2.0 |
