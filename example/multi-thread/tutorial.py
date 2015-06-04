from serial import *
#from threading import thread
import threading
from time import sleep


##########          Task 1            ###########

def Task1(string1):
    sleep(0.5)
    while 1:
        print(string1)
        sleep(1)

##########          End               ###########
            
##########          Task 2            ###########
def Task2(string2):
    while 1:
        print(string2)
        sleep(1)
##########          End               ###########
string1 = 'haha'
string2 = 'hehe'
threads = []
t1 = threading.Thread(target = Task1,args = (string1,))
threads.append(t1)
t2 = threading.Thread(target = Task2,args = (string2,))
threads.append(t2)

for task in threads:
    task.setDaemon(True)
    task.start()

##########            Script End            ###########
