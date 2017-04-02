#!/usr/bin/env python3

import subprocess
import os

x11addargs = [
    "sudo", "xhost", "+local:root" 
]   # Adding permissions for everything to use XHost.  This is a dodgy and insecure way to do. Check with Lystena about a more secure way of doing it


x11removeargs = [
     "sudo", "xhost", "-local:root" 
] # Remove permissions


dockerargs = [
    "sudo", "-g", "docker",
    "docker",
    "run",
    "-it",
    "-v", "/etc/localtime:/etc/localtime:ro",
    "-v", "/tmp/.X11-unix/:/tmp/.X11-unix",
    "-e", "DISPLAY={0}".format(os.environ['DISPLAY']),
    "--device", "/dev/snd",
    "--device", "/dev/dri",
    "--device", "/dev/video0",
    "-v", "/dev/shm:/dev/shm",
    "--group-add", "audio",
    "--group-add", "video",
    "-v", "{0}/.slack:/root/.config/Slack".format(os.environ['HOME']),
    "-v", "{0}/:/root/homeDir".format(os.environ['HOME']),
    "barnie995/slack"
]


subprocess.call(x11addargs)
subprocess.call(dockerargs)
subprocess.call(x11removeargs)

