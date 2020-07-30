#!/usr/bin/env python 

# license removed for brevity
import rospy
from std_msgs.msg import String

def talker():
        pub = rospy.Publisher('chatter', String, queue_size=1)
        rospy.init_node('turnon', anonymous=True)
        rate = rospy.Rate(10) # 10hz
      
        #command_str = "a,1,1,0,0,1,1,255,0\n"
        #command_str = "a,1,1,1,1,1,1,255,0\n" #All On
	command_str = "a,1,1,1,1,0,0,0,0\n" # All relays on 
		

	rospy.loginfo(command_str)
        pub.publish(command_str)
        rate.sleep()

if __name__ == '__main__':
        try:
		talker()
        except rospy.ROSInterruptException:
                pass
                      
