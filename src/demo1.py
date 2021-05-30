import os
import time
import shutil
import tempfile
import speech_recognition as sr
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
# from GoogleAssistant.pushtotalk import main as google_assistant
# from googlesamples.assistant.grpc import audio_helpers
# from google.cloud import texttospeech


# def gtts(text, file_path: os.PathLike=tempfile.NamedTemporaryFile(mode='w', suffix='.mp3').name, *args, **kwargs):
#     client = texttospeech.TextToSpeechClient()
#     input_text = texttospeech.SynthesisInput(text=text)
#     # Note: the voice can also be specified by name.
#     # Names of voices can be retrieved with client.list_voices().
#     voice = texttospeech.VoiceSelectionParams(
#         language_code="zh-tw",
#         name="zh-tw-Standard-A",
#         ssml_gender=texttospeech.SsmlVoiceGender.FEMALE,
#     )

#     audio_config = texttospeech.AudioConfig(
#         audio_encoding=texttospeech.AudioEncoding.MP3
#     )

#     response = client.synthesize_speech(
#         request={"input": input_text, "voice": voice, "audio_config": audio_config}
#     )

#     # The response's audio_content is binary.
#     with open(file_path, "wb") as out:
#         out.write(response.audio_content)
#         print(f'Audio content written to file {file_path}')


def tts(audioString: str, file_path: os.PathLike=tempfile.NamedTemporaryFile(mode='w', suffix='.mp3').name):
    tts = gTTS(text=audioString, lang='zh-tw', slow=False)
    tts.save(file_path)
    # gtts(audioString, file_path)
    # audio_source = audio_helpers.WaveSource(
    #         open(file_path, 'rb'),
    #         sample_rate=audio_helpers.DEFAULT_AUDIO_SAMPLE_RATE,
    #         sample_width=audio_helpers.DEFAULT_AUDIO_SAMPLE_WIDTH
    # )
    # audio_sink = audio_helpers.SoundDeviceStream(
    #     sample_rate=audio_helpers.DEFAULT_AUDIO_SAMPLE_RATE,
    #     sample_width=audio_helpers.DEFAULT_AUDIO_SAMPLE_WIDTH,
    #     block_size=audio_helpers.DEFAULT_AUDIO_DEVICE_BLOCK_SIZE,
    #     flush_size=audio_helpers.DEFAULT_AUDIO_DEVICE_FLUSH_SIZE
    # )
    # conversation_stream = audio_helpers.ConversationStream(
    #     source=audio_source,
    #     sink=audio_sink,
    #     iter_size=audio_helpers.DEFAULT_AUDIO_ITER_SIZE,
    #     sample_width=audio_helpers.DEFAULT_AUDIO_SAMPLE_WIDTH,
    # )
    # conversation_stream.start_playback()
    sound = AudioSegment.from_file(file_path, format='mp3')
    play(sound)

def read_dict(d: dict, file_path: os.PathLike=tempfile.NamedTemporaryFile(mode='w', suffix='.mp3').name):

    result_list = [ f"{k}目前是{v}" for (k, v) in d.items()]
    read_str = ';'.join(str(e) for e in result_list)
    tts(read_str, file_path)

def main(r: sr.Recognizer=sr.Recognizer()):
    my_stt = ''
    tmp_fp = tempfile.NamedTemporaryFile(mode='w', suffix='.mp3', delete=False)

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
                    print("谷歌沒來喔")
                    # try:
                    #     x = google_assistant()
                    #     print(x)
                    # except SystemExit:
                    #     pass
                elif my_stt == "告訴我訊息":
                    print("收到")
                    # tts("你的訊息", tmp_fp.name)
                    d = {
                        # CCS811
                        "CO2": 1111,
                        "TVOC": 2222,
                        # bme280
                        "Temperature": 333,
                        "RelativeHumidity": 444,
                        "Pressure": 55.7,
                        "Altitude": 77.9,
                        # hdc1080
                        "Temperature_HDC1080": 0.11,
                        "Humidity_HDC1080": 999
                    }
                    read_dict(d, tmp_fp.name)
                else:
                    print("i dont know")
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError:
            print("No response from Google Speech Recognition service")
        finally:
            shutil.rmtree(tmp_fp.name, ignore_errors=True)

if __name__ == '__main__':

    r = sr.Recognizer()
    r.energy_threshold = 4000

    main(r)
