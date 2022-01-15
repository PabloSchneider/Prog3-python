#!/usr/bin/env python3

import glob
import os.path

print([[x,int(os.path.getsize(x))] for x in glob.glob("/etc/*conf") if os.path.getsize(x) in sorted([os.path.getsize(x) for x in glob.glob("/etc/*conf")])[-4:-1]])
