#!/usr/bin/env python

import rospy
import espeak
from std_msgs.msg import String
import os

def callback(data,args):
	rospy.loginfo("SpeechServer received speaking command")
	rospy.loginfo("Pyro says: " + data.data)
	args.say(data.data)


def main():
	# init espeak 
	espeak.init();
	speaker = espeak.Espeak()
	# init ros node
	rospy.init_node('speech_server',anonymous=True)
	rospy.Subscriber("/pico/speak",String, callback, speaker)
	speaker.say("One two, One two, Beep Boop")
	rospy.spin()

if __name__ == '__main__':
	try:
		main()
	except rospy.ROSInterruptException:
		pass

