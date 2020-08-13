#!/usr/bin/env python
import serial
import rospy
import actionlib 
import time 
#import actionlib_msgs
from actionlib_msgs.msg import GoalStatusArray
from std_msgs.msg import String

#Turned off command strings for testing

ser = serial.Serial('/dev/ttyUSB0', baudrate=9600) # Set Serial Link

TRUE = 1
FALSE = 0

NOT_GOAL = 0
GOAL = 1

prev_state = GOAL 
current_state = GOAL
goalCounter = 0

# takes in goal array msg, outputs whether we are at the goal or 
# still moving
def checkStatusArray(status_list):
	returnStatus = NOT_GOAL
	length = len(status_list)
	if (length == 0):
		return GOAL
	else:
		for status in status_list:	
			if status.status != 3:
				returnStatus = NOT_GOAL
				return returnStatus
			else:
				returnStatus = GOAL

def callback(data):	
	pub = rospy.Publisher('spray_status', String, queue_size=1)

	global prev_state
	global current_state
	global GOAL
	global NOT_GOAL 
	#primary_counter = 0
	#sub_counter = 0 
	global goalCounter
		
	status_list = data.status_list
	
	current_state = checkStatusArray(status_list)

	if ( current_state != prev_state ):
		goalCounter = goalCounter + 1

	if( (current_state != prev_state) and (current_state == GOAL)):
			
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
              		if(time_now < time_after_2secs):
                        	time_now = rospy.Time.now()
                        	#command = "a,1,1,1,1,1,1,0,0"
                                command = "a,0,0,0,0,0,0,0,0"
				spray_status = "Trigger 1"
                                pub.publish(spray_status)
                                ser.write(command.encode())
				
               		else:
                        	time_now = rospy.Time.now()
                        	#command = "a,1,1,1,1,1,1,255,0"
                                command = "a,0,0,0,0,0,0,0,0"
				spray_status = "Trigger 2"
                                pub.publish(spray_status)
                                ser.write(command.encode())
			
			time_now = rospy.Time.now()

	command = "a,0,0,0,0,0,0,0,0"
	spray_status =  "Trigger 3"
	#print command
	pub.publish(spray_status)
	ser.write(command.encode())
	prev_state = current_state	

		
def goalControl():
	rospy.init_node('goal_control', anonymous=True)
	rospy.Subscriber("/move_base/status", GoalStatusArray, callback)	

	rospy.spin()
 
if __name__ == '__main__':   
	try:
		goalControl()
	except rospy.ROSInterruptException:
		pass

