#!/usr/bin/env python
#modified by the legendary ~software team  

import serial
import rospy
import time 
from std_msgs.msg import String
from sanitation_msgs.msg import solution
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.IN)

def solution_level():
        pub = rospy.Publisher('solution_level', solution, queue_size=1)
        rospy.init_node('solution_level', anonymous=True)
	solution_message = solution()
        rate = rospy.Rate(1) # 1hz
	
	t = time.localtime()
        current_time = time.strftime("%D-%H:%M:%S",t)
	
	while not rospy.is_shutdown():
		if GPIO.input(16):
	    		solution_message.status = "-------Water Level Is Chilling Dawg--------"
			#print solution_message.status
		else:
   		 	solution_message.status = " ------Water Level Is Dangerous Dawg---------"
			#print solution_message.status
		
		solution_message.runtime = current_time
                pub.publish(solution_message)
		rate.sleep()  

if __name__ == '__main__':   
	solution_level()
