from tkinter import *

def Warning(msg):
    Warning=Tk()
    Warning.title("Muthu")
    Warning.minsize(200,200)
    Warning.resizable(0,0)
    Label(Warning,text=msg,font=18,fg="red").place(x=30,y=80)
