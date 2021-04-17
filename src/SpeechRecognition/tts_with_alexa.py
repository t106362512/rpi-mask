from gtts import gTTS
import speech_recognition as sr
import boto3

def speak(audioString):
    polly_client = boto3.Session(
        aws_access_key_id='這邊輸入你的key_id',
        aws_secret_access_key='這邊輸入你的access_key',
        region_name='us-east-1').client('polly')
    response = polly_client.synthesize_speech(VoiceId='Zhiyu',OutputFormat='mp3', Text = audioString)

    with open('speech.mp3', 'wb') as f:
        f.write(response['AudioStream'].read())
        f.close()
    os.system("speech.mp3")

def main(my_stt):
    while my_stt != "離開":
        try:
            speak("你好")
            with sr.Microphone(device_index=0) as source:
                #--------------------
                audio=r.listen(source)
                my_stt=r.recognize_google(audio, language="zh-tw")
                print(my_stt)

                if my_stt == "你好":
                    #print ("我也很好")
                    speak("我也很好")
        except sr.UnknownValueError:
            #print("Google Speech Recognition could not understand audio")
            speak("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            #print("No response from Google Speech Recognition service")
            speak("No response from Google Speech Recognition service")

if __name__ == "__main__":
    r = sr.Recognizer()

    #能量閥值，來設定到一定能量的聲音才辨識
    r.energy_threshold = 4000

    my_stt = ""

    main(my_stt)
