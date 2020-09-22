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

NOT_GOAL = 'MOVING'
GOAL = 'AT GOAL'
prev_state = GOAL 
current_state = GOAL
goalCounter = 0
sleepCounter = 0
navGoalArray = []
i = 0
navPublisher = rospy.Publisher('move_base_simple/goal', PoseStamped, queue_size=1)

# check string for sprayer off
def goodSendFlag(data):
        data = str(data)
        if 'SPRAYER OFF' in data and 'GOAL' in data and 'executing' in data:
                sendGoalFlag = True
        else:
                sendGoalFlag = False

        return sendGoalFlag

# check the launch cmds set goal counter to 0
def launchCmdCheckNavGoals(data):
        global i
	global protocolSent
        if 'protocol' in str(data):
                i = 0
                #sendNavGoal(navGoalArray)


def sendNavGoal(navGoals):
	global i
	j = 0
	print('sent nav goal['+str(i)+']')
	print(str(navGoals[i]))
	print('-----------------------')
	navPublisher.publish(navGoals[i])
	#rospy.sleep(10.0)
	i = i + 1

# listens to spray status
def navGoalCallback(data):

        global navPublisher 
        global i
        global prev_state
        global current_state
        global sleepCounter 
	global protocolSent
        # get the goal array status list        
        # data = str(data)
        current_state = data
        # send goals when the sprayer is off and we are at the goal           
        if goodSendFlag(data) and current_state != prev_state and  i < len(navGoalArray):
                sendNavGoal(navGoalArray)
        # in the case we pressed launch protocol again you will need to send the goal once more

        prev_state = current_state

	
def send_nav_goals():
	global navGoalArray
        rospy.init_node('send_nav_goals', anonymous=True)
        # populate the navGoalArray with goals
        generateNavGoals(navGoalArray,'johnny_boy')
        rospy.sleep(2.5)
        # SENDS ONE NAV GOAL 
        #sendNavGoal(navGoalArray)
        rospy.Subscriber("launch_cmds", String, launchCmdCheckNavGoals)
        rospy.Subscriber("spray_status", String, navGoalCallback)
        rospy.spin()

if __name__ == '__main__':
	try:
		send_nav_goals()
	except rospy.ROSInterruptException:
		print('FAILED NAV GOALS')
		pass


