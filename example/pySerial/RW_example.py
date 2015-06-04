from serial import *
import time

########## Initialize Serial Port Function  ###########
def InitSerial(PN, BR, T):
    se = Serial(PN - 1, baudrate = BR, timeout =  T)
    if se.isOpen():
        se.close()
    se.open()
    return se
##########          Function End            ###########



##########          Script Start            ###########
se = InitSerial(8,115200,0.01)
while 1:
    stringOut = input()
    se.write(stringOut.encode())
    se.flushOutput()
    time.sleep(0.01)
    stringIn = b''
    while se.inWaiting()>0:
        stringIn += se.read()
    print(stringIn.decode())

##########            Script End            ###########
