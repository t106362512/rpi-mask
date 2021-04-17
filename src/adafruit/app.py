# Import standard python modules.
import sys
import os

# Import blinka python modules.
# import board
# import digitalio

# This example uses the MQTTClient instead of the REST client
from Adafruit_IO import MQTTClient

# Set to your Adafruit IO key.
# Remember, your key is a secret,
# so make sure not to publish it when you publish this code!
ADAFRUIT_IO_KEY = os.getenv('ADAFRUIT_IO_KEY')

# Set to your Adafruit IO username.
# (go to https://accounts.adafruit.com to find your username)
ADAFRUIT_IO_USERNAME = os.getenv('ADAFRUIT_IO_USERNAME')

# Set to the ID of the feed to subscribe to for updates.
FEED_ID = os.getenv('FEED_ID')

# relay = digitalio.DigitalInOut(board.D5)
# relay.direction = digitalio.Direction.OUTPUT

# Define callback functions which will be called when certain events happen.


def connected(client):
    """Connected function will be called when the client is connected to
    Adafruit IO.This is a good place to subscribe to feed changes. The client
    parameter passed to this function is the Adafruit IO MQTT client so you
    can make calls against it easily.
    """
    # Subscribe to changes on a feed named Counter.
    print('Subscribing to Feed {0}'.format(FEED_ID))
    client.subscribe(FEED_ID)
    print('Waiting for feed data…')


def disconnected(client):
    """Disconnected function will be called when the client disconnects."""
    sys.exit(1)


def message(client, feed_id, payload):
    """Message function will be called when a subscribed feed has a new value.
    The feed_id parameter identifies the feed, and the payload parameter has
    the new value.
    """
    print('Feed {0} received new value: {1}'.format(feed_id, payload))

    if payload == "0":
        print("Turn off relay!")
        # relay.value = False
    elif payload == "1":
        print("Turn on relay!")
        # relay.value = True

if __name__ == '__main__':

    # Create an MQTT client instance.
    client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

    # Setup the callback functions defined above.
    client.on_connect = connected
    client.on_disconnect = disconnected
    client.on_message = message

    # Connect to the Adafruit IO server.
    client.connect()

    # The first option is to run a thread in the background so you can continue
    # doing things in your program.
    client.loop_blocking()
