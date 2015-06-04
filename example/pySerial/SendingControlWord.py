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
se = InitSerial(6,14400,0.01)
while 1:
    se.write('W'.encode())
    se.write(b'\x01')
    se.write(b'\x80')
    time.sleep(1)
    se.write('W'.encode())
    se.write(b'\x01')
    se.write(b'\x00')
    time.sleep(1)


##########            Script End            ###########
