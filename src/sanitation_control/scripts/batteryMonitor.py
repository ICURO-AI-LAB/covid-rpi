#!/usr/bin/env python
import serial
import rospy
import time
from datetime import datetime 
from std_msgs.msg import String
from sanitation_msgs.msg import battery
from sensor_msgs.msg import BatteryState
 
#ser = serial.Serial('/dev/ttyUSB0', baudrate=9600)


pub = rospy.Publisher('battery_level', battery, queue_size=1)

def callback(data):

	global pub
	status = data
	battery_message = battery()
	
	t = time.localtime()
	current_time = time.strftime("%D-%H:%M:%S",t)

		

	voltage = status.voltage
	percentage = status.percentage 
	
	#print '------battery_info-------'
	#print ("Current Time =", current_time)
	#v_string = str(voltage) + " V" 
	#p_string = str(percentage) + " %"
	#print v_string
	#print p_string
	#print '------------------------'


	if (voltage > 25.5):
		battery_message.status = "------ battery is good ------"
	else:
		battery_message.status = "------ battery is low -------"

	battery_message.runtime = current_time
	battery_message.voltage = voltage
	battery_message.percentage = percentage

	pub.publish(battery_message)
	#pub.publish("------battery_info------")
	#pub.publish(current_time)
	#pub.publish(v_string)
	#pub.publish(p_string)
	#pub.publish("------------------------")
        #rospy.sleep(1)

def batteryMonitor():
       	rospy.init_node('batteryMonitor', anonymous=True)
	rospy.Subscriber("/battery_state", BatteryState, callback)	
	rospy.spin()
  	rate = rospy.Rate(1) # 1hz

if __name__ == '__main__':   
	batteryMonitor()
