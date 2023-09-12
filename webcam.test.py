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

import cv2
import platform

src = 0

if platform.system() == 'Windows':
    capture = cv2.VideoCapture(src, cv2.CAP_DSHOW)
    print(capture.isOpened())

else:
    capture = cv2.VideoCapture(src)

capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)

while capture.isOpened():

    (grabbed, frame) = capture.read()

    if grabbed:
        cv2.imshow('Wand lab Camera Window', frame)

        key = cv2.waitKey(1) & 0xFF
        if key == 27:
            break

capture.release()
cv2.destroyAllWindows()
