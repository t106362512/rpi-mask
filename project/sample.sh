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
      --device rpizw --model ntut-8c905-rpizero --nickname rpizw

# 他預設會在 ~/.config/googlesamples-assistant/device_config.json 建立裝置設定
googlesamples-assistant-pushtotalk --project-id ntut-8c905 --device-model-id ntut-8c905-rpizero