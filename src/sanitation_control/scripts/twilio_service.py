#!/usr/bin/env python 

# license removed for brevity
from twilio.rest import Client 
import os
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import BatteryState
from custom_msgs.msg import bat_and_sol
from sanitation_control.srv import *

TEXT_SENT = False 
MSG_FLAG = False
#subscriber  =  rospy.Subscriber("/battery_and_solution", bat_and_sol, callback, sub_once)

def callback(data):
	global voltage
	global percentage
	global flag 
	global TEXT_SENT
	global MSG_FLAG
	global subscriber
	
	print "Callback called"	

	time = data.runtime
	voltage = data.voltage
	battery_percentage = data.battery_percentage
	battery_status = data.batStatus
	solution_status = data.solStatus


	if not MSG_FLAG:	
		account = "ACd2ef8341685a82c7383519c77688b3c1"
                token = "0a8a9269227957cfdc4e35f328127860"		
	
		client = Client(account,token)

		voltage_string = str(voltage)
		percentage_string = str(battery_percentage)
		
		system_string = "Hello. \n " + battery_status + "\n Battery Level: " + voltage_string[:5] + "V  \n" + "Battery Percentage: " + percentage_string[:5] + "%\n" + solution_status
		
		print system_string	
	
		message = client.messages.create(to="+14084012774", from_="+16157518411", body=system_string) 
			
		print(message.sid)
		MSG_FLAG = True
		TEXT_SENT = True

	subscriber.unregister()
	#print("Returning [%s + %s = %s]"%(req.a, req.b, (req.a + req.b)))
	#return AddTwoIntsResponse("Succeeded")
	


def handle_twilio_text(request):
	global TEXT_SENT
	global subscriber
	global MSG_FLAG
	
	MSG_FLAG = False
	sub_once = None
	subscriber = rospy.Subscriber("/battery_and_solution", bat_and_sol, callback, sub_once)
	"subscribed to topic"
	#while( not TEXT_SENT ):
		#print "Stuck in while"
	#	i = 3
			
	print "Made it"
	return trigger_textResponse(
		succeeded=True, message="Text Sent"
	)

def twilio_service():	
	rospy.init_node('twilio_service', anonymous=True)
	s = rospy.Service('twilio_service', trigger_text, handle_twilio_text)
	print("Ready to send text.")
	sub_once = None
	
	#rospy.Subscriber("/battery_level", battery, callback, sub_once)
	#rospy.Subscriber("/solution_level", solution, callback, sub_once)
		
	rospy.spin()


if __name__ == '__main__':
	try:
		twilio_service()
	except rospy.ROSInterruptException:
 		pass
