import tkinter
from tkinter import messagebox
import Location
import Gui

class StartPage():
    start=tkinter.Tk()
    zipEntry = tkinter.Entry()
    speedEntry = tkinter.Entry()
    def __init__(self) -> None:
        self.start.resizable(False, False)
        self.start.geometry("450x200")
        self.start.title("Drone-Cast")

        zipLabel = tkinter.Label(self.start, text="Enter Zip Code", font=('Arial',18))
        zipLabel.grid(row=0, column=0,padx=10,pady=20)

        self.zipEntry = tkinter.Entry(self.start, font=('Arial',18))
        self.zipEntry.grid(row=0, column=1)  

        speedLabel = tkinter.Label(self.start, text="Drones Speed (MPH)", font=('Arial',18))
        speedLabel.grid(row=1, column=0,padx=10,pady=20)

        self.speedEntry = tkinter.Entry(self.start, font=('Arial',18))
        self.speedEntry.grid(row=1, column=1)  

        submitButton = tkinter.Button(self.start,text="Submit",font=('Arial',18),command=self.submitButtonAction)
        submitButton.grid(row=2,column=0,pady=1)

        getCurrentLocation = tkinter.Button(self.start,text="Use Current Location",font=('Arial',18),command=self.locationButtonAction)
        getCurrentLocation.grid(row=2,column=1)

        self.start.eval('tk::PlaceWindow . center')  
        self.start.mainloop()

    def submitButtonAction(self):
        zip=self.zipEntry.get()
        speed =self.speedEntry.get()
        if(not(self.zipValidation(zip))):
            tkinter.messagebox.showwarning("Zip Code Error", "Invalid Zip Code")
        elif(not(self.speedValidation(speed))):
            tkinter.messagebox.showwarning("Speed Value Error", "Invalid Speed")
        else:
            win = tkinter.Tk()
            self.start.quit
            self.start.withdraw()
            self.start.destroy()
            x =Gui.Gui(win,zip,speed)


    def zipValidation(self,zip:str):
        if(len(zip)!=5):
            return False
        try:
            tempZip = int(zip)
        except ValueError:
            return False
        return True

    def speedValidation(self, speed:str):
        if(len(speed)<=0):
            return False
        try:
            tempSpeed = int(speed)
        except ValueError:
            return False
        return True

    def locationButtonAction(self):
        #print("Get Location Pressed")
        speed = self.speedEntry.get()
        if(not(self.speedValidation(speed))):
            tkinter.messagebox.showwarning("Speed Value Error", "Invalid Speed")
        else:
            self.start.quit
            self.start.withdraw()
            self.start.destroy()
            win = tkinter.Tk()
            curLocal = Location.Location()
            zip=curLocal.getZip()
            x =Gui.Gui(win,zip,speed)
        