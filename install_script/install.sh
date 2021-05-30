SCRIPTPATH="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

echo "Copy .asoundrc to $HOME."
cp $SCRIPTPATH/../config/.asoundrc $HOME/

echo "Install apt package."
sudo apt-get update
sudo apt-get install -y python3-dev python3-venv \
    portaudio19-dev libffi-dev libssl-dev \
    ffmpeg libavcodec-extra

echo "Copy pip.conf to /etc."
sudo cp $SCRIPTPATH/../config/pip.conf /etc/pip.conf

echo "Create venv to project root dir."
python3 -m venv $SCRIPTPATH/../env

echo "Activate the venv."
. $SCRIPTPATH/../env/bin/activate

echo "Install package from requirements.txt."
python -m pip install -r $SCRIPTPATH/../requirements.txt
python -m pip install -r $SCRIPTPATH/../src/rpi-sensor/requirements.txt

echo "Install google outhlib and authorize the application."
python -m pip install --upgrade google-auth-oauthlib[tool]
google-oauthlib-tool --scope https://www.googleapis.com/auth/assistant-sdk-prototype \
      --save --headless --client-secrets $SCRIPTPATH/../config/client_secret.json
