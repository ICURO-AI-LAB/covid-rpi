#!/usr/bin/env python
import rospy
import time
import rospy
from generate_nav_goals import generateNavGoals 
from std_msgs.msg import String
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal # for client approach
from geometry_msgs.msg import PoseStamped # for our crude approach

navGoalArray = []
i = 0
navPublisher = rospy.Publisher('test_nav_goal', PoseStamped, queue_size=1)

safe_spray_status = "Trigger 3"
spraying_status = "Trigger 2"

current_spray_status = safe_spray_status
prev_spray_status = safe_spray_status

# takes status strings, on transition of stage 2 -> stage 3
# return boolean to send the nav goal

def goodToSendGoal(current_spray_status,prev_spray_status):

	global safe_spray_status
	global spraying_status
	# check the transition
	result = None
	if ( safe_spray_status in current_spray_status and  spraying_status in prev_spray_status ):
		result = True
	else: 
		result = False

	#print(result)
	return result		


def sendNavGoal(navGoals):
	global i
	navPublisher.publish(navGoals[i])
	i = i + 1
	print('sent nav goal:')

def navGoalCallback(data):

	global navPublisher 
	global i
	global safe_spray_status
	global prev_spray_status
	global spraying_status

	# convert stdmsg String to str for interpretatoin
	current_spray_status = str(data)

	#print('curr: ' +  current_spray_status ) 
	#print('prev: ' + prev_spray_status ) 

	# initialization
	if ( i == 0 ):
		sendNavGoal(navGoalArray)
	elif goodToSendGoal(current_spray_status,prev_spray_status):
		sendNavGoal(navGoalArray)
		# create move base goal
	print('i: ' + str(i))

	prev_spray_status = current_spray_status
	
def send_nav_goals():
	global navGoalArray

	# populate the navGoalArray with goals
	generateNavGoals(navGoalArray)
	
	rospy.init_node('send_nav_goals', anonymous=True)
	rospy.Subscriber("/spray_status", String, navGoalCallback)	
	
	#print('nav goals: ')
	#for item in navGoalArray:
	#	print(item)
	#print('done printing')
	
	rospy.spin()

if __name__ == '__main__':
	try:
		send_nav_goals()
	except rospy.ROSInterruptException:
		print('FAILED NAV GOALS')
		pass

