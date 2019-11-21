import os
import sys
import time

def main():
  xname=sys.argv[1]
  i = 0
  
  while i < int(xname):
    os.system("./build.out")  
    i += 1
    time.sleep(1)

if __name__=='__main__':
  main()

