sudo apt-get update
sudo apt-get install portaudio19-dev libffi-dev libssl-dev
sudo apt-get install python3-dev python3-venv

# IN VENV
python3 -m venv env
source env/bin/activate
# python -m pip install --upgrade google-auth-oauthlib[tool]
python -m pip install --upgrade google-assistant-sdk[samples]
google-oauthlib-tool --scope https://www.googleapis.com/auth/assistant-sdk-prototype \
      --scope https://www.googleapis.com/auth/gcm \
      --save --headless --client-secrets /path/to/client_secret_client-id.json

googlesamples-assistant-devicetool --project-id ntut-8c905 register-model \
      --model "ntut-8c905-rpizero" \
      --type "LIGHT" \
      --trait "action.devices.traits.OnOff" \
      --manufacturer "Assistant SDK developer" \
      --product-name "rpizero" \
      --description "Assistant SDK rpi zero device"

googlesamples-assistant-devicetool --project-id ntut-8c905 register-device \
      --client-type SERVICE \
      --device "raspberrypi" --model ntut-8c905-rpizero 
      # --nickname rpizw

# 取得 device model id ntut-8c905-rpizero
googlesamples-assistant-devicetool --project-id ntut-8c905 list --model

googlesamples-assistant-devicetool --project-id ntut-8c905 list --device

# 他預設會在 ~/.config/googlesamples-assistant/device_config.json 建立裝置設定
# 如果在 googlesamples-assistant-devicetool --project-id ntut-8c905 register-device 使用 nickname 時，則要說 turn on the $NICKNAME.
# googlesamples-assistant-pushtotalk --project-id ntut-8c905 --device-model-id ntut-8c905-rpizero
googlesamples-assistant-pushtotalk --project-id ntut-8c905 --device-id raspberrypi

# For Linux arm
curl -O https://dl.google.com/gactions/updates/bin/linux/arm/gactions

# For Linux x86_64
curl -O https://dl.google.com/gactions/updates/bin/linux/amd64/gactions/gactions

# For Windows x86_64
curl -O https://dl.google.com/gactions/updates/bin/windows/amd64/gactions.exe/gactions.exe

# For Mac x86_64
curl -O https://dl.google.com/gactions/updates/bin/darwin/amd64/gactions/gactions

# chmod
chmod +x gactions 

./gactions update --action_package actions.json --project ntut-8c905