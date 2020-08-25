#!/usr/bin/env python
import rospy
import time
from custom_msgs.msg import bat_and_sol
import RPi.GPIO as GPIO
from sensor_msgs.msg import BatteryState

GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.IN)
pub = rospy.Publisher('battery_and_solution',bat_and_sol, queue_size=1)

i = 0 
filter_size = 20
v_filter = [0]*filter_size 

MAX_VOLTAGE = 26.7
WARNING_VOLTAGE = 24
MIN_VOLTAGE = 22
WATER_PIN_NO = 16

# linearly map value s within range [a1,a2]
# to range [b1,b2]

def mapRange(s,a1,a2,b1,b2):
	return b1 + ( (s - a1) * (b2 - b1) ) / (a2 - a1)

def callback(data):

	global pub
	global i
	global v_filter
	global filter_size
	global MAX_VOLTAGE
	global WARNING_VOLTAGE
	global MIN_VOLTAGE	

	# create bat_and_sol message type
	bat_and_sol_message = bat_and_sol()
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

		if(data.voltage > MAX_VOLTAGE):
			battery_status = "-- Battery is Fully Charged --"
			percentage = 100.0
		elif (data.voltage < MIN_VOLTAGE):
			battery_status = "-- Battery is Critically Low. Please Charge Now --"
		elif(data.voltage < WARNING_VOLTAGE):
			battery_status = "-- Battery is Low. Please Charge Soon --"
		else:
			battery_status = "-- Battery is Partially Charged --"

		bat_and_sol_message.runtime = current_time
		bat_and_sol_message.voltage = filtered_voltage
		bat_and_sol_message.battery_percentage = percentage
		bat_and_sol_message.batStatus = battery_status

		# water control
		if GPIO.input(WATER_PIN_NO):
	    		#solution_message.status = "-------Water Level Is Chilling Dawg--------"
			bat_and_sol_message.solStatus = "Solution Level Is Sufficient"
			#print solution_message.status
		else:
   		 	#solution_message.status = " ------Water Level Is Dangerous Dawg---------"
			bat_and_sol_message.solStatus = "Solution Level Is Low, Please Refill"
			#print solution_message.status
		
		# publish current status once we have a filtered output
		pub.publish(bat_and_sol_message)

	v_filter[i%filter_size] = data.voltage
	i+=1
	
	
def bat_and_sol_monitor():
       	rospy.init_node('bat_and_sol_monitor', anonymous=True)
	rospy.Subscriber("/battery_state", BatteryState, callback)	
	rospy.spin()
  	#rate = rospy.Rate(1) # 1hz

if __name__ == '__main__':
	try:
		bat_and_sol_monitor()
	except rospy.ROSInterruptException:
		pass


