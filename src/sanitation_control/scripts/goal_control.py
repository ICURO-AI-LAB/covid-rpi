#!/usr/bin/env python
import serial
import rospy
import actionlib 
import time 
#import actionlib_msgs
from actionlib_msgs.msg import GoalStatusArray
from std_msgs.msg import String
from twilio_client import trigger_text_client

#Turned off command strings for testing

ser = serial.Serial('/dev/ttyUSB0', baudrate=9600) # Set Serial Link

TRUE = 1
FALSE = 0

NOT_GOAL = 'MOVING'
GOAL = 'AT GOAL'

prev_state = GOAL 
current_state = GOAL
goalCounter = 0

physicalTesting = False

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
	return returnStatus

def callback(data):	

	global prev_state
	global current_state
	global GOAL
	global NOT_GOAL 
	global goalCounter
		
	status_list = data.status_list
	
	current_state = checkStatusArray(status_list)

	if ( current_state != prev_state ):
		goalCounter = goalCounter + 1
		if goalCounter == 6:
			trigger_text_client()

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
			time_now = rospy.Time.now()

			command = "a,1,1,1,1,1,1,0,0"
			spray_status = "Trigger 1"
			if physicalTesting:
				ser.write(command.encode())

			pub.publish(spray_status)
			time_now = rospy.Time.now()

	command = "a,0,0,0,0,0,0,0,0"
	spray_status =  "Trigger 3"
	if physicalTesting:
		ser.write(command.encode())

	#print command
	pub.publish(spray_status + ' ' + str(current_state) )
	prev_state = current_state	

		
def goalControl():
	pub = rospy.Publisher('spray_status', String, queue_size=1)
	rospy.init_node('goal_control', anonymous=True)
	rospy.Subscriber("/move_base/status", GoalStatusArray, callback)	
	rospy.sleep(2.5)
	rospy.spin()
 
if __name__ == '__main__':   
	try:
		goalControl()
	except rospy.ROSInterruptException:
		pass

