#!/usr/bin/env python
#cense removeid for brevity
import rospy
import re
import sys
import os
from std_msgs.msg import String
#from nav_msgs.msg import Odometry

global recFlag
# send initial pose once we have from the topic we want

def startClean(data):
    global recFlag
    if 'launch' in str(data) and recFlag == False:
        print('LAUNCH CMD RECEIVED, GOOD TO START')
        os.system('roslaunch sanitation_control continuous_spray.launch')
        recFlag = True

def startup():
    global recFlag
    recFlag = False
    rospy.init_node('startupCleanJB', anonymous=True)
    sub = rospy.Subscriber('launch_cmds',String,startClean)
    # idle around until we get data from the pointcloud
    rospy.spin()

if __name__ == '__main__':
    try:
        startup()
    except rospy.ROSInterruptException:
        pass
