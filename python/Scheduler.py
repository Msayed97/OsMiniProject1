# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from matplotlib import pyplot as plt
from matplotlib import style

from Process import *
class Scheduler():
   
    def __init__(self):
        self.NumOfProcess = 0
        self.Processes = list()
        self.ActiveProcesses = list()
        self.PrintProcesses = list()
        self.Done = False
        self.Time = 0
        self.context = 0
        self.quantum = 0
        
    def Draw(self):
        style.use('ggplot')

        for i in self.PrintProcesses:
            plt.bar(i.GetArrival(), i.GetID(), width=i.GetBurstTime(), align='edge')

        plt.show()

    def start(self , argument , cont , quant):
         if cont != "":
            self.context  = int(cont) 
         if quant != "":
            self.quantum = int(quant)
         switcher = {
         1: "HPF",
         2: "FCFS",
         3: "RR",
         4: "SRTN",
         }
         x = switcher.get(argument, "Invalid algo")
         
         if(x=="HPF"):
             x=1 ### function of HPF
             print('HPF is choosen')
         elif(x=="FCFS"):
            self.FCFS()  ### function of FCFS
            print('FCFS is choosen')
         elif(x=="RR"):
             x=3 ### function of RR
             print('RR is choosen')
         elif(x=="SRTN"):
            x=4  ### function of SRTN
            print('SRTNs is choosen')
###############################################
    def FCFS(self):
        while self.NumOfProcess:
            self.RefreshProcesses()
            for i,p in enumerate(self.ActiveProcesses):
                if i >= len(self.ActiveProcesses):
                    print(i,len(self.ActiveProcesses))
                brust = self.ActiveProcesses[i].GetBurstTime();
                self.ActiveProcesses[i].SetFinishTime(brust + self.Time)
                self.Busy(brust)
                # for easy the DRAW 
                self.ActiveProcesses[i].SetArrival(self.Time-brust)
                #####################
                self.PrintProcesses.append(self.ActiveProcesses[i])
                self.ActiveProcesses.pop(i)
                self.NumOfProcess -= 1
                self.Busy(self.context)
            self.Time+=1
        for x in self.PrintProcesses:
            print(x.GetFinishTime())
        self.Draw()



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
            if(pro.GetArrival() == self.Time):
                self.ActiveProcesses.append(pro)
            elif (pro.GetArrival() > self.Time):
                break
    def Busy(self , clock):
        for i in range(clock):
            self.Time+=1;
            self.RefreshProcesses()
            
    
        
    
       
#g = Scheduler()     
#g.AddToScheduler("processes.txt")
#g.SortTime()
#g.RefreshProcesses()

#print(g.NumOfProcess)
#for x in g.ActiveProcesses:
#    print(x.GetID()  , x.GetArrival() , x.GetBurstTime(), x.GetPriority() )
  
        
