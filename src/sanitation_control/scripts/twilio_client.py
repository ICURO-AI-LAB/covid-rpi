#!/usr/bin/env python 

# license removed for brevity
#from twilio.rest import Client 
import rospy
from std_msgs.msg import String
from custom_msgs.msg import bat_and_sol
from sanitation_control.srv import *

def trigger_text_client():
    rospy.wait_for_service('twilio_service')
    try:
        trigger_response = rospy.ServiceProxy('twilio_service', trigger_text)
        resp = trigger_response()
        return (
		resp.succeeded, resp.message
	)

    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def usage():
    	return "Sending Text"
	#return "%s [x y]"%sys.argv[0]

if __name__ == "__main__":
	print(usage())
	print("Testing: %r %s"%(trigger_text_client()))    


    #if len(sys.argv) == 3:
     #   x = int(sys.argv[1])
     #   y = int(sys.argv[2])
    #else:
     #   print(usage())
     #   sys.exit(1)
	
    #print("Requesting %s+%s"%(x, y))
    #print("%s + %s = %s"%(x, y, add_two_ints_client(x, y)))
