from mitmproxy import ctx
from pygame import mixer
import _thread

class Synth:
    def __init__(self):
        mixer.init()
        self.chips_sfx=mixer.Sound("chips.wav")
        self.laser_sfx=mixer.Sound("portal.wav")
        self.chips_sfx.set_volume(0.5)
        self.laser_sfx.set_volume(0.5)

    def request(self, flow):
        if flow.request.method != "GET":
            self.laser_sfx.play()
        else:
            self.chips_sfx.play()

#    def response(self, flow):
#        self.chips_sfx.play()


addons = [
    Synth()
]

