""" some test cases for the mqtt hook
"""
import os
import subprocess
import time
import json
import paho.mqtt.client as mqtt
from mopidy.__main__ import main

def test_mopidy():
    main()


if __name__ == "__main__":
    test_mopidy()