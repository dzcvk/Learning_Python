from serial import *
#from threading import thread
import threading
from time import sleep

########## Initialize Serial Port Function  ###########
def InitSerial(PN, BR, T):
    se = Serial(PN - 1, baudrate = BR, timeout =  T)
    if se.isOpen():
        se.close()
    se.open()
    return se
##########          Function End            ###########

def ReadSerial(se):
    stringIn = b''
    while 1:
        while se.inWaiting()>0:
            stringIn = se.readline()
            print(stringIn.decode())

def WriteSerial(se):
    while 1:
        stringOut = input()
        se.write(stringOut.encode())

##########          Script Start            ###########
se = InitSerial(8,115200,0.01)

threads = []
Task1 = threading.Thread(target = ReadSerial,args = (se,))
threads.append(Task1)
Task1.start()

while 1:
    WriteSerial(se)

##########            Script End            ###########
