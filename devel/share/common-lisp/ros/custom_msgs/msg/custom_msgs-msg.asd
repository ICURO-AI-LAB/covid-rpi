
(cl:in-package :asdf)

(defsystem "custom_msgs-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "bat_and_sol" :depends-on ("_package_bat_and_sol"))
    (:file "_package_bat_and_sol" :depends-on ("_package"))
    (:file "battery" :depends-on ("_package_battery"))
    (:file "_package_battery" :depends-on ("_package"))
    (:file "solution" :depends-on ("_package_solution"))
    (:file "_package_solution" :depends-on ("_package"))
  ))