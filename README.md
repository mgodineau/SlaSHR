 SlaSHR Project

1. [State of the art](#state)
2. [Installation reports](#done)


### State of the art <a name="state"></a>:

Here is the state of the art we manage to do of existing open source VI-SLAM algorithms we found.

<img src="doc/State of the art SLAM-VI_Page_1.png">
<img src="doc/State of the art SLAM-VI_Page_2.png">

### Installation reports <a name="done"></a>:

We will now review what turned out to be the main part of your project, dealing with the installation of the differents solutions. Theses repports are here to help you get through the installation if you have problems.

## [ORB SLAM 3](https://github.com/zhaozhongch/orbslam3_ros)

- Installation of [ROS wrapper](https://github.com/thien94/orb_slam3_ros_wrapper).
You need to make sure orbslam3 dependencies are installed first.
- Get the ORB SLAM 3 yaml files about cameras in *[ORBSLAM3_clone_path]/Examples/[camera_type]/RealSense_D435i.yaml* and */RealSense_T265.yaml.*
- Copy the files in *[...]/catkin_ws/src/orb_slam3_ros_wrapper/config*
- Modify launchfiles *(orb_slam3_ros_wrapper/launch)* according to the case you want : update the topics according to those published by the camera feed of the rosbag.

(Exemple for the D435i with IMU : we get the topics published for the image and IMU data (with ros commands), and we specify the path in the launchfile :
```json
>      <remap from="/camera/image_raw"         to="/camera/color/image_raw"/>
        <remap from="/imu"                      to="/camera/imu"/>
```
)
- Modify .rviz files *(orb_slam3_ros_wrapper/config)* to enter the right topic of image feed.

- WANRNING : IMU data of D435i are sperated in two topics (gyroscope and accelerometer). ORB SLAM 3 only need one to run. You can regroup them while reccording with a library like Realsens for ROS : 
```
roslaunch realsense2_camera rs_camera.launch unite_imu_method:=linear_interpolation
```
see [Realsens](https://github.com/IntelRealSense/realsense-ros/tree/ros1-legacy)
It require to record the datas with intel library and not Intel Realsens Viewer.

- ORB SLAM 3 and Rviz interface launch with this command : 
```
roslaunch orb_slam3_ros_wrapper [launch_file].launch
```
- You just need to open a new terminal to play the .bag camera flow, or record the flow with : 
```
rosbag play [path_to_rosbag_file]
```
or
```
roslaunch realsense2_camera rs_camera.launch unite_imu_method:=linear_interpolation
```

- We can then subscribe to the output topics of ORB SLAM 3 and save them to a .bag to use them later. To use evo for exemple, you need to record theses topics in particular : 
```
rosbag record -O [dest_file_name]  /initialpose /orb_slam3/camera_pose /tf
```

## [Kimera](https://github.com/MIT-SPARK/Kimera)

We had many issues installing Kimera. 

- install ROS wrapper for Kimera from [here](https://github.com/MIT-SPARK/Kimera-VIO-ROS)
- have a clean installation of ROS following [this](https://github.com/MIT-SPARK/Kimera-VIO-ROS/blob/master/docs/ros_installation.md)
- install ROS dependencie [*mesh_rviz_plugins*](https://github.com/ToniRV/mesh_rviz_plugins) in a catskin workspace
- Make sure to execute all commands to install all the dependencies.
- Follow the instructions to install ROS wrapper of Kimera
    - WARNING : you can have error with gtsam and Kimera-VIO while building the catskin workspace. Follow [this](https://github.com/MIT-SPARK/Kimera-VIO-ROS/issues/180) post to have more informations to fix the problem. (change the gsam version and modifiy kimera to accept the new version)