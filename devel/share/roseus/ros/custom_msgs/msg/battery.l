;; Auto-generated. Do not edit!


(when (boundp 'custom_msgs::battery)
  (if (not (find-package "CUSTOM_MSGS"))
    (make-package "CUSTOM_MSGS"))
  (shadow 'battery (find-package "CUSTOM_MSGS")))
(unless (find-package "CUSTOM_MSGS::BATTERY")
  (make-package "CUSTOM_MSGS::BATTERY"))

(in-package "ROS")
;;//! \htmlinclude battery.msg.html


(defclass custom_msgs::battery
  :super ros::object
  :slots (_status _runtime _voltage _percentage ))

(defmethod custom_msgs::battery
  (:init
   (&key
    ((:status __status) "")
    ((:runtime __runtime) "")
    ((:voltage __voltage) 0.0)
    ((:percentage __percentage) 0.0)
    )
   (send-super :init)
   (setq _status (string __status))
   (setq _runtime (string __runtime))
   (setq _voltage (float __voltage))
   (setq _percentage (float __percentage))
   self)
  (:status
   (&optional __status)
   (if __status (setq _status __status)) _status)
  (:runtime
   (&optional __runtime)
   (if __runtime (setq _runtime __runtime)) _runtime)
  (:voltage
   (&optional __voltage)
   (if __voltage (setq _voltage __voltage)) _voltage)
  (:percentage
   (&optional __percentage)
   (if __percentage (setq _percentage __percentage)) _percentage)
  (:serialization-length
   ()
   (+
    ;; string _status
    4 (length _status)
    ;; string _runtime
    4 (length _runtime)
    ;; float32 _voltage
    4
    ;; float32 _percentage
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _status
       (write-long (length _status) s) (princ _status s)
     ;; string _runtime
       (write-long (length _runtime) s) (princ _runtime s)
     ;; float32 _voltage
       (sys::poke _voltage (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _percentage
       (sys::poke _percentage (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _status
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _status (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _runtime
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _runtime (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; float32 _voltage
     (setq _voltage (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _percentage
     (setq _percentage (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get custom_msgs::battery :md5sum-) "0f9f5f64476a27dee61da6b98eac1a1c")
(setf (get custom_msgs::battery :datatype-) "custom_msgs/battery")
(setf (get custom_msgs::battery :definition-)
      "string status
string runtime
float32 voltage
float32 percentage

")



(provide :custom_msgs/battery "0f9f5f64476a27dee61da6b98eac1a1c")


