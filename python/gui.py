import tkinter as tk

LARGE_FONT= ("Verdana", 12)

class HomePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button = tk.Button(self, text="Process Generator",
                            command=lambda: controller.show_frame(pgPage))
        button.pack()

        button2 = tk.Button(self, text="Scheduler",
                            command=lambda: controller.show_frame(schedularPage))
        button2.pack()

class pgPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Process Generator", font=LARGE_FONT)
        label.pack(pady=10,padx=200)

        self.inputLabel = tk.Label(self, text="Enter input file")
        self.inputLabel.pack()

        self.inputEntry = tk.Entry(self)
        self.inputEntry.pack()

        self.outputLabel = tk.Label(self, text="Enter output file")
        self.outputLabel.pack()

        self.outputEntry = tk.Entry(self)
        self.outputEntry.pack()
        
        self.returnHome = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(HomePage))
        self.returnHome.pack()

        self.generate = tk.Button(self, text="Generate",
                            command= self.genOutfile)
        self.generate.pack()

    def genOutfile(self):
        inputfile = self.inputEntry.get()
        outputfile = self.outputEntry.get()
        print(inputfile,outputfile)       

class schedularPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Scheduler", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        self.inputLabel = tk.Label(self, text="Enter input file")
        self.inputLabel.pack()

        self.inputEntry = tk.Entry(self)
        self.inputEntry.pack()

        self.algoListbox = tk.Listbox(self, height = 4, width = 30)
        self.algoListbox.insert(1, "Highest Priority First")
        self.algoListbox.insert(2, "First Come First Serve")
        self.algoListbox.insert(3, "Round Robin")
        self.algoListbox.insert(4, "Shortest Remaining Time Next")
        self.algoListbox.selection_set(0)
        self.algoListbox.pack(pady= 5)

        self.CSLabel = tk.Label(self, text="Enter Context Switching (only integers)")
        self.CSLabel.pack()

        self.CSEntry = tk.Entry(self)
        self.CSEntry.pack()

        self.quantamLabel = tk.Label(self, text="Enter Quatam for Round Robin (only integers)")
        self.quantamLabel.pack()

        self.quantamEntry = tk.Entry(self)
        self.quantamEntry.pack()

        self.returnHome = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(HomePage))
        self.returnHome.pack()

        self.generate = tk.Button(self, text="Generate",
                            command= self.genOutfile)
        self.generate.pack(pady= 5)

    def genOutfile(self):
        inputfile = self.inputEntry.get()
        contextSwitching = self.CSEntry.get()
        quantam = self.quantamEntry.get()
        mode = self.algoListbox.curselection()
        print(inputfile, contextSwitching, quantam, mode)   

class Application(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.winfo_toplevel().title("OS mini Project 1")

        self.frames = {}
        for F in (HomePage, pgPage, schedularPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(HomePage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

app = Application()
app.mainloop()