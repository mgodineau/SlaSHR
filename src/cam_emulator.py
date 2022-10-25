#!/usr/bin/env python

import rospy
import cv2
import numpy as np

import cv_bridge
from sensor_msgs.msg import Image, CameraInfo
from std_msgs.msg import Int32


if __name__ == "__main__":
	rospy.init_node("cam_emulator")
	
	
	pub_color_image = rospy.Publisher("camera/color/image_raw", Image, queue_size=1)
	pub_color_info = rospy.Publisher("camera/color/camera_info", CameraInfo, queue_size=1)
	pub_tmp = rospy.Publisher("camera/test", Int32, queue_size=1)
	
	
	# img = np.ones((400, 400, 3), np.uint8) * 64
	bridge = cv_bridge.CvBridge()
	video_path = rospy.get_param("~video_path")
	video = cv2.VideoCapture(video_path)
	
	timePerFrame = 1.0 / video.get(cv2.CAP_PROP_FPS)
	previousFrameTime = rospy.get_time()
	
	while(not rospy.is_shutdown()):
		
		
		
		ret, img = video.read()
		if not ret:
			video = cv2.VideoCapture(video_path)
			continue
		
		
		pub_color_image.publish( bridge.cv2_to_imgmsg(img) )
	
		rospy.sleep(timePerFrame - (rospy.get_time() - previousFrameTime))
		previousFrameTime = rospy.get_time()
		