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
        self.PrintInfo = list()
        self.Done = False
        self.Time = 0
        self.context = 0
        self.quantum = 4
        
    def Draw(self):
        style.use('ggplot')

        for i in self.PrintProcesses:
            plt.bar(i.GetArrival(), i.GetID(), width=i.GetBurstTime(), align='edge')

        plt.show()
#####################################################################################################################################
    def printData(self):
        with open("Data.txt" , 'w+') as file:
            file.write( "number of processes" + str(len(self.PrintInfo)))
            file.write('\n' + "Id " + "wT " + "TAT " + "weightedTAT" )
            AVGTAT = 0
            AVGWTAT= 0
            for i in range(len(self.PrintInfo)):
                file.write('\n' +str(self.PrintInfo[i].GetID()) + " " + str(self.PrintInfo[i].GetWaitingTime()) + " " + str(self.PrintInfo[i].GetTurnAroundTime()) + " " +  str(self.PrintInfo[i].GetWeightedTat()))
                AVGTAT+=self.PrintInfo[i].GetTurnAroundTime()
                AVGWTAT+=self.PrintInfo[i].GetWeightedTat()
            AVGTAT /=len(self.PrintInfo)
            AVGWTAT /=len(self.PrintInfo)
            file.write('\n' +"Average TAT: " + " " + str(AVGTAT) + " " )
            file.write('\n' +"Average weighted TAT: " + " " + str(AVGWTAT) + " " )    

##############################################################################################
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
             self.RR()
             x=3 ### function of RR
             print('RR is choosen')
         elif(x=="SRTN"):
            self.SRTN()
            print('SRTNs is choosen')
            
##############################################################################################
    def FCFS(self):
        while self.NumOfProcess:
            self.RefreshProcesses()
            while len(self.ActiveProcesses):
                brust = self.ActiveProcesses[0].GetBurstTime();
                self.ActiveProcesses[0].SetFinishTime(brust + self.Time)
                self.PrintInfo.append(self.ActiveProcesses[0])
                self.Busy(brust)
                # for easy the DRAW 
                self.PrintProcesses.append(Process(self.ActiveProcesses[0].GetID(),self.Time-brust,brust,self.Time))
                #####################
                self.ActiveProcesses.pop(0)
                self.NumOfProcess -= 1
                self.Busy(self.context)
            self.Time+=1
        self.printData()
        self.Draw()

    def RR(self):
         while self.NumOfProcess:
             self.RefreshProcesses()
             while len(self.ActiveProcesses):
                remaining = self.ActiveProcesses[0].GetRemainingTime();
                if(remaining >= self.quantum):
                    id = self.ActiveProcesses[0].GetID()
                    self.ActiveProcesses[0].SetRemainingTime(self.ActiveProcesses[0].GetRemainingTime()-self.quantum)
                    self.Busy(self.quantum)
                    self.ActiveProcesses.append(self.ActiveProcesses[0])
                    self.ActiveProcesses.pop(0)
                    self.PrintProcesses.append(Process(id,self.Time-self.quantum,self.quantum,1))
                    if id != self.ActiveProcesses[0].GetID():
                        self.Busy(self.context)
                else:
                    self.ActiveProcesses[0].SetFinishTime(remaining + self.Time)
                    self.Busy(remaining)
                    self.PrintInfo.append(self.ActiveProcesses[0])
                

                    self.PrintProcesses.append(Process(self.ActiveProcesses[0].GetID(),self.Time-remaining,remaining,self.Time))
                    self.NumOfProcess -= 1
                    self.ActiveProcesses.pop(0)
                    self.Busy(self.context)
             self.Time+=1
         self.printData()
         self.Draw()
##############################################################################################################################
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
       self.ActiveProcesses.sort( key = lambda x: (x.GetRemainingTime() , x.GetID() ) )
       
    def RefreshProcesses(self):
        for pro in self.Processes:
            if(pro.GetArrival() == self.Time):
                self.ActiveProcesses.append(pro)
            elif (pro.GetArrival() > self.Time):
                break
    def Busy(self , clock):
        for i in range(clock):
            self.Time+=1
            self.RefreshProcesses()
            
    def HPF(self):
       
        while self.NumOfProcess:
            self.RefreshProcesses()
            self.SortPriority()
            while len(self.ActiveProcesses):
                brust = self.ActiveProcesses[0].GetBurstTime();
                self.ActiveProcesses[0].SetFinishTime(brust + self.Time)
                self.PrintInfo.append(self.ActiveProcesses[0])
                self.Busy(brust)
                self.PrintProcesses.append(Process(self.ActiveProcesses[0].GetID(),self.Time-brust,brust,self.Time))
                self.ActiveProcesses.pop(0)
                self.NumOfProcess -= 1
                
                self.SortPriority()
                self.Busy(self.context)
              
            self.Time+=1
        self.printData()
        self.Draw()    
                
            # kharaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa############################
    def SRTN(self):
       
        while self.NumOfProcess:
            self.RefreshProcesses()
            self.SortRemainingTime()
            while len(self.ActiveProcesses):
                id = self.ActiveProcesses[0].GetID()
                p = self.ActiveProcesses[0]
                end = True
                counter =0 
                while self.ActiveProcesses[0].GetRemainingTime():
                    self.Time+=1
                    counter+=1
                    p.SetRemainingTime(p.GetRemainingTime() - 1)
                    self.RefreshProcesses()
                    self.SortRemainingTime()
                    if id!=self.ActiveProcesses[0].GetID():
                       self.PrintProcesses.append(Process(p.GetID(),self.Time-counter,counter,self.Time)) 
                       self.Busy(self.context)
                       end= False
                       break
                if(end):
                    self.ActiveProcesses[0].SetFinishTime(self.Time)
                    self.PrintInfo.append(self.ActiveProcesses[0])
                    self.PrintProcesses.append(Process(self.ActiveProcesses[0].GetID(),self.Time-counter,counter,self.Time))
                    self.NumOfProcess -= 1
                    self.ActiveProcesses.pop(0)
                    self.Busy(self.context)
            self.Time+=1
        self.printData()
        self.Draw()  

        
            

    
        
    
       
#g = Scheduler()     
#g.AddToScheduler("processes.txt")
#g.SortTime()
#g.RefreshProcesses()

#print(g.NumOfProcess)
#for x in g.ActiveProcesses:
#    print(x.GetID()  , x.GetArrival() , x.GetBurstTime(), x.GetPriority() )
  
        
