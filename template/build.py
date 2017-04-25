#!/usr/bin/env python3


import subprocess

args = [
    "sudo", "-g", "docker",
    "docker",
    "build",
    "-t", "<INSERT NAME>",
    "."
]


subprocess.call(args)
