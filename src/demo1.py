import os
import time
import shutil
import tempfile
import speech_recognition as sr
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
from GoogleAssistant.pushtotalk import main as google_assistant


def tts(audioString: str, file_path: os.PathLike=tempfile.NamedTemporaryFile(mode='w').name):
    tts = gTTS(text=audioString, lang='zh-tw')
    tts.save(file_path)
    sound = AudioSegment.from_file(file_path, format='mp3')
    play(sound)

def main(r: sr.Recognizer=sr.Recognizer()):
    my_stt = ''
    tmp_fp = tempfile.NamedTemporaryFile(mode='w', delete=False)

    while my_stt != "離開":
        # time.sleep(0.1)
        try:
            with sr.Microphone() as source:
                time.sleep(0.5)
                print("說些話吧: ")
                audio = r.listen(source)
                my_stt = r.recognize_google(audio, language="zh-tw")
                print(f"echo: {my_stt}")
                if my_stt == "谷歌":
                    print("谷歌來喔")
                    try:
                        x = google_assistant()
                        print(x)
                    except SystemExit:
                        pass
                elif my_stt == "告訴我訊息":
                    print("收到")
                    tts("你的訊息", tmp_fp.name)
                else:
                    print("i dont know")
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("No response from Google Speech Recognition service")
        finally:
            shutil.rmtree(tmp_fp.name, ignore_errors=True)

if __name__ == '__main__':

    r = sr.Recognizer()
    r.energy_threshold = 4000
    main(r)
