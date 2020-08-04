#!/usr/bin/env python
import serial
import rospy
#import actionlib
from std_msgs.msg import String, UInt8 
#from move_base_msg.msg import MoveBaseGoal 
 
ser = serial.Serial('/dev/ttyUSB2', baudrate=9600) # Set Serial Link


def callback(status_list):
	rospy.loginfo(rospy.get_caller_id() + "I heard %d", status_list.status)
	#command = status_list.status
	#print command 
	#ser.write(command.encode())      	

	#primary_counter = 0
	#sub_counter = 0	
	
	#init_command = "a,0,0,0,0,0,0,0,0"
	#ser.write(init_command.encode())
	#rospy.sleep(1.)

	#while(primary_counter < 700):
		
		#time_now = rospy.get_time()
		#if (time_now - seconds) < 2.0:
		#	print "Trigger 1"

		#else : 
		#	print "Trigger 2"
		
		

		#if (sub_counter < 200):
			#command = "a,0,0,1,1,1,1,0,0"
			#print "Trigger 1"
			#print command
			#ser.write(command.encode())
		#else:
			#command = "a,1,1,1,1,1,1,255,0"
			#print "Trigger 2"
			#print command	
			#ser.write(command.encode())
		
		#primary_counter += 1
		#sub_counter += 1
		#print primary_counter
		#print sub_counter 
	
	
	#command = "a,0,0,0,0,0,0,0,0"
	#print "Trigger 3"
	#print command 
	#ser.write(command.encode())	
	#print "Exitted Loop"


def goalControl():
	rospy.init_node('goalControl', anonymous=True)
 	rospy.Subscriber("/move_base/status", UInt8, callback)
	
	seconds = rospy.get_time()
	duration = rospy.Duration.from_sec(3.) 
	
	primary_counter = 0
	sub_counter = 0	
	
	init_command = "a,0,0,0,0,0,0,0,0"
	ser.write(init_command.encode())
	rospy.sleep(1.)

	while(primary_counter < 700):
		
		#time_now = rospy.get_time()
		#if (time_now - seconds) < 2.0:
		#	print "Trigger 1"

		#else : 
		#	print "Trigger 2"
		
		

		if (sub_counter < 200):
			command = "a,0,0,1,1,1,1,0,0"
			print "Trigger 1"
			print command
			ser.write(command.encode())
		else:
			command = "a,1,1,1,1,1,1,255,0"
			print "Trigger 2"
			print command	
			ser.write(command.encode())
		
		primary_counter += 1
		sub_counter += 1
		print primary_counter
		print sub_counter 
	
	
	command = "a,0,0,0,0,0,0,0,0"
	print "Trigger 3"
	print command 
	ser.write(command.encode())	
	print "Exitted Loop"
	rospy.spin()
 
if __name__ == '__main__':   
	try:
		goalControl()
	except KeyboardInterrupt:
		command = "a,0,0,0,0,0,0,0,0"
		ser.write(command.encode())
	else:
		pass
		
