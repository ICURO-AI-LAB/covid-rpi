; Auto-generated. Do not edit!


(cl:in-package custom_msgs-msg)


;//! \htmlinclude bat_and_sol.msg.html

(cl:defclass <bat_and_sol> (roslisp-msg-protocol:ros-message)
  ((batStatus
    :reader batStatus
    :initarg :batStatus
    :type cl:string
    :initform "")
   (solStatus
    :reader solStatus
    :initarg :solStatus
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
   (battery_percentage
    :reader battery_percentage
    :initarg :battery_percentage
    :type cl:float
    :initform 0.0))
)

(cl:defclass bat_and_sol (<bat_and_sol>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <bat_and_sol>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'bat_and_sol)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name custom_msgs-msg:<bat_and_sol> is deprecated: use custom_msgs-msg:bat_and_sol instead.")))

(cl:ensure-generic-function 'batStatus-val :lambda-list '(m))
(cl:defmethod batStatus-val ((m <bat_and_sol>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader custom_msgs-msg:batStatus-val is deprecated.  Use custom_msgs-msg:batStatus instead.")
  (batStatus m))

(cl:ensure-generic-function 'solStatus-val :lambda-list '(m))
(cl:defmethod solStatus-val ((m <bat_and_sol>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader custom_msgs-msg:solStatus-val is deprecated.  Use custom_msgs-msg:solStatus instead.")
  (solStatus m))

(cl:ensure-generic-function 'runtime-val :lambda-list '(m))
(cl:defmethod runtime-val ((m <bat_and_sol>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader custom_msgs-msg:runtime-val is deprecated.  Use custom_msgs-msg:runtime instead.")
  (runtime m))

(cl:ensure-generic-function 'voltage-val :lambda-list '(m))
(cl:defmethod voltage-val ((m <bat_and_sol>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader custom_msgs-msg:voltage-val is deprecated.  Use custom_msgs-msg:voltage instead.")
  (voltage m))

(cl:ensure-generic-function 'battery_percentage-val :lambda-list '(m))
(cl:defmethod battery_percentage-val ((m <bat_and_sol>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader custom_msgs-msg:battery_percentage-val is deprecated.  Use custom_msgs-msg:battery_percentage instead.")
  (battery_percentage m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <bat_and_sol>) ostream)
  "Serializes a message object of type '<bat_and_sol>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'batStatus))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'batStatus))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'solStatus))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'solStatus))
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
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'battery_percentage))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <bat_and_sol>) istream)
  "Deserializes a message object of type '<bat_and_sol>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'batStatus) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'batStatus) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'solStatus) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'solStatus) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
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
    (cl:setf (cl:slot-value msg 'battery_percentage) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<bat_and_sol>)))
  "Returns string type for a message object of type '<bat_and_sol>"
  "custom_msgs/bat_and_sol")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'bat_and_sol)))
  "Returns string type for a message object of type 'bat_and_sol"
  "custom_msgs/bat_and_sol")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<bat_and_sol>)))
  "Returns md5sum for a message object of type '<bat_and_sol>"
  "5782c79eb06aac24e86dd4fe43a05d5f")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'bat_and_sol)))
  "Returns md5sum for a message object of type 'bat_and_sol"
  "5782c79eb06aac24e86dd4fe43a05d5f")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<bat_and_sol>)))
  "Returns full string definition for message of type '<bat_and_sol>"
  (cl:format cl:nil "string batStatus~%string solStatus~%string runtime~%float32 voltage~%float32 battery_percentage~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'bat_and_sol)))
  "Returns full string definition for message of type 'bat_and_sol"
  (cl:format cl:nil "string batStatus~%string solStatus~%string runtime~%float32 voltage~%float32 battery_percentage~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <bat_and_sol>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'batStatus))
     4 (cl:length (cl:slot-value msg 'solStatus))
     4 (cl:length (cl:slot-value msg 'runtime))
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <bat_and_sol>))
  "Converts a ROS message object to a list"
  (cl:list 'bat_and_sol
    (cl:cons ':batStatus (batStatus msg))
    (cl:cons ':solStatus (solStatus msg))
    (cl:cons ':runtime (runtime msg))
    (cl:cons ':voltage (voltage msg))
    (cl:cons ':battery_percentage (battery_percentage msg))
))
