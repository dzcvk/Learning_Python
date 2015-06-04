from serial import *
import threading
from time import sleep
from msvcrt import getch
from msvcrt import putch
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
            stringIn = se.read()
            print(stringIn.decode('utf8',errors='ignore'),end='')

def WriteSerial(se):
    while 1:
        charOut = getch()
        if charOut != b'\xff':
            se.write(charOut)

##########          Script Start            ###########
se = InitSerial(8,115200,0.01)

threads = []
Task1 = threading.Thread(target = ReadSerial,args = (se,))
threads.append(Task1)
Task1.start()

WriteSerial(se)

##########            Script End            ###########
