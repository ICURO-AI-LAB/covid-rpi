#!/usr/bin/env python
import serial
import rospy
import actionlib 
import time 
#import actionlib_msgs

from actionlib_msgs.msg import GoalStatus
from actionlib_msgs.msg import GoalStatusArray
from std_msgs.msg import String
from twilio_client import trigger_text_client

ser = serial.Serial('/dev/ttyUSB_ARDUINO', baudrate=9600) # Set Serial Link

NOT_GOAL = 'MOVING'
GOAL = 'AT GOAL'

prev_state = GOAL 
current_state = GOAL

zonesCompleted = 0
preLoaded = False
physicalTesting = False
goalCounter = 0
validGoalCount = [ 1 ,5 ,9 ]
goHomeFlag = False

# return true if we are supposed to be spraying
# sprays every other waypoint
def validSprayGoal():
	if goalCounter in validGoalCount:
		return True
	else:
		return False

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

# spray helper functinos
def sprayWater():
        command = "a,1,1,1,1,1,1,255,0"
        spray_status =  "SPRAYING"
        if physicalTesting:
                ser.write(command.encode())
        return spray_status

def loadSprayer():
        command = "a,1,1,1,1,1,1,0,0"
        spray_status =  "SPRAYING"
        if physicalTesting:
                ser.write(command.encode())
        return spray_status


def turnOffSprayer():
        command = "a,0,0,0,0,0,0,0,0"
        spray_status =  "SPRAYER OFF"
        if physicalTesting:
                ser.write(command.encode())
        return spray_status


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

def callback(data):	

	global prev_state
	global current_state
	global goalCounter
	global physical_testing 
	global preLoaded
	global zonesCompleted

	spray_status = ""
	# define the status list from the incoming data received		
	status_list = data.status_list
	current_state = checkStatusArray(status_list)
	# debugging print statements

	# beginning the journey not preloaded water yet
	if ( current_state != prev_state ):
		goalCounter = goalCounter + 1	
		print( 'validSprayGoal: ' + str(validSprayGoal()))
	
	print('state: ' + current_state + ' -- prev_state: ' + prev_state + ' -- goalCounter: ' + str(goalCounter))

	# do nothing if we went home
	if goHomeFlag:
		spray_status = 'awaiting cmds ' + turnOffSprayer()
		pass
	else:
		spray_status = 'executing '
		# go home flag has not been pressed
		# nominal execution:
		# if we arent at the goal and its a valid spray goal
		if ( current_state == NOT_GOAL and not preLoaded and validSprayGoal() ):

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

			# for consistency
			rospy.sleep(0.5)

			spray_status = spray_status + loadSprayer()	
			# preload the sprayer as to not damage the large motor
			while( time_now < time_after_2secs ): #Time for full spraying actuation
				time_now = rospy.Time.now()
				time_now = rospy.Time.now()
				preLoaded = True
				pub.publish(current_state + ' ' + spray_status + ' ' + str(zonesCompleted) + ' \n')		

			
			zonesCompleted = zonesCompleted + 1	
		
		# if the robot is moving and its a valid spray goal, go ahead and  spray
		if ( current_state == NOT_GOAL and preLoaded and validSprayGoal() ):
			spray_status = spray_status + sprayWater()
		
		# if we're chilling then dont spray
		if ( current_state == GOAL ):
			spray_status = spray_status + turnOffSprayer()
			preLoaded = False

	# publish current status
	pub.publish(current_state + ' ' + spray_status + ' ' + str(zonesCompleted) + ' \n')		
	print(current_state + ' ' + spray_status)		
	
	# update current state
	prev_state = current_state	

def continuous_spray_control():
	global pub
	rospy.init_node('continuous_spray_control', anonymous=True)
	rospy.sleep(1.0)
	pub = rospy.Publisher('spray_status', String, queue_size=1)
	rospy.Subscriber("/move_base/status", GoalStatusArray, callback)
	rospy.Subscriber("launch_cmds", String, launchCmdCheck)
	rospy.spin()
 
if __name__ == '__main__':   
	try:
		continuous_spray_control()
	except rospy.ROSInterruptException:
		pass

