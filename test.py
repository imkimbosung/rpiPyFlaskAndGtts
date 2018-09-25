# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding(‘utf-8’)
from gtts import gTTS
from pygame import mixer
from tempfile import TemporaryFile
from io import BytesIO

text =“안녕하세요,여러분. 파이썬으로 노는 것은 재미있습니다”
tts = gTTS(text=text, lang=‘ko’)
mixer.init()

print(mp3_fp)
sf = TemporaryFile()
tts.write_to_fp(sf)
sf.seek(0)
mixer.music.load(sf)
mixer.music.play()

from time import sleep
sleep(5)
