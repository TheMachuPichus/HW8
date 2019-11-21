import os
import sys
import time

xname=sys.argv[1]
i = 0

while i < int(xname):
  os.system("./build.out")  
  i += 1
  time.sleep(1)

