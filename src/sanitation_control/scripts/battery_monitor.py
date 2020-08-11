#!/usr/bin/env python
import serial
import rospy
import time
from datetime import datetime 
from std_msgs.msg import String
from custom_msgs.msg import battery
from sensor_msgs.msg import BatteryState
 

pub = rospy.Publisher('battery_level', battery, queue_size=1)
i = 0

def callback(data):

	global pub
	global i
	global v_filter



	status = data
	battery_message = battery()
	
	t = time.localtime()
	current_time = time.strftime("%D-%H:%M:%S",t)
		
	if(i >= 5 ):	
		print "done"
		filtered_voltage = sum(v_filter)/5
		print filtered_voltage
		i = 0
	else:
		v_filter[i] = status.voltage
		print i
		print v_filter[i]
		i += 1

	#if(status.voltage > 26.5):
	#	voltage  	

	voltage = status.voltage
	percentage = status.percentage

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
       	rospy.init_node('battery_monitor', anonymous=True)
	rospy.Subscriber("/battery_state", BatteryState, callback)	
	rospy.spin()
  	#rate = rospy.Rate(1) # 1hz

if __name__ == '__main__':   
	batteryMonitor()
