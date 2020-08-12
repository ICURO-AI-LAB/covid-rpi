;; Auto-generated. Do not edit!


(when (boundp 'sanitation_control::trigger_text)
  (if (not (find-package "SANITATION_CONTROL"))
    (make-package "SANITATION_CONTROL"))
  (shadow 'trigger_text (find-package "SANITATION_CONTROL")))
(unless (find-package "SANITATION_CONTROL::TRIGGER_TEXT")
  (make-package "SANITATION_CONTROL::TRIGGER_TEXT"))
(unless (find-package "SANITATION_CONTROL::TRIGGER_TEXTREQUEST")
  (make-package "SANITATION_CONTROL::TRIGGER_TEXTREQUEST"))
(unless (find-package "SANITATION_CONTROL::TRIGGER_TEXTRESPONSE")
  (make-package "SANITATION_CONTROL::TRIGGER_TEXTRESPONSE"))

(in-package "ROS")





(defclass sanitation_control::trigger_textRequest
  :super ros::object
  :slots ())

(defmethod sanitation_control::trigger_textRequest
  (:init
   (&key
    )
   (send-super :init)
   self)
  (:serialization-length
   ()
   (+
    0
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;;
   self)
  )

(defclass sanitation_control::trigger_textResponse
  :super ros::object
  :slots (_succeeded _message ))

(defmethod sanitation_control::trigger_textResponse
  (:init
   (&key
    ((:succeeded __succeeded) nil)
    ((:message __message) "")
    )
   (send-super :init)
   (setq _succeeded __succeeded)
   (setq _message (string __message))
   self)
  (:succeeded
   (&optional __succeeded)
   (if __succeeded (setq _succeeded __succeeded)) _succeeded)
  (:message
   (&optional __message)
   (if __message (setq _message __message)) _message)
  (:serialization-length
   ()
   (+
    ;; bool _succeeded
    1
    ;; string _message
    4 (length _message)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _succeeded
       (if _succeeded (write-byte -1 s) (write-byte 0 s))
     ;; string _message
       (write-long (length _message) s) (princ _message s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _succeeded
     (setq _succeeded (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; string _message
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _message (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass sanitation_control::trigger_text
  :super ros::object
  :slots ())

(setf (get sanitation_control::trigger_text :md5sum-) "92f07022ad10c1e4ff936618bca1e212")
(setf (get sanitation_control::trigger_text :datatype-) "sanitation_control/trigger_text")
(setf (get sanitation_control::trigger_text :request) sanitation_control::trigger_textRequest)
(setf (get sanitation_control::trigger_text :response) sanitation_control::trigger_textResponse)

(defmethod sanitation_control::trigger_textRequest
  (:response () (instance sanitation_control::trigger_textResponse :init)))

(setf (get sanitation_control::trigger_textRequest :md5sum-) "92f07022ad10c1e4ff936618bca1e212")
(setf (get sanitation_control::trigger_textRequest :datatype-) "sanitation_control/trigger_textRequest")
(setf (get sanitation_control::trigger_textRequest :definition-)
      "---
bool succeeded
string message

")

(setf (get sanitation_control::trigger_textResponse :md5sum-) "92f07022ad10c1e4ff936618bca1e212")
(setf (get sanitation_control::trigger_textResponse :datatype-) "sanitation_control/trigger_textResponse")
(setf (get sanitation_control::trigger_textResponse :definition-)
      "---
bool succeeded
string message

")



(provide :sanitation_control/trigger_text "92f07022ad10c1e4ff936618bca1e212")


