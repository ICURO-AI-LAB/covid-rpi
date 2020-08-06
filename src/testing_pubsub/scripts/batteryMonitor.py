#!/usr/bin/env python
import serial
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import BatteryState
 
#ser = serial.Serial('/dev/ttyUSB0', baudrate=9600)


def callback(data):
	#rospy.loginfo(rospy.get_caller_id() + "I heard %s", data)

	status = data

	voltage = status.voltage
	percentage = status.percentage 
	
	print '------'
#	print status
	print voltage 
	print percentage
	print '------'

	#command = data.data

	#print command 
 
	#ser.write(command.encode())  

	#command = data.data 

	#if command != last_command: 
	#	ser.write(command.encode())	
	#	last_command = command 
    	


def batteryMonitor():
	rospy.init_node('batteryMonitor', anonymous=True)
 	rospy.Subscriber("/battery_state", BatteryState, callback)

	rospy.spin()
  
if __name__ == '__main__':   
	batteryMonitor()
