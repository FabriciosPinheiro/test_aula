import rospy
from std_msgs.msg import String

rospy.init_node('teste1')

def timerCallBack(event):
    msg = String()
    msg.data = 'test3'
    pub.publish(msg)
    
    
    
pub = rospy.Publisher('/topic1', String, queue_size = 1)
timer = rospy.Timer(rospy.Duration(0.1), timerCallBack)

rospy.spin()
