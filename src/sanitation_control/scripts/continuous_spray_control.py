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

ser = serial.Serial('/dev/ttyUSB0', baudrate=9600) # Set Serial Link

NOT_GOAL = 'Not At Goal'
GOAL = 'At Specified Goal'

prev_state = GOAL 
current_state = GOAL

preLoaded = False
physical_testing = True
goalCounter = 0

validGoalCount = [ 1 ,5 ,9 ]

# return true if we are supposed to be spraying
# sprays every other waypoint
def validSprayGoal():

	global goalCounter
	global validGoalCount

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

def callback(data):	
	pub = rospy.Publisher('spray_status', String, queue_size=1)

	global prev_state
	global current_state
	global GOAL
	global NOT_GOAL
	global goalCounter
	global physical_testing 
	global preLoaded

	# define the status list from the incoming data received		
	status_list = data.status_list
	#print( 'status list len:' + str(len(status_list)) )
	#for i in range(0,len(status_list)):
#		print(i)
#		print(status_list[i])

	spray_status = "Trigger 3: Both Spraying Motors Off"
	current_state = checkStatusArray(status_list)
	# debugging print statements
	#for status in status_list:
	#	print(str(status.status))


	# beginning the journey not preloaded water yet
	if ( current_state != prev_state ):
		goalCounter = goalCounter + 1	
		print( 'validSprayGoal: ' + str(validSprayGoal()))
		if ( goalCounter == 10 ):
			trigger_text_client()		

	print('state: ' + current_state + ' -- prev_state: ' + prev_state + ' -- goalCounter: ' + str(goalCounter))	

			
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
		
		# preload the sprayer as to not damage the large motor
		while( time_now < time_after_2secs ): #Time for full spraying actuation

			time_now = rospy.Time.now()
			command = "a,1,1,1,1,1,1,0,0"

			spray_status = "Trigger 1: Relays On, Loading Initial Water"
			#print(spray_status)
			pub.publish(spray_status)
			if physical_testing:		
				ser.write(command.encode())
			time_now = rospy.Time.now()
			preLoaded = True	
			
	if ( current_state == NOT_GOAL and preLoaded and validSprayGoal() ):
		command = "a,1,1,1,1,1,1,255,0"
		spray_status = "Trigger 2: Spraying Water!"
		if (physical_testing):
			ser.write(command.encode())

	if ( current_state == GOAL ):
		command = "a,0,0,0,0,0,0,0,0"
		spray_status = "Trigger 3: Both Spraying Motors Off"
		if physical_testing:
			ser.write(command.encode())
		# print('TRIGGER 3: DONE SPRAYING, AT GOAL')
		preLoaded = False

	print(spray_status)

	# publish current status
	pub.publish(spray_status)		
	# update current state
	prev_state = current_state	

		
def continuous_spray_control():
	rospy.init_node('continuous_spray_control', anonymous=True)
	rospy.Subscriber("/move_base/status", GoalStatusArray, callback)	

	rospy.spin()
 
if __name__ == '__main__':   
	try:
		continuous_spray_control()
	except rospy.ROSInterruptException:
		pass

