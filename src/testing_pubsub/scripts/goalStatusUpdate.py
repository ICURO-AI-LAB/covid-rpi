#!/usr/bin/env python
import serial
import rospy
import actionlib 
#import actionlib_msgs
from actionlib_msgs.msg import GoalStatusArray
from std_msgs.msg import String, UInt8 
#from move_base_msg.msg import MoveBaseGoal
 
#ser = serial.Serial('/dev/ttyUSB1', baudrate=9600) # Set Serial Link


def callback(status_list):
	rospy.loginfo(rospy.get_caller_id() + "I heard %d", status_list.status)	
	print status_list.status
	print status_list.text
		
def goalStatusUpdate():
	rospy.init_node('goalStatusUpdate', anonymous=True)
 	rospy.Subscriber("/move_base/status", GoalStatusArray, callback)	
	rospy.spin()
 
if __name__ == '__main__':   
	try:
		goalStatusUpdate()
	except rospy.ROSInterruptException:
		pass
