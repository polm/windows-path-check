import os
import subprocess
import sys

cmd = "python inner.py"
if os.name != "nt":
    cmd = cmd.split()

print("outer executable:", sys.executable)
subprocess.run(cmd)
