; Auto-generated. Do not edit!


(cl:in-package sysinfo-msg)


;//! \htmlinclude ostmsg.msg.html

(cl:defclass <ostmsg> (roslisp-msg-protocol:ros-message)
  ((state
    :reader state
    :initarg :state
    :type cl:fixnum
    :initform 0))
)

(cl:defclass ostmsg (<ostmsg>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ostmsg>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ostmsg)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name sysinfo-msg:<ostmsg> is deprecated: use sysinfo-msg:ostmsg instead.")))

(cl:ensure-generic-function 'state-val :lambda-list '(m))
(cl:defmethod state-val ((m <ostmsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sysinfo-msg:state-val is deprecated.  Use sysinfo-msg:state instead.")
  (state m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ostmsg>) ostream)
  "Serializes a message object of type '<ostmsg>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'state)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ostmsg>) istream)
  "Deserializes a message object of type '<ostmsg>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'state)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ostmsg>)))
  "Returns string type for a message object of type '<ostmsg>"
  "sysinfo/ostmsg")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ostmsg)))
  "Returns string type for a message object of type 'ostmsg"
  "sysinfo/ostmsg")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ostmsg>)))
  "Returns md5sum for a message object of type '<ostmsg>"
  "800f34bc468def1d86e2d42bea5648c0")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ostmsg)))
  "Returns md5sum for a message object of type 'ostmsg"
  "800f34bc468def1d86e2d42bea5648c0")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ostmsg>)))
  "Returns full string definition for message of type '<ostmsg>"
  (cl:format cl:nil "uint8 state~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ostmsg)))
  "Returns full string definition for message of type 'ostmsg"
  (cl:format cl:nil "uint8 state~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ostmsg>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ostmsg>))
  "Converts a ROS message object to a list"
  (cl:list 'ostmsg
    (cl:cons ':state (state msg))
))
