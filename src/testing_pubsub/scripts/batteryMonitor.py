#!/usr/bin/env python
import serial
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import BatteryState
 
#ser = serial.Serial('/dev/ttyUSB0', baudrate=9600)


pub = rospy.Publisher('battery_level', String, queue_size=1)

def callback(data):
	#rospy.loginfo(rospy.get_caller_id() + "I heard %s", data)
	global pub
	status = data

	voltage = status.voltage
	percentage = status.percentage 
	
	print '------battery_info------'
	v_string = voltage, 'V' 
	p_string = percentage, '%'
	print v_string
	print p_string
	print '------------------------'

	pub.publish("------battery_info------")
	#pub.publish(v_string)
	#pub.publish(p_string)
	pub.publish("------------------------")
        rospy.sleep(1)

def batteryMonitor():
       	rospy.init_node('batteryMonitor', anonymous=True)
	rospy.Subscriber("/battery_state", BatteryState, callback)	
	rospy.spin()
  	rate = rospy.Rate(1) # 1hz

if __name__ == '__main__':   
	batteryMonitor()
