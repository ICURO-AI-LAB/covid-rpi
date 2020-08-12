#!/usr/bin/env python 

# license removed for brevity
from twilio.rest import Client 
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import BatteryState
from custom_msgs.msg import battery, solution
from sanitation_control.srv import *


#
#def send_twilio_msg(req):
#	global voltage
# 	global percentage
#	global flag 
#		
#	status = data
#	voltage = status.voltage
#	percentage = (status.percentage)*100	
#
#	if not flag:
#
#		print "Testing"
#		print str(voltage)
#		print str(percentage)
#		flag = 1
#		
#		account = "ACd2ef8341685a82c7383519c77688b3c1"
#                token = "0a8a9269227957cfdc4e35f328127860"		
#	
#		client = Client(account,token)
#
#		voltage_string = str(voltage)
#		percentage_string = str(percentage)
#			
#		system_string = "\n Hello Bipin. \n " + "Battery Level:" + voltage_string[:5] + "V  \n" + "Battery Percentage:" + percentage_string[:5] + "%"
# 
#		message = client.messages.create(to="+14084012774", from_="+16157518411", body=system_string) 
#		
#		#message = client.messages.create(to="+13098689834", from_="+16157518411", body=system_string) 
#		
#		print(message.sid)



def handle_add_two_ints(req):
	print("Returning [%s + %s = %s]"%(req.a, req.b, (req.a + req.b)))
	return AddTwoIntsResponse(req.a + req.b)
	

def twilio_service():	
	rospy.init_node('twilio_service', anonymous=True)
	s = rospy.Service('twilio_service', AddTwoInts, handle_add_two_ints)
	print("Ready to add two ints.")
	sub_once = None
	
	#rospy.Subscriber("/battery_level", battery, callback, sub_once)
	#rospy.Subscriber("/solution_level", solution, callback, sub_once)

	global voltage
	global percentage
		
	rospy.spin()


if __name__ == '__main__':
	try:
		twilio_service()
	except rospy.ROSInterruptException:
 		pass
