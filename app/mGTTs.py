# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from gtts import gTTS
from pygame import mixer
from pygame import time
from tempfile import TemporaryFile


class mGTTs:
    def __init__(self):
        pass

    def run(self, text):
        # pygame.init()
        mixer.init()
        sf = TemporaryFile()
        
        tts = gTTS(text=text, lang='ko')
        
        clock = time.Clock()
        tts.write_to_fp(sf)
        sf.seek(0)
        mixer.music.load(sf)
        mixer.music.play()

        while mixer.music.get_busy()==True:
            clock.tick(1000)
            print( mixer.music.get_busy())
    
    def stop(self):
        mixer.music.stop()
       

    
    

