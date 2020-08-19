#!/usr/bin/env python
import serial
import rospy
import time 
from std_msgs.msg import String
from nav_msgs.msg import Odometry 




def callback(data):
	#print str(data)
	t = time.localtime()
	current_time = time.strftime("%D-%H:%M:%S",t)
	
	print "-----------"
	print (current_time)
	print str(data.pose.pose.position)
	print str(data.header.stamp)
	
	#rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
	rospy.sleep(1)


def odom_write():
	rospy.init_node('odom_tracking', anonymous=True)
 	rospy.Subscriber("odom", Odometry, callback)
	rospy.spin()
  
if __name__ == '__main__':   
	odom_write()
