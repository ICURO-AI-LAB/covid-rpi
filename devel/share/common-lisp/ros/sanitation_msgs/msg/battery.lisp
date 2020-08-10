; Auto-generated. Do not edit!


(cl:in-package sanitation_msgs-msg)


;//! \htmlinclude battery.msg.html

(cl:defclass <battery> (roslisp-msg-protocol:ros-message)
  ((status
    :reader status
    :initarg :status
    :type cl:string
    :initform "")
   (runtime
    :reader runtime
    :initarg :runtime
    :type cl:string
    :initform "")
   (voltage
    :reader voltage
    :initarg :voltage
    :type cl:float
    :initform 0.0)
   (percentage
    :reader percentage
    :initarg :percentage
    :type cl:float
    :initform 0.0))
)

(cl:defclass battery (<battery>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <battery>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'battery)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name sanitation_msgs-msg:<battery> is deprecated: use sanitation_msgs-msg:battery instead.")))

(cl:ensure-generic-function 'status-val :lambda-list '(m))
(cl:defmethod status-val ((m <battery>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sanitation_msgs-msg:status-val is deprecated.  Use sanitation_msgs-msg:status instead.")
  (status m))

(cl:ensure-generic-function 'runtime-val :lambda-list '(m))
(cl:defmethod runtime-val ((m <battery>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sanitation_msgs-msg:runtime-val is deprecated.  Use sanitation_msgs-msg:runtime instead.")
  (runtime m))

(cl:ensure-generic-function 'voltage-val :lambda-list '(m))
(cl:defmethod voltage-val ((m <battery>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sanitation_msgs-msg:voltage-val is deprecated.  Use sanitation_msgs-msg:voltage instead.")
  (voltage m))

(cl:ensure-generic-function 'percentage-val :lambda-list '(m))
(cl:defmethod percentage-val ((m <battery>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sanitation_msgs-msg:percentage-val is deprecated.  Use sanitation_msgs-msg:percentage instead.")
  (percentage m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <battery>) ostream)
  "Serializes a message object of type '<battery>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'status))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'status))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'runtime))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'runtime))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'voltage))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'percentage))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <battery>) istream)
  "Deserializes a message object of type '<battery>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'status) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'status) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'runtime) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'runtime) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'voltage) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'percentage) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<battery>)))
  "Returns string type for a message object of type '<battery>"
  "sanitation_msgs/battery")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'battery)))
  "Returns string type for a message object of type 'battery"
  "sanitation_msgs/battery")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<battery>)))
  "Returns md5sum for a message object of type '<battery>"
  "0f9f5f64476a27dee61da6b98eac1a1c")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'battery)))
  "Returns md5sum for a message object of type 'battery"
  "0f9f5f64476a27dee61da6b98eac1a1c")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<battery>)))
  "Returns full string definition for message of type '<battery>"
  (cl:format cl:nil "string status~%string runtime~%float32 voltage~%float32 percentage~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'battery)))
  "Returns full string definition for message of type 'battery"
  (cl:format cl:nil "string status~%string runtime~%float32 voltage~%float32 percentage~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <battery>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'status))
     4 (cl:length (cl:slot-value msg 'runtime))
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <battery>))
  "Converts a ROS message object to a list"
  (cl:list 'battery
    (cl:cons ':status (status msg))
    (cl:cons ':runtime (runtime msg))
    (cl:cons ':voltage (voltage msg))
    (cl:cons ':percentage (percentage msg))
))
