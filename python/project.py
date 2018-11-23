# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 15:14:36 2018

@author: Mohamed
"""

import copy
from matplotlib import pyplot as plt
from matplotlib import style
style.use('ggplot')

class Process():
    def __init__(self, id, arrival, burst, priority):
        self.id = id
        self.arrival = arrival
        self.burst = burst
        self.priority = priority
        self.remainingTime = burst
        self.finish = -1

def readProcesses(processArray, filename="pgoutput.txt"):
    with open(filename) as f:
        n = int(f.readline())
        lines = f.readlines()
        for line in lines:
            parameters = line.split(' ')
            processArray.insert(int(parameters[0]) - 1, Process(int(parameters[0]), int(parameters[1]), int(parameters[2]), int(parameters[3])))
        return n
    
def HPF(processArray, n, contextSwitching):
    plt.title('HPF')
    plt.ylabel('Process number')
    plt.xlabel('time')
    x = list()  #numbers on x-axis
    y = list()  #numbers on غ-axis
    readyQueue = list()
    #sort processes according to arrival time then priority reversed then id 
    processArray.sort(key=lambda x: (x.arrival, x.priority * -1, x.id), reverse=False)
    processRunning = False
    time = j = finished = 0
    while(finished < n):     #loop while not all processes finished
        #if current time > arrival of the process 
        while(j < len(processArray) and time >= processArray[j].arrival):
            #add it to ready queue
            readyQueue.append(processArray[j])
            j += 1
        if(len(readyQueue) > 0):
            if(not processRunning): #if no process is currently running
                #sort again the ready queue with reversed priority (decreasing) and increasing id
                readyQueue.sort(key=lambda x: (x.priority, x.id * -1), reverse=True)
                processRunning = True
            readyQueue[0].remainingTime -= 1
            if(readyQueue[0].remainingTime != -1):
                x.append(time)                      #record x-value
                y.append(readyQueue[0].id)          #record y-value
            if(readyQueue[0].remainingTime < 0):    #if process is finished
                readyQueue[0].finish = time         #set the finish time
                readyQueue.pop(0)                   
                finished += 1                       #increment the finished process counter
                time += contextSwitching
                processRunning = False              #allow new process to be popped and run
                time -= 1
        time += 1

    '''z = []
    for process in processArray:
        z.append(process.finish)

    plt.xticks(z, z)
    plt.yticks(y, y)'''
    
    #draw the graph
    plt.bar(x, y, width=1.0, align='edge')
    plt.show()

def RR(processArray, n, contextSwitching, quantam):
    plt.title('RR')
    plt.ylabel('Process number')
    plt.xlabel('time')
    x = list()  #numbers on x-axis
    y = list()  #numbers on y-axis
    readyQueue = list()
    #sort processes according to arrival time then id 
    processArray.sort(key=lambda x: (x.arrival, x.id), reverse=False)
    originalArray = copy.deepcopy(processArray)
    processRunning = False
    time = j = finished = q = 0
    currentProcess = 0
    while(finished < n):    #loop while not all processes finished
        #if current time > arrival of the process 
        while(j < len(processArray) and time >= processArray[j].arrival):
            #add it to ready queue
            readyQueue.append(processArray[j])
            j += 1
        if(len(readyQueue) > 0 or currentProcess != 0):
            if (not processRunning):    #if no process is currently running
                currentProcess = readyQueue.pop(0)
                processRunning = True
            q += 1  #quantam counter
            currentProcess.remainingTime -= 1
            #if process is not finished and we already gave it a quanta
            if(currentProcess.remainingTime >= 0 and q > quantam):
                currentProcess.arrival = time   #new arrival time
                currentProcess.remainingTime += 1   #increase remaining time (calcualtion wise) 
                readyQueue.append(currentProcess)   #push it into the queue
                currentProcess = 0
                #sort again to break ties in case of collision with new inserts at same arrival time
                '''readyQueue.sort(key=lambda x: (x.arrival, x.id), reverse=False)'''
                #add context switching and minus 1 from time (calcualtion wise) 
                time += contextSwitching - 1
                #allow new process to be popped and run
                processRunning = False
                #reset quantam counter
                q = 0

            #if process is finished and we already gave it a quanta
            elif(currentProcess.remainingTime < 0 and q >= quantam):
                currentProcess.finish = time    #set the finish time
                currentProcess = 0
                finished += 1   #increment the finished process counter
                #add context switching and minus 1 from time (calcualtion wise) 
                time += contextSwitching - 1
                #allow new process to be popped and run
                processRunning = False
                #reset quantam counter
                q = 0
            else:   #if process is not finished and its quanta is not done yet
                x.append(time)  #record x-value
                y.append(currentProcess.id) #record y-value
        time += 1
    
    #draw the graph
    plt.bar(x, y, width=1.0, align='edge')
    plt.show()

    #copy finish time from processed array to original one
    for i in range(n):
        originalArray[i].finish = processArray[i].finish

    return originalArray

'''class Scheduler():
    def __init__():
        self.'''
 
processArray = list()   
n = readProcesses(processArray, "pgoutput.txt")
contextSwitching = 0
quantam = 3

#HPF(processArray, n, contextSwitching)

processArray = RR(processArray, n, contextSwitching, quantam)

for i in range(len(processArray)):
    print(processArray[i].id , " ", processArray[i].arrival , " ", processArray[i].burst, " ", processArray[i].priority, " ", processArray[i].finish)
print(n) 



