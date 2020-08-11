;; Auto-generated. Do not edit!


(when (boundp 'custom_msgs::bat_and_sol)
  (if (not (find-package "CUSTOM_MSGS"))
    (make-package "CUSTOM_MSGS"))
  (shadow 'bat_and_sol (find-package "CUSTOM_MSGS")))
(unless (find-package "CUSTOM_MSGS::BAT_AND_SOL")
  (make-package "CUSTOM_MSGS::BAT_AND_SOL"))

(in-package "ROS")
;;//! \htmlinclude bat_and_sol.msg.html


(defclass custom_msgs::bat_and_sol
  :super ros::object
  :slots (_batStatus _solStatus _runtime _voltage _battery_percentage ))

(defmethod custom_msgs::bat_and_sol
  (:init
   (&key
    ((:batStatus __batStatus) "")
    ((:solStatus __solStatus) "")
    ((:runtime __runtime) "")
    ((:voltage __voltage) 0.0)
    ((:battery_percentage __battery_percentage) 0.0)
    )
   (send-super :init)
   (setq _batStatus (string __batStatus))
   (setq _solStatus (string __solStatus))
   (setq _runtime (string __runtime))
   (setq _voltage (float __voltage))
   (setq _battery_percentage (float __battery_percentage))
   self)
  (:batStatus
   (&optional __batStatus)
   (if __batStatus (setq _batStatus __batStatus)) _batStatus)
  (:solStatus
   (&optional __solStatus)
   (if __solStatus (setq _solStatus __solStatus)) _solStatus)
  (:runtime
   (&optional __runtime)
   (if __runtime (setq _runtime __runtime)) _runtime)
  (:voltage
   (&optional __voltage)
   (if __voltage (setq _voltage __voltage)) _voltage)
  (:battery_percentage
   (&optional __battery_percentage)
   (if __battery_percentage (setq _battery_percentage __battery_percentage)) _battery_percentage)
  (:serialization-length
   ()
   (+
    ;; string _batStatus
    4 (length _batStatus)
    ;; string _solStatus
    4 (length _solStatus)
    ;; string _runtime
    4 (length _runtime)
    ;; float32 _voltage
    4
    ;; float32 _battery_percentage
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _batStatus
       (write-long (length _batStatus) s) (princ _batStatus s)
     ;; string _solStatus
       (write-long (length _solStatus) s) (princ _solStatus s)
     ;; string _runtime
       (write-long (length _runtime) s) (princ _runtime s)
     ;; float32 _voltage
       (sys::poke _voltage (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _battery_percentage
       (sys::poke _battery_percentage (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _batStatus
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _batStatus (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _solStatus
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _solStatus (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _runtime
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _runtime (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; float32 _voltage
     (setq _voltage (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _battery_percentage
     (setq _battery_percentage (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get custom_msgs::bat_and_sol :md5sum-) "5782c79eb06aac24e86dd4fe43a05d5f")
(setf (get custom_msgs::bat_and_sol :datatype-) "custom_msgs/bat_and_sol")
(setf (get custom_msgs::bat_and_sol :definition-)
      "string batStatus
string solStatus
string runtime
float32 voltage
float32 battery_percentage

")



(provide :custom_msgs/bat_and_sol "5782c79eb06aac24e86dd4fe43a05d5f")


