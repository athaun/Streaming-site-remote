from flask import Flask, render_template, request
from flask import jsonify
import pyautogui
import time
import webbrowser

    
app = Flask(__name__)
# keyboard = Controller()

playingVideo = False

urls = [
    [b"netflix",    "https://netflix.com"],
    [b"hulu",       "https://hulu.com"],
    [b"amazon",     "https://www.amazon.com/Amazon-Video/b/?ie=UTF8&node=2858778011"],
    [b"youtube",    "https://youtube.com"],
    [b"hbo",        "https://hbomax.com"],
    [b"disney_plus","https://disneyplus.com"],
    [b"spotify",    "https://open.spotify.com"],
    [b"pandora",    "https://pandora.com"],
    [b"google",     "https://google.com"]
]

def checkPost (request, data):
    return request.get_data() == data

@app.route("/", methods=['POST', 'GET'])
def index():
    global playingVideo

    if request.method == 'POST':
        if checkPost(request, b'play_pause'):
            pyautogui.press(" ")
            playingVideo = (not playingVideo)
            if playingVideo:
                print("The video is now playing")
            else:
                print("The video is now paused")

        if checkPost(request, b'vol_up'):
            print("Volume up")
            pyautogui.press("volumeup")

        if checkPost(request, b'vol_dn'):
            print("Volume down")
            pyautogui.press("volumedown")

        if checkPost(request, b'left_arrow'):
            print("Left Arrow")
            pyautogui.press("left")

        if checkPost(request, b'right_arrow'):
            print("Right Arrow")
            pyautogui.press("right")
    
        for i in urls:
            if checkPost(request, i[0]):
                webbrowser.open(i[1], new=2)


    return render_template("index.html", css="static/css/index.css", favicon="static/images/favicon.png")

@app.route('/_pause', methods=['GET'])
def stuff():
    return jsonify(playingVideo=playingVideo)  

if __name__ == '__main__':
    app.run(host="192.168.1.10", port=7070, debug=True)

