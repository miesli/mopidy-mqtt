""" some test cases for the mqtt hook
"""
import os
import subprocess
import time
import json
import paho.mqtt.client as mqtt
from mopidy.__main__ import main

def test_example_mp3():
    client = mqtt.Client("mopidy_test_publisher")
    client.username_pw_set('mqtt_rhasspy', password="12345")
    client.connect("localhost", port=1883)

    # client.publish("home/livingroom/music/control", "stop")
    path_example_mp3 = "file://" + os.path.expanduser(os.path.join('~', 'Music', 'file_example_MP3_700KB.mp3'))
    client.publish("home/livingroom/music/play", path_example_mp3)
    # print("Published {:s} to the topic {:s}".format(path_example_mp3, topic) )
    # client.publish("home/livingroom/music/control", "play")

    # client.publish(topic, 'play')

    client.disconnect()

def test_radionet_link():

    client = mqtt.Client("mopidy_test_publisher")
    client.username_pw_set('mqtt_rhasspy', password="12345")
    client.connect("localhost", port=1883)

    url = "https://stream.rockantenne.hamburg/rockantenne-hamburg/stream/mp3?aw_0_1st.playerid=radio.de"

    client.publish("home/kitchen/music/play", url)
    client.disconnect()

def test_radionet_favorite():

    client = mqtt.Client("mopidy_test_publisher")
    client.username_pw_set('mqtt_rhasspy', password="12345")
    client.connect("localhost", port=1883)

    station = "Rock Antenne"

    client.publish("home/kitchen/music/play_radio", station)
    client.disconnect()

if __name__ == "__main__":
    # test_example_mp3()
    test_radionet_favorite()