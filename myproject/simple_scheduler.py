import subprocess
from datetime import datetime
import logging
import time


logFile = "log.log"
UiRobot = r'C:\Users\aagent\AppData\Local\UiPath\app-19.2.0\UiRobot.exe'
init = r'C:\Users\aagent\Documents\UiPath\StatusUpdate\Main.xaml'
a = r'C:\Users\aagent\Documents\UiPath\Delegate Access\Main.xaml'
b = r'C:\Users\aagent\Documents\UiPath\Skype Account Enable\Main.xaml'
c = r'C:\Users\aagent\Documents\UiPath\TimeCard\Main.xaml'
logging.basicConfig(filename=logFile,level=logging.DEBUG)

#aTask = subprocess.call((UiRobot+" /file:\""+a+"\""), shell=True)
#bTask = subprocess.call((UiRobot+" /file:\""+b+"\""), shell=True)
#cTask = subprocess.call((UiRobot+" /file:\""+c+"\""), shell=True)

def taskInit():
    logging.info(tstamp()+" : 'Change Status to In Progress' flow has started.")
    initTask = subprocess.call((UiRobot+" /file:\""+init+"\""), shell=True)
    if initTask != 0:
        taskInit()
        logging.debug(tstamp()+" : 'Change Status to In Progress' flow has been restarted after error code: "+str(aTask)+" was recieved")
    elif initTask == 0:
        logging.info(tstamp()+" : 'Change Status to In Progress' flow ended with code: 0")
    return initTask

def taskA():
    logging.info(tstamp()+" : 'Delegate Access' flow has started.")
    aTask = subprocess.call((UiRobot+" /file:\""+a+"\""), shell=True)
    if aTask != 0:
        taskA()
        logging.debug(tstamp()+" : 'Delegate Access' flow has been restarted after error code: "+str(aTask)+" was recieved")
    elif aTask == 0:
        logging.info(tstamp()+" : 'Delegate Access' flow ended with code: 0")
    return aTask

def taskB():
    logging.info(tstamp()+" : 'Skype Account Enable' flow has started.")
    bTask = subprocess.call((UiRobot+" /file:\""+b+"\""), shell=True)
    if bTask != 0:
        taskB()
        logging.debug(tstamp()+" : 'Skype Account Enable' flow has been restarted after error code: "+str(bTask)+" was recieved")
    elif bTask == 0:
        logging.info(tstamp()+" : 'Skype Account Enable' flow ended with code: 0")
    return bTask

def taskC():
    logging.info(tstamp()+" : 'Timecard' flow has started.")
    cTask = subprocess.call((UiRobot+" /file:\""+c+"\""), shell=True)
    if cTask != 0:
        taskC()
        logging.debug(tstamp()+" : 'Timecard' flow has been restarted after error code: "+str(cTask)+" was recieved")
    elif cTask == 0:
        logging.info(tstamp()+" : 'Timecard' flow ended with code: 0")
    return cTask

def tstamp():
    return (str(datetime.now()))

while (1):
     initReturn = taskInit()
     time.sleep(240)
     
    
