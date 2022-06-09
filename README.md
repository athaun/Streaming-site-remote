# TV Remote
A python/flask web server that can perform basic functions to optimize your lazyness.
With one tap of a button, open a streaming service from your phone, control the volume, pause and play, and skip.
[Video demo on YT](https://www.youtube.com/watch?v=o4WpVH0GWw0)

![](static/images/phone.png)

## PyInstaller (to build an executable)
```
pyinstaller --noconfirm --onefile --console --add-data "/Users/asher/Documents/code/Streaming-site-remote/static:static/" --add-data "/Users/asher/Documents/code/Streaming-site-remote/templates:templates/"  "/Users/asher/Documents/code/Streaming-site-remote/main.py"
```

## Running for yourself

Install the dependancies:
```
pip install -r requirements.txt
```
Run:
```
python main.py
```
or double click `runServer.bat`

connect the the ip address of the computer running the server from your phone
For example, `http://192.168.1.10`

<br>
Tested on

* YouTube
* Amazon Prime Video
* Disney+
