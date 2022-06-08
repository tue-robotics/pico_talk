Install Dependencies
```
sudo apt-get install libespeak-dev python3-pip
sudo apt-get ffmpeg
pip install python-espeak
```

Make sure the python script is executable
```
chmod +x ./path/to/file/speech_server.py
```

Run the file
```
rosrun pico_talk speech_server.py
```
or
```
rosrun pico_talk speech_server.py /speech/topic/here
``'
