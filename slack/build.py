#!/usr/bin/env python3


import subprocess

args = [
    "sudo", "-g", "docker",
    "docker",
    "build",
    "-t", "barnie995/slack",
    "."
]


subprocess.call(args)
