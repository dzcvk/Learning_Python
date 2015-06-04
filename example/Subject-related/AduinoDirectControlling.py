from serial import *
import threading
from time import sleep
from msvcrt import getch
from msvcrt import putch


#######################################################

Reg = {'POB':b'x00','POC':b'x01','POD':b'x02','POE':b'x03','POF':b'x04'}



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
            print(stringIn)

def WriteSerial(se):
    while 1:
        #turn on the LED
        se.write('W'.encode())
        se.write(Reg['POC'])
        se.write(b'\xf0')
        #read the value of GPIOB
        se.write('R'.encode())
        se.write(Reg['POC'])
        se.write(b'\xf0')
        sleep(2)
        #turn off the LED
        se.write('W'.encode())
        se.write(Reg['POC'])
        se.write(b'\x00')
        #read the value of GPIOB
        se.write('R'.encode())
        se.write(Reg['POC'])
        se.write(b'\x00')
        sleep(2)
##########          Script Start            ###########
se = InitSerial(8,14400,0.01)

threads = []
Task1 = threading.Thread(target = ReadSerial,args = (se,))
threads.append(Task1)
Task1.start()

WriteSerial(se)

##########            Script End            ###########
