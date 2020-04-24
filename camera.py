import cv2
from threading import Thread


class Camera:
    def __init__(self):
        self.cam = None
        self.running = False

        self.__start_thread__()

    def __start_thread__(self):
        if self.cam != None:
            print("Camera is already running")
            return

        self.cam = cv2.VideoCapture(0)
        if self.cam.isOpened():
            print("Camera started successfully")
            self.running, self.frame = self.cam.read()
        else:
            self.running = False
            raise Exception("Camera failed to start")

        self.thread = Thread(target=self.camera_loop, args=())
        self.thread.daemon = True
        self.thread.start()

    def camera_loop(self):
        if not self.running:
            raise Exception("Camera is not running!")

        while self.running:
            self.running, self.frame = self.cam.read()

    def end(self):
        print("Stopping Camera")

        self.running = False

        self.cam.release()
        self.cam = None
