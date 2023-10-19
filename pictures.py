from picamera2 import Picamera2, Preview
from picamera2 import Picamera2, Preview
from datetime import datetime

import time
picam2 = Picamera2()
camera_config = picam2.create_still_configuration(main={"size": (1920, 1080)}, lores={"size": (640, 480)}, display="lores")
picam2.configure(camera_config)
picam2.start_preview(Preview.QTGL)
timestamp = datetime.now().isoformat()

picam2.start()
picam2.capture_file('/home/heckl/Pictures/%s.jpg' % timestamp)
picam2.stop_preview()

wait = input("Press any key to continue...")
picam2.start_preview(Preview.QTGL)
timestamp = datetime.now().isoformat()
picam2.capture_file('/home/heckl/Pictures/%s.jpg' % timestamp)

picam2.stop()