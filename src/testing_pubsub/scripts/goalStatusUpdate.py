#!/usr/bin/env python
import serial
import rospy
import actionlib 
#import actionlib_msgs
from actionlib_msgs.msg import GoalStatusArray,GoalStatus,GoalID
from std_msgs.msg import String, UInt8 
#from move_base_msg.msg import MoveBaseGoal
 
#ser = serial.Serial('/dev/ttyUSB1', baudrate=9600) # Set Serial Link


def callback(data):
	#rospy.loginfo(rospy.get_caller_id() + "I heard %s", data)

	status_list = data.status_list

	print('-----')
	if (len(status_list) == 1):
		for status in status_list: 
			state = status.status
			if(status.status == 1):
				print "moving"
			else:			
				print "stopped"
			print(status.text)
			print(status.status)
	elif (len(status_list) <= 2):
		for status in status_list:
			print "moving"
			print(status.text)
			print(status.status)	
	print('----')
	
		
def goalStatusUpdate():
	rospy.init_node('goalStatusUpdate', anonymous=True)
 	rospy.Subscriber("/move_base/status", GoalStatusArray, callback)	
	rospy.spin()
 
if __name__ == '__main__':   
	try:
		goalStatusUpdate()
	except rospy.ROSInterruptException:
		pass

