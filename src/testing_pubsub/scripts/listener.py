#!/usr/bin/env python
import serial
import rospy
from std_msgs.msg import String
 
ser = serial.Serial('/dev/ttyUSB0', baudrate=9600)


def callback(data):
	rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
	command = data.data

	print command 
 
	ser.write(command.encode())  

	#command = data.data 

	#if command != last_command: 
	#	ser.write(command.encode())	
	#	last_command = command 
    	


def listener():
	rospy.init_node('listener', anonymous=True)
 	rospy.Subscriber("chatter", String, callback)

	rospy.spin()
  
if __name__ == '__main__':   
	listener()
