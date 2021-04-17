# 使用 RPI Zero W 串接語音助理

## 折騰點

- 乾，音效卡好雷喔，換第三片找到能用的。
- 音效卡的部分沒有這麼好搞，這問題會因為系統版本的不同而有不同的設定要做。
- 這篇文章是使用 rpi zero w 且系統為 Raspbian GNU/Linux 10 (buster) 上弄出來的。
- google 文件只能當參考，要雷過才知道(他後面有更新了grpc的問題了)。

## Fix SoundCard

1. 使用 `aplay -l` 與 `arecord -l` 取得聲卡位置

    ```bash
    pi@raspberrypi:~ $ aplay -l
    **** List of PLAYBACK Hardware Devices ****
    card 0: b1 [bcm2835 HDMI 1], device 0: bcm2835 HDMI 1 [bcm2835 HDMI 1]
      Subdevices: 8/8
      Subdevice #0: subdevice #0
      Subdevice #1: subdevice #1
      Subdevice #2: subdevice #2
      Subdevice #3: subdevice #3
      Subdevice #4: subdevice #4
      Subdevice #5: subdevice #5
      Subdevice #6: subdevice #6
      Subdevice #7: subdevice #7
    card 1: Device [USB Audio Device], device 0: USB Audio [USB Audio]
      Subdevices: 1/1
      Subdevice #0: subdevice #0

    pi@raspberrypi:~ $ arecord -l
    **** List of CAPTURE Hardware Devices ****
    card 1: Device [USB Audio Device], device 0: USB Audio [USB Audio]
      Subdevices: 1/1
      Subdevice #0: subdevice #0
    ```

2. `vim /home/pi/.asoundrc`  

    ```conf
    pcm.!default {
      type asym
      capture.pcm "mic"
      playback.pcm "speaker"
    }
    pcm.mic {
      type plug
      slave {
        pcm "hw:<card number>,<device number>"
      }
    }
    pcm.speaker {
      type plug
      slave {
        pcm "hw:<card number>,<device number>"
      }
    }
    ```

3. check audio card  

    ```bash
    pi@raspberrypi:~ $ amixer scontrols
    Simple mixer control 'PCM',0
    Simple mixer control 'Mic',0

    pi@raspberrypi:~ $ amixer -c 1
    Simple mixer control 'PCM',0
      Capabilities: pvolume pswitch pswitch-joined
      Playback channels: Front Left - Front Right
      Limits: Playback 0 - 999
      Mono:
      Front Left: Playback 999 [100%] [3.90dB] [on]
      Front Right: Playback 999 [100%] [3.90dB] [on]
    Simple mixer control 'Mic',0
      Capabilities: cvolume cswitch cswitch-joined
      Capture channels: Front Left - Front Right
      Limits: Capture 0 - 3996
      Front Left: Capture 3932 [98%] [15.35dB] [on]
      Front Right: Capture 3780 [95%] [14.75dB] [on]
    ```

4. vim /usr/share/alsa/alsa.conf

    ```conf
    # search and repleac this
    defaults.ctl.card 1 # change 0 to 1
    defaults.pcm.card 1
    ```

5. 使用以下指令將mic與speack提高

    ```bash
    alsamixer -c1
    ```

6. 使用以下指令測試

    ```bash
    # 測試喇叭是否正常
    pi@raspberrypi:~ $ speaker-test -t wav

    # 測試錄音
    pi@raspberrypi:~ $ arecord --format=S16_LE --duration=5 --rate=16000 --file-type=raw out.raw
    Recording raw data 'out.raw' : Signed 16 bit Little Endian, Rate 16000 Hz, Mono

    # 測試回放錄音
    pi@raspberrypi:~ $ aplay --format=S16_LE --rate=16000 ./out.raw
    Playing raw data './out.raw' : Signed 16 bit Little Endian, Rate 16000 Hz, Mono
    ```

## 串接 google assistant 服務

參考資料

- [Introduction to the Google Assistant Service](https://developers.google.com/assistant/sdk/guides/service/python)

1. 先參考 [Embed the Google Assistant](https://developers.google.com/assistant/sdk/guides/service/python#embed) ，並建立基本的 google assistan 在 rpi zero w 上，以成功連接基本之服務。
2. 上一步服務建立完後，在參考 [Extend the Google Assistant](https://developers.google.com/assistant/sdk/guides/service/python#extend) ，並擴充基本的服務。
3. https://console.actions.google.com/u/4/project/ntut-8c905/deviceregistration/
4. 目前能使用 turn down(小聲點)作為觸發，請參考[網址](https://developers.google.com/assistant/smarthome/traits/volume)設定參數。
