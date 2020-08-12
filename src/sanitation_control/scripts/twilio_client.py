#!/usr/bin/env python 

# license removed for brevity
from twilio.rest import Client 
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import BatteryState
from custom_msgs.msg import battery, solution
from sanitation_control.srv import *

def add_two_ints_client(x, y):
    rospy.wait_for_service('twilio_service')
    try:
        add_two_ints = rospy.ServiceProxy('twilio_service', AddTwoInts)
        resp1 = add_two_ints(x, y)
        return resp1.s
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def usage():
    return "%s [x y]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 3:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
    else:
        print(usage())
        sys.exit(1)
    print("Requesting %s+%s"%(x, y))
    print("%s + %s = %s"%(x, y, add_two_ints_client(x, y)))
