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
    "-ti",
    "-v", "/etc/localtime:/etc/localtime:ro",
    "-v", "/tmp/.X11-unix/:/tmp/.X11-unix:ro",
    "-v", "{0}/:/root/hhomeDir/".format(os.environ['HOME']),
    "-e", "DISPLAY={0}".format(os.environ['DISPLAY']),
    "barnie995/gimp"  
]


subprocess.call(x11addargs)
subprocess.call(dockerargs)
subprocess.call(x11removeargs)

