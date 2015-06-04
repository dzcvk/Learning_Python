from serial import *
#from threading import thread
import threading
from time import sleep
from msvcrt import getch



########## Initialize Serial Port Function  ###########
def InitSerial(PN, BR, T):
    se = Serial(PN - 1, baudrate = BR, timeout =  T)
    if se.isOpen():
        se.close()
    se.open()
    return se


def WriteSerial(se):
    while 1:
        #print("debug Write ff")
        charOut = getch()
        #print(charOut)
        if charOut != b'\xff':
            print(charOut.decode())
            #print(charOut)
            #se.write(charOut)
        #se.flushOutput()
        #sleep(0.5)
        #print("debug"+stringOut)

se = InitSerial(8,115200,0.01)
while 1:
    WriteSerial(se)
