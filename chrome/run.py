#!/usr/bin/env python3

import subprocess
import os
import argparse

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
    "-e", "DISPLAY={0}".format(os.environ['DISPLAY']),
    "--network=burp",
    "--memory", "512mb",
    "--cpuset-cpus", "0",
    "-v", "{0}/Downloads:/home/chrome/Downloads".format(os.environ['HOME']),
    "--security-opt", "seccomp={0}/chrome.json".format(os.getcwd()),
    "--device", "/dev/snd",
    "--device", "/dev/dri",
    "barnie995/chrome", "--no-sandbox"  
]

#Arg Parsing Stuff

parser = argparse.ArgumentParser()

parser.add_argument('-P', '--proxy')
args = parser.parse_args()

subprocess.call(x11addargs)

if args.proxy is not None:
    dockerargs.append("--proxy-server={0}".format(args.proxy))
    subprocess.call(dockerargs) 
else:
    subprocess.call(dockerargs)

subprocess.call(x11removeargs)

