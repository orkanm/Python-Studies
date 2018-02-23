# This python script created for synchronizing two different thread through an event.
# Maintainer: Orkan Murat CELIK.

#!/usr/bin/python
import threading # Import threading module.

event = threading.Event() # Create an event to sync threads.

def firstThread(): # Define a function to use as thread.
    print "firstThread is started..."  
    for i in range(0,5):
        print i
        if i == 1:
            event.wait() # Wait for the event to run.
    print "firstThread is end."

def secondThread(): # Define a function to use as thread.
    print "secondThread is started..."
    print "secondThread is end."
    event.set() # set  event flag. After that firstThread continue to run.

# Describe functions as threads and run as follows.
try:
    t1 = threading.Thread(target = firstThread) # Define "firstThread()" function as thread and assign it to "t1".
    t2 = threading.Thread(target = secondThread) # Define "secondThread()" function as thread and assign it to "t2".   
    t1.start() # Start first thread.
    t2.start() # Start second thread.
except:
   print "Error: unable to start thread"

while 1:
   pass