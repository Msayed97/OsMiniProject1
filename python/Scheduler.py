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
             self.HPF()
             print('HPF is choosen')
         elif(x=="FCFS"):
            self.FCFS()  ### function of FCFS
            print('FCFS is choosen')
         elif(x=="RR"):
             x=3 ### function of RR
             print('RR is choosen')
         elif(x=="SRTN"):
            self.SRTN()
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
       self.ActiveProcesses.sort( key = lambda x: (x.GetPriority() , -x.GetID() ) , reverse=True)
    def SortRemainingTime(self):
       self.ActiveProcesses.sort( key = lambda x: (x.GetRemainingTime() , -x.GetID() ) , reverse=True)
       
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
            
    def HPF(self):
       
        while self.NumOfProcess:
            self.RefreshProcesses()
            self.SortPriority()
            while len(self.ActiveProcesses):
                brust = self.ActiveProcesses[0].GetBurstTime();
                self.ActiveProcesses[0].SetFinishTime(brust + self.Time)
                self.Busy(brust)
                 
                self.ActiveProcesses[0].SetArrival(self.Time-brust)
                self.PrintProcesses.append(self.ActiveProcesses[0])
                self.ActiveProcesses.pop(0)
                self.NumOfProcess -= 1
                
                self.SortPriority()
                self.Busy(self.context)
              
            self.Time+=1
        self.Draw()       
                
            # kharaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa############################
    def SRTN(self):
       
        while self.NumOfProcess:
            self.RefreshProcesses()
            self.SortRemainingTime()
            while len(self.ActiveProcesses):
                if(self.ActiveProcesses[0].GetRemainingTime() <= self.quantum):
                    remainingTime = self.ActiveProcesses[0].GetRemainingTime()
                    self.ActiveProcesses[0].SetFinishTime(remainingTime + self.Time)
                    self.Busy(remainingTime)
                
                    self.ActiveProcesses[0].SetArrival(self.Time-remainingTime)
                    self.PrintProcesses.append(self.ActiveProcesses[0])
                    self.ActiveProcesses.pop(0)
                    self.NumOfProcess -= 1
                    self.SortRemainingTime()
                    self.Busy(self.context)
                   #### should handle when there gone happen 2 or more context switching in row
                   
                else:
                    id = self.ActiveProcesses[0].GetID()
                    remainingTime = self.ActiveProcesses[0].GetRemainingTime()
                    self.ActiveProcesses[0].SetRemainingTime(remainingTime - self.quantum)
                    self.ActiveProcesses[0].SetFinishTime(self.quantum + self.Time)
                    self.Busy(self.quantum)
                    self.ActiveProcesses[0].SetArrival(self.Time-self.quantum)
                    self.PrintProcesses.append(self.ActiveProcesses[0])
                    self.SortRemainingTime()
                    if(id != self.ActiveProcesses[0].GetID()):
                         self.Busy(self.context)
                         
                        
            self.Time+=1
        self.Draw()       

        
            

    
        
    
       
#g = Scheduler()     
#g.AddToScheduler("processes.txt")
#g.SortTime()
#g.RefreshProcesses()

#print(g.NumOfProcess)
#for x in g.ActiveProcesses:
#    print(x.GetID()  , x.GetArrival() , x.GetBurstTime(), x.GetPriority() )
  
        
