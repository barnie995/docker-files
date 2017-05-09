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
    "-p", "228.5.6.7:8888:6789",
    "barnie995/java"  
]



subprocess.call(dockerargs)

