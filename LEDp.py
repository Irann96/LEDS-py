#!/usr/bin/python

import sys
LED3_PATH = "/sys/class/leds/beaglebone:green:usr3"
def writeLED ( filename, value, path=LED3_PATH ):
    "This function writes the passed value to the file in the path"
    fo = open( path + filename,"w")
    fo.write(value)
    fo.close()
    return

def removeTrigger():
    writeLED ("/trigger", value="none")
    return

print "Starting the LED Python Script"

if len(sys.argv)!=2:
    print("Wrong number of arguments")
    sys.exit(2)

if sys.argv[1]== "on":
    print("LED3 on")
    removeTrigger()
    writeLED("/brightness", "1")

elif  sys.argv[1] == "off":
    print("LED3 off")
    removeTrigger()
    writeLED("/brightness", "0")
    
elif sys.argv[1]=="flash":
    print "Flashing the LED3"
    writeLed("/trigger", value="timer")
    writeLed("/brightness", value="50")
    writeLed("/brightness", value="50")
             
else:
    print("Wrong argument")
