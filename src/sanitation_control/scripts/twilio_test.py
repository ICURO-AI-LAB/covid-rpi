#!/usr/bin/env python 

# license removed for brevity
from twilio.rest import Client 
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import BatteryState
from custom_msgs.msg import battery, solution, bat_and_sol

voltage = 0
percentage = 0
solution_level = '0'
flag = 0



def callback(data):
	global voltage
 	global percentage
	global flag 
		
	voltage = data.voltage
	percentage = data.battery_percentage	
	battery_status = data.batStatus
	solution_status = data.solStatus

	if not flag:

		print "Testing"
		print str(voltage)
		print str(percentage)
		flag = 1
		account = "ACd2ef8341685a82c7383519c77688b3c1"
		token = "0a8a9269227957cfdc4e35f328127860"
	
		client = Client(account,token)

		#message = client.messages.create(to="+14084012774", from_="+16157518411", body="Hello Sir!") 
		voltage_string = str(voltage)
		percentage_string = str(percentage)
			
		system_string = "Hello. \n " + battery_status + "\n Battery Level: " + voltage_string[:5] + "V  \n" + "Battery Percentage: " + percentage_string[:5] + "%\n" + solution_status

 
		#message = client.messages.create(to="+14084012774", from_="+16157518411", body=system_string) 
		message = client.messages.create(to="+14084012774", from_="+16157518411", body=system_string) 
		
		#message = client.messages.create(to="+13098689834", from_="+16157518411", body=system_string) 
		

		print(message.sid)



		
	
	#subscriber.unregister()

#def callback2(data, subscriber):
#	global solution_level
	
#	solution_status = data
#	solution_level =  solution_status.status
#	subscriber.unregister()


def twilio_test():	
	pub = rospy.Publisher('twilio_test', String, queue_size=1)
	rospy.init_node('twilio_test', anonymous=True)

	sub_once = None
	
	#rospy.Subscriber("/battery_level", battery, callback, sub_once)
	rospy.Subscriber("/battery_and_solution", bat_and_sol, callback, sub_once)

	global voltage
	global percentage
		
	rospy.spin()


if __name__ == '__main__':
	try:
		twilio_test()
	except rospy.ROSInterruptException:
 		pass
