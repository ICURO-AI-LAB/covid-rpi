#!/usr/bin/env python
import serial
import rospy
import actionlib 
#import actionlib_msgs
from actionlib_msgs.msg import GoalStatusArray,GoalStatus,GoalID
from std_msgs.msg import String, UInt8 
#from move_base_msg.msg import MoveBaseGoal


ser = serial.Serial('/dev/ttyUSB2', baudrate=9600) # Set Serial Link

TRUE = 1
FALSE = 0

NOT_GOAL = 0
GOAL = 1

prev_state = GOAL 
current_state = GOAL 

#primary_counter = 0
#sub_counter = 0
#main_Counter = 0 #keep track of spraying time 
#spraying_interval = 300 #spray for 300 seconds


def callback(data):
	#rospy.loginfo(rospy.get_caller_id() + "I heard %s", data)
	global prev_state
	global current_state
	global GOAL
	global NOT_GOAL 
	primary_counter = 0
	sub_counter = 0 
		
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
			#print(status.text)
			#print(status.status)
	elif (len(status_list) <= 2):
		for status in status_list:
			current_state = NOT_GOAL
			print "moving"
			#print(status.text)
			#print(status.status)	
	print('----')

	if( (current_state != prev_state) and (current_state == GOAL)):
		while(primary_counter < 500):	#Start loop for 5 seconds
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
	
	prev_state = current_state			
	#elif( current_state == )

	#if(ACTIVATE_SPRAY):
	
		
def goalControl():
	rospy.init_node('goalControl', anonymous=True)
 	rospy.Subscriber("/move_base/status", GoalStatusArray, callback)	
	
	"Testing Launch File"	
	#Spraying_Actuated = FALSE

	#if( (current_state!= prev_state)
	

	#if((current_state != prev_state):
		
		
	#else:
	
	rospy.spin()
 
if __name__ == '__main__':   
	try:
		goalControl()
	except rospy.ROSInterruptException:
		pass

