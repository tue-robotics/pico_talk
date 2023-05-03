#!/usr/bin/env python

import rospy
import espeak
from std_msgs.msg import String
import subprocess
import sys

def talkcallback(data,args):
	rospy.loginfo("SpeechServer received speaking command")
	rospy.loginfo("Pyro says: " + data.data)
	args.say(data.data)
	
def filecallback(data):
	rospy.loginfo("SpeechServer received play command")
	rospy.loginfo("Pyro plays: " + data.data)
	path = ("~/MRC_audio/" + data.data)
	subprocess.run(("ffplay -i " + path + " -loglevel error -nodisp -autoexit"), shell=True) 


def main(topic = "/pyro/text_to_speech/input"):
	# init espeak 
	espeak.init();
	speaker = espeak.Espeak()
	# init ros node
	rospy.init_node('speech_server',anonymous=True)
	rospy.Subscriber(topic, String, talkcallback, speaker)
	rospy.Subscriber("/pyro/text_to_speech/file", String, filecallback)
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

