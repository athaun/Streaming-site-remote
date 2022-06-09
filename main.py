from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit  
from engineio.async_drivers import gevent
from flask import jsonify
import pyautogui
import webbrowser
import socket
import json
import platform
import osascript


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'                                            
socketio = SocketIO(app) 

playingVideo = False

urls = [
    ["netflix",    "https://netflix.com"],
    ["hulu",       "https://hulu.com"],
    ["amazon",     "https://www.amazon.com/Amazon-Video/b/?ie=UTF8&node=2858778011"],
    ["youtube",    "https://youtube.com"],
    ["hbo",        "https://hbomax.com"],
    ["disney_plus","https://disneyplus.com"],
    ["spotify",    "https://open.spotify.com"],
    ["pandora",    "https://pandora.com"],
    ["google",     "https://google.com"]
]

def darwinVolume (direction):
    result = osascript.osascript('get volume settings')
    info = result[1].split(',')
    currentVolume = int(info[0].replace('output volume:', ''))

    if direction == "up":
       currentVolume += 5
    elif direction == "down":
        currentVolume -= 5

    osascript.osascript("set volume output volume " + str(currentVolume))
    

def getip ():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def checkPost (request, data):
    return request == data

@socketio.on('connect')                                                         
def connect():               
    print("Socket connected")   

@socketio.on('message')
def handleMessage (data):
    message = data["data"]
  

    global playingVideo

    if checkPost(message, 'play_pause'):
        pyautogui.press(" ")
        playingVideo = (not playingVideo)
        if playingVideo:
            print("The video is now playing")
        else:
            print("The video is now paused")
        emit('message', "DUMMY", broadcast=True)


    if checkPost(message, 'vol_up'):
        print("Volume up")
        if platform.system() == "Darwin":
            darwinVolume("up")
        else:
            pyautogui.press("volumeup")

    if checkPost(message, 'vol_dn'):
        print("Volume down")
        if platform.system() == "Darwin":
            darwinVolume("down")
        else:
            pyautogui.press("volumedown")

    if checkPost(message, 'left_arrow'):
        print("Left Arrow")
        pyautogui.press("left")

    if checkPost(message, 'right_arrow'):
        print("Right Arrow")
        pyautogui.press("right")

    for i in urls:
        if checkPost(message, i[0]):
            webbrowser.open(i[1], new=2)

@app.route("/", methods = ['POST', 'GET'])
def index ():
    return render_template("index.html", css="static/css/index.css")

@app.route('/_pause', methods=['GET'])
def stuff ():
    return jsonify(playingVideo=playingVideo)  

if __name__ == '__main__':
    print(f"\nOn your phone go to http://{getip()}:8080\n")
    socketio.run(app, host = "0.0.0.0", port = 8080) # , debug = True

