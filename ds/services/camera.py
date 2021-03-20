import cv2
from . import base


class Camera(base.Service):

    def __init__(self):
        self.state = False
        self.video_capture: cv2.VideoCapture = None

    def start(self):
        if not self.state:
            self.video_capture = cv2.VideoCapture(0)
            self._reverse_state()

    def stop(self):
        if self.state:
            self.video_capture.release()
            self._reverse_state()

    def _reverse_state(self):
        self.state = not self.state

    def read_frame(self):
        if not self.state:
            return
        _, frame = self.video_capture.read()
        return frame

    def read_frames(self, no_limit=False, limit=1):
        """
            :param no_limit, if True infinite send of frames until Q button is tapped
            :param limit, if no_limit is False, points to the number of frames
        """
        if not self.state:
            return
        if no_limit:
            while not cv2.waitKey(1) & 0xFF == ord('q'):
                yield self.read_frame()
        else:
            for _ in range(limit):
                yield self.read_frame()
