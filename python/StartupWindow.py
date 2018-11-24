from tkinter import *
from tkinter.ttk import Radiobutton
class StartupWindow(Frame):
    def __init__(self,master,controller):
        Frame.__init__(self,master)
        generateButton = Button(self,text = 'Generate Processes' , command = lambda: controller.show_frame(GenerateWindow))
        generateButton.pack(fill = BOTH,expand = True)
        scheduleButton = Button(self,text = 'Schedule', command = lambda: controller.show_frame(ScheduleWindow))
        scheduleButton.pack(fill = BOTH,expand = True)

class ScheduleWindow(Frame):
    def __init__(self, master,controller):
        Frame.__init__(self,master)
        label = Label(self,text ='Choose any Algo you want:')
        label.pack(anchor=W , padx = 25 , pady = 5)

        paddingX = 30
        paddingY = 2
        algoNumber = IntVar()
        algo = ['FCFS','HPF','RR','SRTN']
        FCFS = Radiobutton(self,text = algo[0],value = 0 , variable = algoNumber)
        FCFS.pack(anchor=W,padx = paddingX,pady = paddingY)
        HPF = Radiobutton(self,text = algo[1],value = 1 , variable = algoNumber)
        HPF.pack(anchor=W,padx = paddingX,pady = paddingY)
        RR = Radiobutton(self,text = algo[2],value = 2 , variable = algoNumber)
        RR.pack(anchor=W,padx = paddingX,pady = paddingY)
        SRTN = Radiobutton(self,text = algo[3],value = 3 , variable = algoNumber)
        SRTN.pack(anchor=W,padx = paddingX,pady = paddingY)
        contextLabel = Label(self,text ='Context Time')
        contextLabel.pack(anchor=W , padx = 25 , pady = 5)
        contextEntery = Entry(self)
        contextEntery.pack(anchor=W , padx = 30)

        quantLabel = Label(self,text ='Quantum Time')
        quantEntery = Entry(self)
        quantLabel.pack(anchor=W , padx = 25 , pady = 5)
        quantEntery.pack(anchor=W , padx = 30)
        
        schedule = Button(self,text = 'schedule')
        schedule.pack(padx = 25 , pady = 10, expand = True)

class GenerateWindow(Frame):
    def __init__(self, master,controller):
        Frame.__init__(self,master)
        inputLabel = Label(self,text ='Input file name')
        inputLabel.pack(anchor=W , padx = 25 , pady = 5)
        inputEntery = Entry(self)
        inputEntery.pack(anchor=W , padx = 25 , pady = 5)

        outputLabel = Label(self,text ='output file name')
        outputLabel.pack(anchor=W , padx = 25 , pady = 5)

        outputEntery = Entry(self)
        outputEntery.pack(anchor=W , padx = 25 , pady = 5)
        
        generate = Button(self,text = 'generate')
        generate.pack(anchor=W , padx = 25 , pady = 5)

class Application(Tk):
    def __init__(self):
        Tk.__init__(self)
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


root = Application()
root.mainloop()
