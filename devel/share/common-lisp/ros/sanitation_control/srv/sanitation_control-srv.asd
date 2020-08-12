
(cl:in-package :asdf)

(defsystem "sanitation_control-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "AddTwoInts" :depends-on ("_package_AddTwoInts"))
    (:file "_package_AddTwoInts" :depends-on ("_package"))
    (:file "trigger_text" :depends-on ("_package_trigger_text"))
    (:file "_package_trigger_text" :depends-on ("_package"))
  ))