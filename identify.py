#!/usr/bin/env python
"""
Usage: python identify.py

Finds all APT controllers and flashes their activity lights
"""
import time
import pylibftdi
import pyAPT

def main(args):
  print 'Looking for APT controllers'
  drv = pylibftdi.Driver()
  controllers = drv.list_devices()

  if controllers:
    for con in controllers:
      print 'Found %s %s S/N: %s'%con
      with pyAPT.Controller(serial_number=con[2]) as con:
        print '\tIdentifying controller'
        con.identify()

      return 0
  else:
    print '\tNo APT controllers found. Maybe you need to specify a PID'
    return 1

if __name__ == '__main__':
  import sys
  sys.exit(main(sys.argv))

