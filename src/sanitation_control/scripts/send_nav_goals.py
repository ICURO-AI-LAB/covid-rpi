#!/usr/bin/env python
import rospy
import time
import rospy
from generate_nav_goals import generateNavGoals 
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped # for our crude approach
from actionlib_msgs.msg import GoalStatus
from actionlib_msgs.msg import GoalStatusArray
from std_msgs.msg import String
from continuous_spray_control import checkStatusArray

NOT_GOAL = 'Not At Goal'
GOAL = 'At Specified Goal'
prev_state = GOAL 
current_state = GOAL
goalCounter = 0
sleepCounter = 0


navGoalArray = []
i = 0
navPublisher = rospy.Publisher('move_base_simple/goal', PoseStamped, queue_size=1)

def sendNavGoal(navGoals):
	global i
	j = 0
	print('sent nav goal['+str(i)+']')
	print(str(navGoals[i]))
	print('-----------------------')
	navPublisher.publish(navGoals[i])
	i = i + 1

def navGoalCallback(data):

	global navPublisher 
	global i
	global prev_state
	global current_state
	global sleepCounter 
	# get the goal array status list	
	status_list = data.status_list
	# check the status list
	current_state = checkStatusArray(status_list)

	#print(str(current_state))
	#print(str(sleepCounter))
		
	if current_state == GOAL  and i < len(navGoalArray):
		sendNavGoal(navGoalArray)

	prev_state = current_state
	
def send_nav_goals():
	global navGoalArray
	rospy.init_node('send_nav_goals', anonymous=True)

	# populate the navGoalArray with goals
	generateNavGoals(navGoalArray,'johnny_boy')
	rospy.sleep(2.5)
	# SENDS ONE NAV GOAL 
	#sendNavGoal(navGoalArray)

	rospy.Subscriber("/move_base/status", GoalStatusArray, navGoalCallback)	
	rospy.spin()

if __name__ == '__main__':
	try:
		send_nav_goals()
	except rospy.ROSInterruptException:
		print('FAILED NAV GOALS')
		pass


