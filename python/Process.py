# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
class Process():
    
    def __init__(self, d, arrival, burst, priority):
       self.__Id =self.SetID(d)
       self.__ArrivalTime=self.SetArrival(arrival)
       self.__BurstTime=self.SetBurstTime(burst)
       self.__RemainingTime=self.SetRemainingTime(burst)
       self.__Priority=self.SetPriority(priority)
       self.__FinishTime=self.SetFinishTime(0)

##############Get functions###########################################################
    def GetID(self):
        return self.__Id
    
    def GetArrival(self):
        return self.__ArrivalTime

    def GetBurstTime(self):
        return self.__BurstTime
    
    def GetRemainingTime(self):
        return self.__RemainingTime
    
    def GetPriority(self):
        return self.__Priority
    
    def GetTurnAroundTime(self):
         self.__FinishTime - self.__ArrivalTime
    
    def GetWeightedTat(self):
        return self.TurnAroundTime / self.__BurstTime
    
    
    def GetFinishTime(self):
        return self.__FinishTime
    #################################def of Set functions#####################################
    def SetID(self , value):
        if(value >=0):
            self.__Id = value
    
    
    def SetArrival(self , value):
        if(value >=0):
            self.__ArrivalTime = value
            
    def SetBurstTime(self , value):
        if(value >=0):
            self.__BurstTime = value
            
    def SetRemainingTime(self , value):
        if(value >=0):
            self.__RemainingTime = value
            
    def SetPriority(self , value):
        if(value >=0):
            self.__Priority = value

    def SetFinishTime(self , value):
        if(value >=0):
            self.__FinishTime = value
            
            

    
    
    

g = Process(1,2,3,4)