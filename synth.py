from mitmproxy import ctx
import re
from pygame import mixer
import _thread

class Synth:
    def __init__(self):
        mixer.init()
        self.chips_sfx=mixer.Sound("sfx/chips.wav")
        self.laser_sfx=mixer.Sound("sfx/laser.wav")
        self.hoop_sfx=mixer.Sound("sfx/hoop.wav")
        self.stick_sfx=mixer.Sound("sfx/stick.wav")

        self.chips_sfx.set_volume(0.3)
        self.laser_sfx.set_volume(0.3)
        self.hoop_sfx.set_volume(0.2)
        self.stick_sfx.set_volume(0.2)

    def request(self, flow):
        if flow.request.method == "GET":
            self.chips_sfx.play()
        else:
            self.laser_sfx.play()

    def response(self,flow):
        if(re.search("javascript",str(flow.response.headers.get("content-type")))):
            self.stick_sfx.play()
        if(re.search("json",str(flow.response.headers.get("content-type")))):
            self.hoop_sfx.play()

addons = [
    Synth()
]

