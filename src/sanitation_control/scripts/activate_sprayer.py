#!/usr/bin/env python
import serial
import rospy
import tty
import sys
import termios
import actionlib
from actionlib_msgs.msg import GoalStatusArray
#from std_msgs.msg import String, UInt8 
#from move_base_msg.msg import MoveBaseGoal 
 
ser = serial.Serial('/dev/ttyUSB0', baudrate=9600) # Set Serial Link

NOT_GOAL = 0
GOAL = 1

def callback(data):
	global NOT_GOAL
	global GOAL
	
	print "hello"
	status_list = data.status_list	
	
	print('-----')
        if (len(status_list) == 1):
                for status in status_list:
                        if(status.status == 1):
                                current_state = NOT_GOAL
                                print "moving"
                        else:
                                current_state = GOAL
                                print "stopped"
                        
        elif (len(status_list) <= 2):
                for status in status_list:
                        current_state = NOT_GOAL
                        print "moving"
                           
        print('----')


def activateSprayer():
	rospy.init_node('activate_sprayer', anonymous=True)
 	rospy.Subscriber("/move_base/status", GoalStatusArray, callback)
	
	#Set Duration Times
	two_seconds = rospy.Duration.from_sec(2.)
	five_seconds = rospy.Duration.from_sec(5.)
	fifteen_seconds = rospy.Duration.from_sec(15.)
	twenty_seconds = rospy.Duration.from_sec(20.)
	thirty_seconds = rospy.Duration.from_sec(30.)
	sixty_seconds = rospy.Duration.from_sec(60.)

	#Save current times and set stop times
	time_now = rospy.Time.now()
	time_after_2secs = time_now + two_seconds
	time_after_7secs = time_after_2secs + five_seconds
	time_after_15secs = time_now + fifteen_seconds
	time_after_20secs = time_now + twenty_seconds
	time_after_30secs = time_now + thirty_seconds 
	time_after_60secs = time_now + sixty_seconds 	
	
	rospy.sleep(.5)
	
	while(time_now < time_after_7secs): #Time for full spraying actuation
		if (time_now < time_after_2secs):
			print "Trigger 1	"
			time_now = rospy.Time.now()
			init_command = "a,1,1,1,1,1,1,0,0" #Trigger relay actuation 
			ser.write(init_command.encode())
		else:
			print "Trigger 2"
			time_now = rospy.Time.now()
			init_command = "a,1,1,1,1,1,1,255,0" #Turn on PWM signals 
			ser.write(init_command.encode())

		time_now = rospy.Time.now() #Upate current time 

		

		

	#while(primary_counter < 700):		

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

	command = "a,0,0,0,0,0,0,0,0"
	print "Trigger 3"
	print command 
	ser.write(command.encode())	

				
	print "Exitted Loop"
	rospy.spin()
	command = "a,0,0,0,0,0,0,0,0"
	print "Safety Off Trigger"
	print command 
	ser.write(command.encode())	

 
if __name__ == '__main__':   
	try:
		activateSprayer()
	except rospy.ROSInterruptException:
		pass
	#except KeyboardInterrupt:
		#command = "a,0,0,0,0,0,0,0,0"
		#ser.write(command.encode())
	#else:
		#pass
