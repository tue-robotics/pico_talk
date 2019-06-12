#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import os

def callback(data):
	rospy.loginfo("SpeechServer received speaking command")
	os.system('espeak "' + data.data + '" --stdout | aplay --device "default" &')


def main():
	rospy.init_node('speech_server',anonymous=True)
	rospy.Subscriber("/pico/speak",String, callback)
	rospy.spin()

if __name__ == '__main__':
	try:
		main()
	except rospy.ROSInterruptException:
		pass

