#!/usr/bin/env python
#modified by the legendary ~software team  

import serial
import rospy
from std_msgs.msg import String
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.IN)

def solution_level():
        pub = rospy.Publisher('Solution_Level', String, queue_size=1)
        rospy.init_node('Solution_Level', anonymous=True)
        rate = rospy.Rate(1) # 1hz
	while not rospy.is_shutdown():
		if GPIO.input(14):
	    		indication = "Pin 8 is HIGH, Water Level Is Chilling Dawg"
			print indication
		else:
   		 	indication = "Pin 8 is LOW, Water Level Is Dangerous Dawg"
			print indication
                pub.publish(indication)
		rate.sleep()  

if __name__ == '__main__':   
	solution_level()
