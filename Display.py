from tkinter import *

def Display(b_n,a_n,p_y,v,p,length):
    Display=Tk()
    Display.title("Muthu")
    Display.minsize(1000,800)
    Display.resizable(0,0)
    Label(Display,text="Author Name",font=18).place(x=0,y=0)
    Label(Display,text="Boook Name",font=18).place(x=250,y=0)
    Label(Display,text="Published Year",font=18).place(x=500,y=0)
    Label(Display,text="Version",font=18).place(x=750,y=0)
    Label(Display,text="Price",font=18).place(x=900,y=0)
    a_y=50
    b_y=50
    pu_y=50
    v_y=50
    pr_y=50
    for i in range(0,length):
        Label(Display,text=a_n[i],font=10).place(x=0,y=a_y)
        a_y+=50
        Label(Display,text=b_n[i],font=10).place(x=250,y=b_y)
        b_y+=50
        Label(Display,text=p_y[i],font=10).place(x=500,y=pu_y)
        pu_y+=50
        Label(Display,text=v[i],font=10).place(x=750,y=v_y)
        v_y+=50
        Label(Display,text=p[i],font=10).place(x=900,y=pr_y)
        pr_y+=50
