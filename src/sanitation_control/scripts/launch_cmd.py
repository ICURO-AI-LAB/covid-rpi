#!/usr/bin/env python 

# license removed for brevity
import rospy
import sys
from std_msgs.msg import String


if __name__ == '__main__':
	if (len(sys.argv) != 2):
		print('Usage: python launch_cmd.py [launch cmd]')
	else:	
		pub = rospy.Publisher('launch_cmds', String, queue_size=1)
		rospy.init_node('talker', anonymous=True)
		#rospy.sleep(1.0)
		rospy.loginfo(sys.argv[1])
		pub.publish(sys.argv[1])	
