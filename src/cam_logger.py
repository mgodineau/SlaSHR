#!/usr/bin/env python

import rospy
import cv2
import numpy as np

import cv_bridge
from sensor_msgs.msg import Image, CameraInfo


class camLogger_node:
	
	
	def __init__(self):
		self.cameraInfo = None
		self.outputFile = None
		self.bridge = cv_bridge.CvBridge()
		
		rospy.init_node("cam_logger")
		
		image_sub = rospy.Subscriber("camera/color/image_raw", Image, self.addFrame)
		cam_info_sub = rospy.Subscriber("camera/color/camera_info", CameraInfo, self.setCameraInfo)
	
	def __del__(self):
		rospy.logwarn("deleting camLogger")
		if self.outputFile is not None:
			self.outputFile.release()
	
	
	def setCameraInfo(self, cameraInfo):
		if self.outputFile is not None:
			return
		
		rospy.logwarn("opening file...")
		self.outputFile = cv2.VideoWriter("/home/robot/Documents/output.avi", cv2.VideoWriter_fourcc(*'MJPG'), 30, (cameraInfo.width, cameraInfo.height))
		
		self.cameraInfo = cameraInfo
	
	
	def addFrame(self, image ):
		if self.cameraInfo is None:
			rospy.logwarn("[cam_logger] the camera logger received a frame before the camera infos were send, so the frame is discared.")
			return
		
		# frame = np.ones((400, 600, 3), dtype=np.uint8) * 128
		frame = self.bridge.imgmsg_to_cv2(image)
		self.outputFile.write(frame)
		




if __name__ == "__main__":
	
	node = camLogger_node()
	
	rospy.spin()
	del node