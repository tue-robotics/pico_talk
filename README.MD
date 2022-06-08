# pico_talk

## Install dependencies

```bash
sudo apt-get install libespeak-dev python3-pip
sudo apt-get ffmpeg
pip install python-espeak
```

Make sure the python script is executable

```bash
chmod +x ./path/to/file/speech_server.py
```

Run the file

```bash
rosrun pico_talk speech_server.py
```

or

```bash
rosrun pico_talk speech_server.py /speech/topic/here
```
