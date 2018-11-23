# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 18:27:21 2018

@author: Mohamed
"""

import numpy as np

class ProcessGenerator():
    def __init__(self, name="input.txt"):
        self.FileName = name
        self.NumOfProcesses = 0
        self.ArrivalTMean = 0
        self.ArrivalTVariance = 0
        self.BurstTMean = 0
        self.BurstTVariance = 0
        self.priorityLambda = 0        
           
    def ReadInput(self):
        with open(self.FileName) as file:
            content = file.readlines()
            self.NumOfProcesses = int(content[0])
            self.ArrivalTMean , self.ArrivalTVariance = map(float, content[1].split(" "))
            self.BurstTMean , self.BurstTVariance = map(float, content[2].split(" "))
            self.priorityLambda = float(content[3])

    def GenerateOutput(self, outputName="processes.txt"):
        ArrivalTimes = np.random.normal(self.ArrivalTMean, self.ArrivalTVariance, self.NumOfProcesses).astype(int)
        BustTimes = np.random.normal(self.BurstTMean, self.BurstTVariance, self.NumOfProcesses).astype(int)
        Prioritys = np.random.poisson(self.priorityLambda, self.NumOfProcesses)
        with open(outputName , 'w+') as file:
            file.write(str(self.NumOfProcesses))
            for i in range(self.NumOfProcesses):
                file.write('\n' + str(i+1) + " " + str(ArrivalTimes[i]) + " " + str(BustTimes[i]) + " " + str(Prioritys[i]))


pg = ProcessGenerator("input.txt")
pg.ReadInput()
pg.GenerateOutput()



