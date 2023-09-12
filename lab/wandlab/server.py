# -*- encoding: utf-8 -*-
# -------------------------------------------------#
# Date created          : 2020. 8. 18.
# Date last modified    : 2020. 8. 19.
# Author                : chamadams@gmail.com
# Site                  : http://wandlab.com
# License               : GNU General Public License(GPL) 2.0
# Version               : 0.1.0
# Python Version        : 3.6+
# -------------------------------------------------#

from flask import Flask
from flask import request
from flask import Response
from flask import stream_with_context

from lab.wandlab.streamer import Streamer

app = Flask(__name__)
streamer = Streamer()


@app.route('/stream')
def stream():
    src = request.args.get('src', default=0, type=int)
    # ip cam 주소
    src = "rtsp://172.30.1.12:8080/h264.sdp"
    try:

        return Response(
            stream_with_context(stream_gen(src)),
            mimetype='multipart/x-mixed-replace; boundary=frame')

    except Exception as e:

        print('[wand lab] ', 'stream error : ', str(e))


def stream_gen(src):
    try:

        streamer.run(src)

        while True:
            frame = streamer.bytecode()
            print("frame: ", frame)
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    except GeneratorExit:
        print('[wand lab]', 'disconnected stream')
        streamer.stop()
