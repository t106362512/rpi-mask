import speech_recognition as sr

r = sr.Recognizer()

# 能量閥值，來設定到一定能量的聲音才辨識，可避免偵測錯誤
r.energy_threshold = 4000

my_stt = ''
while my_stt != "離開":
    try:
        # 假設抓不到設備可以調整device_index
        with sr.Microphone(device_index=0) as source:
            print("說些話吧: ")
            audio = r.listen(source)

            # 這邊language 也可以進行調整
            my_stt = r.recognize_google(audio, language="zh-TW")
            print(my_stt)
            if my_stt == "你好":
                print("我也很好")
            elif my_stt == "你的名字是什麼":
                print("我的名字是")
            else:
                print("i dont know")
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("No response from Google Speech Recognition service")
