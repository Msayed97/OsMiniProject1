from tkinter import *
from tkinter.ttk import Radiobutton
from Scheduler import *
from ProcessGenerator import *

class StartupWindow(Frame):
    def __init__(self,master,controller):
        Frame.__init__(self,master)
        generateButton = Button(self,text = 'Generate Processes' , command = lambda: controller.show_frame(GenerateWindow), bg = "#0FF")
        generateButton.pack(fill = BOTH,expand = True)
        scheduleButton = Button(self,text = 'Schedule', command = lambda: controller.show_frame(ScheduleWindow),bg = "#FF0")
        scheduleButton.pack(fill = BOTH,expand = True)

#################################################################################################################################################

class ScheduleWindow(Frame):
    def __init__(self, master,controller):
        Frame.__init__(self,master)
        self.config(bg = "#FF0")
        self.controller = controller
        label = Label(self,text ='Choose any Algo you want:')
        label.pack(anchor=W , padx = 25 , pady = 5)

        paddingX = 30
        paddingY = 2
        #choosing which algo
        self.algoNumber = IntVar()
        self.algoNumber.set(1)
        algo = ['HPF','FCFS','RR','SRTN']
        FCFS = Radiobutton(self,text = algo[0],value = 1 , variable = self.algoNumber)
        FCFS.pack(anchor=W,padx = paddingX,pady = paddingY)
        HPF = Radiobutton(self,text = algo[1],value = 2 , variable = self.algoNumber)
        HPF.pack(anchor=W,padx = paddingX,pady = paddingY)
        RR = Radiobutton(self,text = algo[2],value = 3 , variable = self.algoNumber)
        RR.pack(anchor=W,padx = paddingX,pady = paddingY)
        SRTN = Radiobutton(self,text = algo[3],value = 4 , variable = self.algoNumber)
        SRTN.pack(anchor=W,padx = paddingX,pady = paddingY)
        
        #add required Data
        contextLabel = Label(self,text ='Context Time')
        contextLabel.pack(anchor=W , padx = 25 , pady = 5)
        self.contextEntery = Entry(self)
        self.contextEntery.pack(anchor=W , padx = 30)

        quantLabel = Label(self,text ='Quantum Time')
        self.quantEntery = Entry(self)
        quantLabel.pack(anchor=W , padx = 25 , pady = 5)
        self.quantEntery.pack(anchor=W , padx = 30)
        #  scheduling button
        schedule = Button(self,text = 'schedule' , command = self.startScheduling )
        schedule.pack(padx = 25 , pady = 10, expand = True )
    
    def startScheduling(self):
        sch = Scheduler()
        sch.AddToScheduler(self.controller.outputText)
        sch.SortTime()
        sch.start(self.algoNumber.get(),self.contextEntery.get(),self.quantEntery.get())

####################################################################################################################################

class GenerateWindow(Frame):
    def __init__(self, master,controller):
        Frame.__init__(self,master)
        self.controller = controller
        self.config(bg = "#0FF")
        self.inputLabel = Label(self,text ='Input file name')
        self.inputLabel.pack(anchor=W , padx = 25 , pady = 5)
        self.inputEntery = Entry(self)
        self.inputEntery.pack(anchor=W , padx = 25 , pady = 5)

        self.outputLabel = Label(self,text ='output file name')
        self.outputLabel.pack(anchor=W , padx = 25 , pady = 5)

        self.outputEntery = Entry(self)
        self.outputEntery.pack(anchor=W , padx = 25 , pady = 5)
        
        generate = Button(self,text = 'generate',command = self.generateFile)
        generate.pack(anchor=W , padx = 25 , pady = 5)
        back = Button(self,text = 'back',command = lambda: controller.show_frame(StartupWindow))
        back.pack(anchor=W , padx = 25 , pady = 5)
        # when click generate
    def generateFile(self):
        Label(self,text="done generation").pack()
        self.controller.inputText = self.inputEntery.get()
        self.controller.outText = self.outputEntery.get()
        p = ProcessGenerator(self.controller.inputText)
        p.ReadInput()
        p.GenerateOutput(self.controller.outText)

#################################################################################################################################################

class Application(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.inputText = "input.txt"
        self.outputText = "output.txt"
        self.minsize(300,300)
        self.maxsize(300,300)
        container = Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.winfo_toplevel().title("OS mini Project 1")
        self.frames = {}
        for i in (StartupWindow,ScheduleWindow,GenerateWindow):
            frame = i(container, self)
            self.frames[i] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartupWindow)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
