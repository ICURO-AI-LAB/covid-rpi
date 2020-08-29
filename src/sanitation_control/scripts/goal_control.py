#!/usr/bin/env python
import serial
import rospy
import actionlib 
import time
from go_home_client import go_home_client 
#import actionlib_msgs
from actionlib_msgs.msg import GoalStatusArray
from std_msgs.msg import String
#from twilio_client import trigger_text_client

#Turned off command strings for testing

ser = serial.Serial('/dev/ttyUSB_ARDUINO', baudrate=9600) # Set Serial Link

NOT_GOAL = 'MOVING'
GOAL = 'AT GOAL'

global pub
prev_state = GOAL 
current_state = GOAL
numSprayPoints = 3 # number of waypoints
zonesCompleted = 0
numGoals = numSprayPoints * 2
goalCounter = 0  
goHomeFlag = False
physicalTesting = True


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

# listen to launch cmd string
def launchCmdCheck(data):
	global goHomeFlag
	global pub
	global goalCounter
	global zonesCompleted 
	if 'home' in str(data):
		goHomeFlag = True
		# going home protocol
		spray_status = turnOffRelays()
		print('got go home flag')
		pub.publish(spray_status + ' ' + str(current_state) + ' returning home' )
		# go home action
		goalCounter = 0
		zonesCompleted = 0
		go_home_client()
		
	if 'protocol' in str(data):
		print('received launch protocol')
		goalCounter = 0
		zonesCompleted = 0
		goHomeFlag = False

# turn on and turn off relays return a spray status string
def turnOnRelays():
	command = "a,1,1,1,1,1,1,0,0"
	spray_status =  "SPRAYING"
	if physicalTesting:
		ser.write(command.encode())
	return spray_status

def turnOffRelays():
	command = "a,0,0,0,0,0,0,0,0"
	spray_status =  "SPRAYER OFF"
	if physicalTesting:
		ser.write(command.encode())
	return spray_status

# data is the move base status
def executeStopSpraySM(data):	
	global prev_state
	global current_state
	global GOAL
	global NOT_GOAL 
	global goalCounter
	global goHomeFlag
	global pub
	global zonesCompleted

	spray_status = ''
	status_list = data.status_list	
	current_state = checkStatusArray(status_list)
	if ( current_state != prev_state ):
		goalCounter = goalCounter + 1

	
	#print(str(data))
	if goHomeFlag:
		spray_status = 'awaiting cmds '
		pass
	else:
		spray_status = 'executing '
		# if we havent gotten the goHomeFlag, then if we are at a goal
		# and we stopped spraying, then execute cleaning protocol

		# if we are at a goal just spray
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
				spray_status = turnOnRelays()
				pub.publish(spray_status + ' ' + str(current_state) + ' ' + str(zonesCompleted) + ' ')
				time_now = rospy.Time.now()

			zonesCompleted = zonesCompleted + 1

		
	spray_status = spray_status + turnOffRelays()
	#print command
	pub.publish(spray_status + ' ' + str(current_state) + ' ' +  str(zonesCompleted) + ' ')
	prev_state = current_state	
		
def goalControl():
	global pub
	pub = rospy.Publisher('spray_status', String, queue_size=1)
	rospy.init_node('goal_control', anonymous=True)
	moveBaseSub = rospy.Subscriber("/move_base/status", GoalStatusArray, executeStopSpraySM)
	cmdsSub = rospy.Subscriber("launch_cmds", String, launchCmdCheck)	
	rospy.sleep(2.5)
	#print('spinning')
	rospy.spin()
 
if __name__ == '__main__':   
	try:
		goalControl()
	except rospy.ROSInterruptException:
		pass

