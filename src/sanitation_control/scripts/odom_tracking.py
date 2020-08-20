#!/usr/bin/env python
import serial
import rospy
import time 
import re
from std_msgs.msg import String
from nav_msgs.msg import Odometry 

global file_object

def callback(data):
	global file_object
	#print str(data)
	t = time.localtime()
	current_time = time.strftime("%D-%H:%M:%S",t)

	timeString = str(current_time)
	poseString = str(data.pose.pose.position)
	headerString = str(data.header.stamp)
	
	print(timeString)
	print(poseString)
	#file_object.write(headerString)	
	file_object.seek(0,0)
	file_object.write(timeString)
	file_object.write('\n')
	file_object.write(poseString)
	file_object.write('\n')
	file_object.write('\n')
	
	#rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
	rospy.sleep(1)

	

def odom_write():
	global file_object
	print('creating file object')
	file_object = open('testfile.txt','w')
	safe_sleep_time = 1.0
	rospy.init_node('odom_tracking', anonymous=True)
 	rospy.Subscriber("odom", Odometry, callback)
	rospy.sleep(safe_sleep_time)
	#print('done sleeping')
	rospy.spin()
  
if __name__ == '__main__':   
	odom_write()
