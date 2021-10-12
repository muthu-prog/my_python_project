from tkinter import *
from tkinter import ttk
from Dataset import author_Name,book_Name,price,version,publishing_year
from Display import *
from Warning import *
root = Tk()
root.geometry("600x400")
root.resizable(0,0)
root.title("Muthu")

Author_Name_Var=StringVar()
Publish_year_Var=StringVar()

def Find():
    filter=Filter.get()
    name=Author_Name_Var.get()
    year=Publish_year_Var.get()
    if(len(name)>0 and len(year)>0):
        aname=[]
        bname=[]
        pyear=[]
        ver=[]
        pr=[]
        for i in range(0,len(author_Name)):
            if author_Name[i]==name and publishing_year[i]==int(year):
                aname.append(author_Name[i])
                bname.append(book_Name[i])
                pyear.append(publishing_year[i])
                ver.append(version[i])
                pr.append(price[i])
        if(len(aname)>0):
            Display(bname,aname,pyear,ver,pr,len(aname))
        else:
            Warning("No Match Found")
    elif(len(name)>0):
        aname=[]
        bname=[]
        pyear=[]
        ver=[]
        pr=[]
        for i in range(0,len(author_Name)):
            if author_Name[i]==name:
                aname.append(author_Name[i])
                bname.append(book_Name[i])
                pyear.append(publishing_year[i])
                ver.append(version[i])
                pr.append(price[i])
        if(len(aname)>0):
            Display(bname,aname,pyear,ver,pr,len(aname))
        else:
            Warning("No Match Found")
    elif(filter=="Price"):
        for i in range(0,len(price)-1):
            for j in range(i+1,len(price)):
                if(price[j]<price[i]):
                    price[j], price[i] = price[i], price[j]
                    author_Name[j],author_Name[i]=author_Name[i],author_Name[j]
                    book_Name[j],book_Name[i]=book_Name[i],book_Name[j]
                    version[j],version[i]=version[i],version[j]
                    publishing_year[j],publishing_year[i]=publishing_year[i],publishing_year[j]
        Display(book_Name,author_Name,publishing_year,version,price,len(price))
    elif(filter=="Author & Year"):
        for i in range(0,len(publishing_year)-1):
            for j in range(i+1,len(publishing_year)):
                if(publishing_year[j]<publishing_year[i]):
                    price[j], price[i] = price[i], price[j]
                    author_Name[j],author_Name[i]=author_Name[i],author_Name[j]
                    book_Name[j],book_Name[i]=book_Name[i],book_Name[j]
                    version[j],version[i]=version[i],version[j]
                    publishing_year[j],publishing_year[i]=publishing_year[i],publishing_year[j]
        Display(book_Name,author_Name,publishing_year,version,price,len(price))
    else:
        Warning("Enter Valid data")
    Filter.set("")
    Author_Name_Var.set("")
    Publish_year_Var.set("")

Label(root,text="Author_Name",font=18).place(x=100,y=100)
AuthName_entry=Entry(root,textvariable=Author_Name_Var).place(x=230,y=105)
Label(root,text="Publish_Year",font=18).place(x=100,y=125)
Publish_year_entry=Entry(root,textvariable=Publish_year_Var).place(x=230,y=130)

ttk.Label(root, text = "Sort By : ",font = ("Times New Roman", 18)).place(x=100,y=180)

n = StringVar()
Filter = ttk.Combobox(root, width = 27, textvariable = n)
Filter['values'] = ('Price','Author & Year')  

Filter.place(x=230,y=185)

Filter.current()

Button(root,text="Find",command=Find,bg="blue",fg="white",font=20).place(x=250,y=230)
root.mainloop()