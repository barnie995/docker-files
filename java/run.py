#!/usr/bin/env python3

import subprocess
import os



dockerargs = [
    "sudo", "-g", "docker",
    "docker",
    "run",
    "-ti",
    "-v", "/etc/localtime:/etc/localtime:ro",
    "-v", "{0}/:/root/".format(os.environ['HOME']),
    "barnie995/java"  
]



subprocess.call(dockerargs)

