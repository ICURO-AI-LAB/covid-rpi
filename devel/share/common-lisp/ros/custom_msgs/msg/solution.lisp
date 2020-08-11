; Auto-generated. Do not edit!


(cl:in-package custom_msgs-msg)


;//! \htmlinclude solution.msg.html

(cl:defclass <solution> (roslisp-msg-protocol:ros-message)
  ((status
    :reader status
    :initarg :status
    :type cl:string
    :initform "")
   (runtime
    :reader runtime
    :initarg :runtime
    :type cl:string
    :initform ""))
)

(cl:defclass solution (<solution>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <solution>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'solution)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name custom_msgs-msg:<solution> is deprecated: use custom_msgs-msg:solution instead.")))

(cl:ensure-generic-function 'status-val :lambda-list '(m))
(cl:defmethod status-val ((m <solution>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader custom_msgs-msg:status-val is deprecated.  Use custom_msgs-msg:status instead.")
  (status m))

(cl:ensure-generic-function 'runtime-val :lambda-list '(m))
(cl:defmethod runtime-val ((m <solution>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader custom_msgs-msg:runtime-val is deprecated.  Use custom_msgs-msg:runtime instead.")
  (runtime m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <solution>) ostream)
  "Serializes a message object of type '<solution>"
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
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <solution>) istream)
  "Deserializes a message object of type '<solution>"
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
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<solution>)))
  "Returns string type for a message object of type '<solution>"
  "custom_msgs/solution")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'solution)))
  "Returns string type for a message object of type 'solution"
  "custom_msgs/solution")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<solution>)))
  "Returns md5sum for a message object of type '<solution>"
  "cccbed84ab87ac04d9a21ce3df5e3ac7")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'solution)))
  "Returns md5sum for a message object of type 'solution"
  "cccbed84ab87ac04d9a21ce3df5e3ac7")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<solution>)))
  "Returns full string definition for message of type '<solution>"
  (cl:format cl:nil "string status~%string runtime~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'solution)))
  "Returns full string definition for message of type 'solution"
  (cl:format cl:nil "string status~%string runtime~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <solution>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'status))
     4 (cl:length (cl:slot-value msg 'runtime))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <solution>))
  "Converts a ROS message object to a list"
  (cl:list 'solution
    (cl:cons ':status (status msg))
    (cl:cons ':runtime (runtime msg))
))
