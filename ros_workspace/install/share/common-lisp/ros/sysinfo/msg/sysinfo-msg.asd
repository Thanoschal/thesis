
(cl:in-package :asdf)

(defsystem "sysinfo-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "ostmsg" :depends-on ("_package_ostmsg"))
    (:file "_package_ostmsg" :depends-on ("_package"))
  ))