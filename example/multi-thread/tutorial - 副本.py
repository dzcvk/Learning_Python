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

##########          Task 1            ###########

def ReadSerial():
    stringIn = b''
    while 1:
        print('1')
        sleep(1)

##########          End               ###########
            
##########          Task 2            ###########
def WriteSerial():
    while 1:
        print('2')
        sleep(1)
##########          End               ###########

#se = InitSerial(8,115200,0.01)

string = 'haha'
threads = []
t1 = threading.Thread(target = ReadSerial(), args = (se,))
threads.append(t1)
t2 = threading.Thread(target = WriteSerial(), args = (se,))
threads.append(t2)

for task in threads:
    task.setDaemon(True)
    task.start()

##########            Script End            ###########
