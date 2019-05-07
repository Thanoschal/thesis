#!/usr/bin/env python

# TurtleBot must have minimal.launch & amcl_demo.launch
# running prior to starting this script
# For simulation: launch gazebo world & amcl_demo prior to run this script

import rospy
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import actionlib
from actionlib_msgs.msg import *
from geometry_msgs.msg import Pose, Point, Quaternion

class GoToPose():
    
    def __init__(self):
        self.goal_sent = False

	# What to do if shut down (e.g. Ctrl-C or failure)
	rospy.on_shutdown(self.shutdown)
	
	# Tell the action client that we want to spin a thread by default
	self.move_base = actionlib.SimpleActionClient("move_base", MoveBaseAction)
	rospy.loginfo("Wait for the action server to come up")

	# Allow up to 5 seconds for the action server to come up
	self.move_base.wait_for_server(rospy.Duration(5))

    def goto(self, pos, quat):

        # Send a goal
        self.goal_sent = True
        goal = MoveBaseGoal()
        goal.target_pose.header.frame_id = 'map'
        goal.target_pose.header.stamp = rospy.Time.now()
        goal.target_pose.pose = Pose(Point(pos['x'], pos['y'], 0.000),Quaternion(quat['r1'], quat['r2'], quat['r3'], quat['r4']))
        
        # Start moving
        self.move_base.send_goal(goal)

        # Allow TurtleBot up to 60 seconds to complete task
        success = self.move_base.wait_for_result(rospy.Duration(60)) 

        state = self.move_base.get_state()
        result = False

        if success and state == GoalStatus.SUCCEEDED:
            # We made it!
            result = True
        else:
            self.move_base.cancel_goal()

        self.goal_sent = False
        return result

    def shutdown(self):
        if self.goal_sent:
            self.move_base.cancel_goal()
        rospy.loginfo("Stop")
        rospy.sleep(1)

if __name__ == '__main__':

    rospy.init_node('nav_goto', anonymous=False)
    navigator = GoToPose()
    
    while(True):
        
        position = {'x': 0.0, 'y' : 0.0}
        quaternion = {'r1' : 0.000, 'r2' : 0.000, 'r3' : 0.000, 'r4' : 1.000}
        
        ox = 0
        oy = 0
        oz = 0
        ow = 1
        
        print "---Give the location of the goal---"
        x = input("x : ")
        y = input("y : ")
        print "---Would you like to give the quaternion?---"
        answer = raw_input("yes/no : ")
        if answer == "yes":
            print "---Give the quaternion of the goal---"
            ox = input("ox : ")
            oy = input("oy : ")
            oz = input("oz : ")
            ow = input("ow : ")
       
        # Customize the following values so they are appropriate for your location
        
        position['x'] = x
        position['y'] = y
        quaternion['r1'] = ox
        quaternion['r2'] = oy
        quaternion['r3'] = oz
        quaternion['r4'] = ow
        
        rospy.loginfo("Go to (%s, %s) pose", position['x'], position['y'])
        success = navigator.goto(position, quaternion)

        if success:
            rospy.loginfo("Hooray, reached the desired pose")
        else:
            rospy.loginfo("The base failed to reach the desired pose")

        # Sleep to give the last log messages time to be sent
        rospy.sleep(1)
        
        print "Do you want to give another goal?"
        answer = raw_input("yes/no : ")
        if answer == "no":
            print "au revoir..."
            break
        
    #end while

