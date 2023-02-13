#!/usr/bin/env python

import rospy
import cv2
import numpy as np

import cv_bridge
from sensor_msgs.msg import Image, CameraInfo
from std_msgs.msg import Header, Time


if __name__ == "__main__":
	rospy.init_node("cam_emulator")
	
	
	pub_color_image = rospy.Publisher("camera/color/image_raw", Image, queue_size=1)
	pub_color_info = rospy.Publisher("camera/color/camera_info", CameraInfo, queue_size=1)
	
	
	
	# img = np.ones((400, 400, 3), np.uint8) * 64
	bridge = cv_bridge.CvBridge()
	video_path = rospy.get_param("~video_path")
	video = cv2.VideoCapture(video_path)
	
	timePerFrame = 1.0 / video.get(cv2.CAP_PROP_FPS)
	previousFrameTime = rospy.get_time()
	
	cameraInfo = CameraInfo(
		header = Header(
			seq=0,
			stamp=rospy.Time.now(),
			frame_id="map"
		),
		height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT)),
		width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH)),
		distortion_model = "plumb_bob",
		D = [0, 0, 0, 0, 0],
		K = [1, 0, 0, 0, 1, 0, 0, 0, 1],
		R = [1, 0, 0, 0, 1, 0, 0, 0, 1],
		P = [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0]
	)
	
	while(not rospy.is_shutdown()):
		
		
		
		ret, img = video.read()
		if not ret:
			video = cv2.VideoCapture(video_path)
			continue
		
		
		pub_color_image.publish( bridge.cv2_to_imgmsg(img) )
		pub_color_info.publish( cameraInfo )
		
		rospy.sleep(timePerFrame - (rospy.get_time() - previousFrameTime))
		previousFrameTime = rospy.get_time()
		