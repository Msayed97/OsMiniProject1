# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from Process import *

class Scheduler():
   
    def __init__(self):
        self.NumOfProcess = 0
        self.Processes = list()
        self.ActiveProcesses = list()
        self.PrintProcesses = list()
        self.Done = False
        self.Time = 0
        
    def start(self , argument):
         switcher = {
         1: "HPF",
         2: "FCFS",
         3: "RR",
         4: "SRTN",
         }
         x = switcher.get(argument, "Invalid algo")
         
         if(x=="HPF"):
             x=1 ### function of HPF
         elif(x=="FCFS"):
            x=2  ### function of FCFS
         elif(x=="RR"):
             x=3 ### function of RR
         elif(x=="SRTN"):
            x=4  ### function of SRTN

    def AddToScheduler(self , InputFile):
         with open(InputFile) as file:
            self.NumOfProcess = int(file.readline())
            content = file.readlines()
            for pro in content:
                ID , arrival , burst , priority = map(int, pro.split(" "))
                self.Processes.insert( ID-1 , Process( ID ,arrival , burst, priority ))
    
    def SortTime(self):
         self.Processes.sort( key = lambda x: (x.GetArrival() , x.GetID()))
    
    def SortPriority(self):
       self.Processes.sort( key = lambda x: (x.GetPriority() , -x.GetID() ) , reverse=True)
       
    def RefreshProcesses(self):
        for pro in self.Processes:
            if(pro.GetArrival()<=self.Time):
                self.ActiveProcesses.insert(len(self.ActiveProcesses) , pro)
            else:
                break
    def Busy(self , clock):
        for i in range(clock):
            self.Time+=1;
            self.RefreshProcesses()
            
    
        
    
       
g = Scheduler()     
g.AddToScheduler("processes.txt")
g.SortTime()
g.RefreshProcesses()

print(g.NumOfProcess)
for x in g.ActiveProcesses:
    print(x.GetID()  , x.GetArrival() , x.GetBurstTime(), x.GetPriority() )
  
        
