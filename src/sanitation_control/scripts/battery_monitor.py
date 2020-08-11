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
 
filter_size = 20
v_filter = [0]*filter_size 

MAX_VOLTAGE = 26
MIN_VOLTAGE = 22

# linearly map value s within range [a1,a2]
# to range [b1,b2]

def mapRange(s,a1,a2,b1,b2):
	return b1 + ( (s - a1) * (b2 - b1) ) / (a2 - a1)

def callback(magniBatMsg):

	global pub
	global i
	global v_filter
	global filter_size
	global MAX_VOLTAGE
	global MIN_VOTLAGE	

	# create battery message type
	battery_message = battery()
	pub = rospy.Publisher('battery_level', battery, queue_size=1)
	# rate = rospy.Rate(1) # 1 Hz


	t = time.localtime()
	current_time = time.strftime("%D-%H:%M:%S",t)
	
	# array has been filled
	#print('---')
	#for voltage in v_filter:
	#	print(voltage)
	#print('---')


	# only perform the moving average filter after the 
	if ( v_filter[filter_size-1] != 0 ):		

		filtered_voltage = sum(v_filter)/filter_size
		percentage = mapRange(filtered_voltage,MIN_VOLTAGE,MAX_VOLTAGE,0,100)

		if(magniBatMsg.voltage > MAX_VOLTAGE):
			battery_status = "-- Battery is Fully Charged --"
			percentage = 100.0
		elif (magniBatMsg.voltage < MIN_VOTLAGE):
			battery_status = "-- Battery is Low. Please Charge --"
		else:
			battery_status = "-- Battery is Partially Charged --"

		battery_message.runtime = current_time
		battery_message.voltage = filtered_voltage
		battery_message.percentage = percentage
		battery_message.status = battery_status

		# publish current status once we have a filtered output
		pub.publish(battery_message)

	v_filter[i%filter_size] = magniBatMsg.voltage
	i+=1
	
	
def batteryMonitor():
       	rospy.init_node('battery_monitor', anonymous=True)
	rospy.Subscriber("/battery_state", BatteryState, callback)	
	rospy.spin()
  	#rate = rospy.Rate(1) # 1hz

if __name__ == '__main__':   
	batteryMonitor()
