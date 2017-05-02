#!/usr/bin/env python3

import subprocess
import os

dockerargs = [
    "sudo", "-g", "docker",
    "docker",
    "run",
    "-ti",
    "-v", "/etc/localtime:/etc/localtime:ro",
    "-v", "{0}/:/root/hostFiles/".format(os.environ['HOME']),
    "barnie995/hashid"  
]


subprocess.call(dockerargs)

