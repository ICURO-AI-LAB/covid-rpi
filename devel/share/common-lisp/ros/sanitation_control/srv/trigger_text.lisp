; Auto-generated. Do not edit!


(cl:in-package sanitation_control-srv)


;//! \htmlinclude trigger_text-request.msg.html

(cl:defclass <trigger_text-request> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass trigger_text-request (<trigger_text-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <trigger_text-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'trigger_text-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name sanitation_control-srv:<trigger_text-request> is deprecated: use sanitation_control-srv:trigger_text-request instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <trigger_text-request>) ostream)
  "Serializes a message object of type '<trigger_text-request>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <trigger_text-request>) istream)
  "Deserializes a message object of type '<trigger_text-request>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<trigger_text-request>)))
  "Returns string type for a service object of type '<trigger_text-request>"
  "sanitation_control/trigger_textRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'trigger_text-request)))
  "Returns string type for a service object of type 'trigger_text-request"
  "sanitation_control/trigger_textRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<trigger_text-request>)))
  "Returns md5sum for a message object of type '<trigger_text-request>"
  "92f07022ad10c1e4ff936618bca1e212")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'trigger_text-request)))
  "Returns md5sum for a message object of type 'trigger_text-request"
  "92f07022ad10c1e4ff936618bca1e212")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<trigger_text-request>)))
  "Returns full string definition for message of type '<trigger_text-request>"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'trigger_text-request)))
  "Returns full string definition for message of type 'trigger_text-request"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <trigger_text-request>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <trigger_text-request>))
  "Converts a ROS message object to a list"
  (cl:list 'trigger_text-request
))
;//! \htmlinclude trigger_text-response.msg.html

(cl:defclass <trigger_text-response> (roslisp-msg-protocol:ros-message)
  ((succeeded
    :reader succeeded
    :initarg :succeeded
    :type cl:boolean
    :initform cl:nil)
   (message
    :reader message
    :initarg :message
    :type cl:string
    :initform ""))
)

(cl:defclass trigger_text-response (<trigger_text-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <trigger_text-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'trigger_text-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name sanitation_control-srv:<trigger_text-response> is deprecated: use sanitation_control-srv:trigger_text-response instead.")))

(cl:ensure-generic-function 'succeeded-val :lambda-list '(m))
(cl:defmethod succeeded-val ((m <trigger_text-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sanitation_control-srv:succeeded-val is deprecated.  Use sanitation_control-srv:succeeded instead.")
  (succeeded m))

(cl:ensure-generic-function 'message-val :lambda-list '(m))
(cl:defmethod message-val ((m <trigger_text-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sanitation_control-srv:message-val is deprecated.  Use sanitation_control-srv:message instead.")
  (message m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <trigger_text-response>) ostream)
  "Serializes a message object of type '<trigger_text-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'succeeded) 1 0)) ostream)
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'message))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'message))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <trigger_text-response>) istream)
  "Deserializes a message object of type '<trigger_text-response>"
    (cl:setf (cl:slot-value msg 'succeeded) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'message) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'message) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<trigger_text-response>)))
  "Returns string type for a service object of type '<trigger_text-response>"
  "sanitation_control/trigger_textResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'trigger_text-response)))
  "Returns string type for a service object of type 'trigger_text-response"
  "sanitation_control/trigger_textResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<trigger_text-response>)))
  "Returns md5sum for a message object of type '<trigger_text-response>"
  "92f07022ad10c1e4ff936618bca1e212")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'trigger_text-response)))
  "Returns md5sum for a message object of type 'trigger_text-response"
  "92f07022ad10c1e4ff936618bca1e212")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<trigger_text-response>)))
  "Returns full string definition for message of type '<trigger_text-response>"
  (cl:format cl:nil "bool succeeded~%string message~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'trigger_text-response)))
  "Returns full string definition for message of type 'trigger_text-response"
  (cl:format cl:nil "bool succeeded~%string message~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <trigger_text-response>))
  (cl:+ 0
     1
     4 (cl:length (cl:slot-value msg 'message))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <trigger_text-response>))
  "Converts a ROS message object to a list"
  (cl:list 'trigger_text-response
    (cl:cons ':succeeded (succeeded msg))
    (cl:cons ':message (message msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'trigger_text)))
  'trigger_text-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'trigger_text)))
  'trigger_text-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'trigger_text)))
  "Returns string type for a service object of type '<trigger_text>"
  "sanitation_control/trigger_text")