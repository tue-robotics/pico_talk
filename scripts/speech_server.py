#!/usr/bin/env python

import rospy
import espeak
from std_msgs.msg import String
import os
import sys

def callback(data,args):
	rospy.loginfo("SpeechServer received speaking command")
	rospy.loginfo("Pyro says: " + data.data)
	args.say(data.data)


def main(topic = "/pyro/text_to_speech/input"):
	# init espeak 
	espeak.init();
	speaker = espeak.Espeak()
	# init ros node
	rospy.init_node('speech_server',anonymous=True)
	rospy.Subscriber(topic, String, callback, speaker)
	speaker.say("One two, One two, Beep Boop")
	rospy.spin()

if __name__ == '__main__':
	try:
		if len(sys.argv) < 2:
			main()
		else:
			main(sys.argv[1])	
			
	except rospy.ROSInterruptException:
		pass

