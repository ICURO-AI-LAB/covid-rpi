#!/usr/bin/env python
import rospy
import time
import rospy
from geometry_msgs.msg import PoseStamped # for our crude approach

NUM_GOALS = 5
#rospy.init_node('generateNavGoals', anonymous=True)

def genPoseStamped(px,py,pz,ox,oy,oz,ow,i):
	nav_goal = PoseStamped()
	nav_goal.header.frame_id = 'map'
	nav_goal.header.seq = i
	nav_goal.header.stamp = rospy.Time.now()
	nav_goal.pose.position.x = px
	nav_goal.pose.position.y = py
	nav_goal.pose.position.z = pz
	nav_goal.pose.orientation.x = ox
	nav_goal.pose.orientation.y = oy
	nav_goal.pose.orientation.z = oz
	nav_goal.pose.orientation.w = ow
	return nav_goal

# sets up predefined goals for navigation and puts them in the navGoalArray
def generateNavGoals(navGoalArray,robotType):

	#for i in range(NUM_GOALS):
	#	navGoalArray.append(genPoseStamped(0,0,0,0,0,0,0,i))
	
	if (robotType == 'johnny_boy'):
		# waypoint 1: first spray before sexy robot
		navGoalArray.append(genPoseStamped( -3.102, -1.482, 0.0,   0.0, 0.0, 0.304, 0.953 , 1))
		# waypoint 2: next spray next to sexy robot
		navGoalArray.append(genPoseStamped( -2.102, -1.482, 0.0,   0.0, 0.0, 0.304, 0.953 , 2))
		# waypoint 3: facing closet door handle
		navGoalArray.append(genPoseStamped( 2.968, -3.65, 0.0,   0.0, 0.0, 0.842, 0.539 , 3))
		# waypoint 4: beginning second spray
		navGoalArray.append(genPoseStamped( 4.580, 0.665, 0.0,   0.0, 0.0, 0.969, 0.246 , 4))
		# waypoint 5: end of second spray
		navGoalArray.append(genPoseStamped( 0.856, 3.3, 0.0,   0.0, 0.0, 0.982, 0.189 , 5))
		# waypoint 6: show off to the haters
		navGoalArray.append(genPoseStamped( 5.143, -2.049, 0.0,   0.0, 0.0, -0.246, 0.969 ,6))
	
	elif (robotType == 'johnny_red'):
		# waypoint 1: next spray next to sexy robot
		navGoalArray.append(genPoseStamped( -1.804, -1.207, 0.0,   0.0, 0.0, 0.179, 0.984, 1))
		# waypoint 2: for first tables
		navGoalArray.append(genPoseStamped( 4.276, -1.107, 0.0,   0.0, 0.0, -0.044, 0.999, 2))
		# waypoint 3B: for second tables
		#navGoalArray.append(genPoseStamped( 4.130, -1.308, 0.0,   0.0, 0.0, -0.0457, 0.890, 3))
		# waypoint 6: show off to the haters
		# navGoalArray.append(genPoseStamped( 5.143, -1.049, 0.0,   0.0, 0.0, -0.246, 0.969 ,4))
		# waypoint 6: show off to the haters
		navGoalArray.append(genPoseStamped( 4.349, -1.479, 0.0,   0.0, 0.0, -0.508, 0.862,3))



	else:
		print('specify robot type in generate Nav Goals!')
		exit()

if __name__ == '__main__':
	pass
