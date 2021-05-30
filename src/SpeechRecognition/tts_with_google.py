import os
import tempfile
import subprocess
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play


def tts(audioString: str, file_path: os.PathLike=tempfile.NamedTemporaryFile(mode='w', suffix='.mp3').name):
    tts = gTTS(text=audioString, lang='zh-tw')
    tts.save(file_path)
    # subprocess.check_output(file_path)
    sound = AudioSegment.from_file(file_path, format='mp3')
    play(sound)

def speak(audioString):
    # 利用gTTS將文字轉成聲音
    tts = gTTS(text=audioString, lang='zh-tw')
    # 將其存成mp3檔
    tts.save("audio.mp3")
    # 播放mp3有各種方法，以下提供其中一種方法:
    # 在embedded linux的環境下播放wav檔比較簡單
    # 所以這邊使用pydub將 mp3 轉成 wav 後再進行播放
    sound = AudioSegment.from_mp3("audio.mp3")
    sound.export("myfile.wav",format="wav")
    play('myfile.wav')

if __name__ == '__main__':
    tts('測試喔')
