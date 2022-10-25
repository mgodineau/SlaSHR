import rospy
import cv2

from sensor_msgs.msg import Image, CameraInfo


class camLogger_node:
    
    
    def __init__(self) -> None:
        self.cameraInfo = None
        self.outputFile = None
        
        rospy.init_node("cam_logger")
        
        image_sub = rospy.Subscriber("camera/color/image_raw", Image, self.addFrame)
        cam_info_sub = rospy.Subscriber("camera/color/camera_info", CameraInfo, self.setCameraInfo)
    
    
    def setCameraInfo(self, msg: CameraInfo):
        if self.cameraInfo != msg:
            if self.outputFile is not None:
                self.outputFile.release()
            
            self.outputFile = cv2.VideoWriter("/home/robot/Documents/output.pm4", cv2.VideoWriter_fourcc(*'MPEG'), 30, (1080, 1920))
            
        self.cameraInfo = msg
    
    
    def addFrame(self, msg: Image ):
        if self.cameraInfo is None:
            rospy.logwarn("the camera logger received a frame before the camera infos were send, so the frame is discared.")
            return
        
        frame = None
        self.cameraInfo.write(frame)
        




if __name__ == "__main__":
    
    node = camLogger_node()
    
    rospy.spin()