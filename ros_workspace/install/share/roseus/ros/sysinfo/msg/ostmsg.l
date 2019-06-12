;; Auto-generated. Do not edit!


(when (boundp 'sysinfo::ostmsg)
  (if (not (find-package "SYSINFO"))
    (make-package "SYSINFO"))
  (shadow 'ostmsg (find-package "SYSINFO")))
(unless (find-package "SYSINFO::OSTMSG")
  (make-package "SYSINFO::OSTMSG"))

(in-package "ROS")
;;//! \htmlinclude ostmsg.msg.html


(defclass sysinfo::ostmsg
  :super ros::object
  :slots (_state ))

(defmethod sysinfo::ostmsg
  (:init
   (&key
    ((:state __state) 0)
    )
   (send-super :init)
   (setq _state (round __state))
   self)
  (:state
   (&optional __state)
   (if __state (setq _state __state)) _state)
  (:serialization-length
   ()
   (+
    ;; uint8 _state
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; uint8 _state
       (write-byte _state s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; uint8 _state
     (setq _state (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;;
   self)
  )

(setf (get sysinfo::ostmsg :md5sum-) "800f34bc468def1d86e2d42bea5648c0")
(setf (get sysinfo::ostmsg :datatype-) "sysinfo/ostmsg")
(setf (get sysinfo::ostmsg :definition-)
      "uint8 state

")



(provide :sysinfo/ostmsg "800f34bc468def1d86e2d42bea5648c0")


