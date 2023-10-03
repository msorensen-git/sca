import time
# import picamera

def capture_image():
    # with picamera.PiCamera() as camera:
        # camera.resolution = (1920, 1080)  # Set the resolution as needed
        timestamp = time.strftime("%Y%m%d%H%M%S")
        image_name = f"image_{timestamp}.jpg"
        # camera.capture(image_name)
        print(f"Image captured: {image_name}")

if __name__ == "__main__":
    while True:
        capture_image()
        time.sleep(100)  # Capture an image every hour (3600 seconds)