;; Auto-generated. Do not edit!


(when (boundp 'sanitation_msgs::solution)
  (if (not (find-package "SANITATION_MSGS"))
    (make-package "SANITATION_MSGS"))
  (shadow 'solution (find-package "SANITATION_MSGS")))
(unless (find-package "SANITATION_MSGS::SOLUTION")
  (make-package "SANITATION_MSGS::SOLUTION"))

(in-package "ROS")
;;//! \htmlinclude solution.msg.html


(defclass sanitation_msgs::solution
  :super ros::object
  :slots (_status _runtime ))

(defmethod sanitation_msgs::solution
  (:init
   (&key
    ((:status __status) "")
    ((:runtime __runtime) "")
    )
   (send-super :init)
   (setq _status (string __status))
   (setq _runtime (string __runtime))
   self)
  (:status
   (&optional __status)
   (if __status (setq _status __status)) _status)
  (:runtime
   (&optional __runtime)
   (if __runtime (setq _runtime __runtime)) _runtime)
  (:serialization-length
   ()
   (+
    ;; string _status
    4 (length _status)
    ;; string _runtime
    4 (length _runtime)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _status
       (write-long (length _status) s) (princ _status s)
     ;; string _runtime
       (write-long (length _runtime) s) (princ _runtime s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _status
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _status (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _runtime
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _runtime (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(setf (get sanitation_msgs::solution :md5sum-) "cccbed84ab87ac04d9a21ce3df5e3ac7")
(setf (get sanitation_msgs::solution :datatype-) "sanitation_msgs/solution")
(setf (get sanitation_msgs::solution :definition-)
      "string status
string runtime

")



(provide :sanitation_msgs/solution "cccbed84ab87ac04d9a21ce3df5e3ac7")


