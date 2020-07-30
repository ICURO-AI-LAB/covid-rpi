#!/usr/bin/env python 

# license removed for brevity
import rospy
from std_msgs.msg import String

def talker():
        pub = rospy.Publisher('chatter', String, queue_size=1)
        rospy.init_node('turnoff', anonymous=True)
        rate = rospy.Rate(10) # 10hz
        


        #while not rospy.is_shutdown():
                #hello_str = "hello world %s" % rospy.get_time()
                #rospy.loginfo(hello_str)
                #pub.publish(hello_str)
                #rate.sleep()
                
	#command_str = "a,0,0,1,1,1,1,0,0\n" 
	command_str = "a,0,0,0,0,0,0,0,0\n" #All off
	
	rospy.loginfo(command_str)
	pub.publish(command_str)
	rate.sleep()

if __name__ == '__main__':
        try:
                talker()
        except rospy.ROSInterruptException:
                pass

