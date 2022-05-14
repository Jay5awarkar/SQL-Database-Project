from pymysql import *
from tkinter import *
from tkinter import messagebox
class GUI:
    def __init__(self):
        self.a=Tk()
        self.a.geometry("600x400+350+150")

        self.b=Frame(self.a)
        self.lb1=Label(self.b,text="Rno:",width=15,font=("Times",20,"bold"))
        self.e1=Entry(self.b,font=("Times",20,"bold"))
        self.b.pack(side=TOP,padx=5,pady=5,fill=X)
        self.lb1.pack(side="left")
        self.e1.pack(side="left")

        self.c=Frame(self.a)
        self.lb2=Label(self.c,text="Name",width=15,font=("Times",20,"bold"))
        self.e2=Entry(self.c,font=("Times",20,"bold"))
        self.c.pack(side=TOP,padx=5,pady=5,fill=X)
        self.lb2.pack(side="left")
        self.e2.pack(side="left")

        self.d=Frame(self.a)
        self.lb3=Label(self.d,text="Course",width=15,font=("Times",20,"bold"))
        self.e3=Entry(self.d,font=("Times",20,"bold"))
        self.d.pack(side=TOP,padx=5,pady=5,fill=X)
        self.lb3.pack(side="left")
        self.e3.pack(side="left")

        self.e=Frame(self.a)
        self.lb4=Label(self.e,text="Fees",width=15,font=("Times",20,"bold"))
        self.e4=Entry(self.e,font=("Times",20,"bold"))
        self.e.pack(side=TOP,padx=5,pady=5,fill=X)
        self.lb4.pack(side="left")
        self.e4.pack(side="left")

        self.f=Frame(self.a)
        self.bt1=Button(self.f,text="First",width=15,font=("Times",10,"bold"),command=self.first)
        self.bt2=Button(self.f,text="Prev",width=15,font=("Times",10,"bold"),command=self.prev)
        self.bt3=Button(self.f,text="Next",width=15,font=("Times",10,"bold"),command=self.next)
        self.bt4=Button(self.f,text="Last",width=15,font=("Times",10,"bold"),command=self.last)
        self.f.pack(side=TOP,fill=X,padx=5,pady=5)
        self.bt1.pack(side="left")
        self.bt2.pack(side="left")
        self.bt3.pack(side="left")
        self.bt4.pack(side="left")

        self.g=Frame(self.a)
        self.bt5=Button(self.g,text="Clear",width=15,font=("Times",10,"bold"),command=self.clearall)
        self.bt6=Button(self.g,text="Insert",width=15,font=("Times",10,"bold"),command=self.insert)
        self.bt7=Button(self.g,text="Update",width=15,font=("Times",10,"bold"))
        self.bt8=Button(self.g,text="Delete",width=15,font=("Times",10,"bold"),command=self.delete)
        self.g.pack(side=TOP,fill=X,padx=5,pady=5)
        self.bt5.pack(side="left")
        self.bt6.pack(side="left")
        self.bt7.pack(side="left")
        self.bt8.pack(side="left")

        self.connecttodb()

        self.a.mainloop()

    def connecttodb(self):
        self.h=connect(host="localhost",user="root",password="",db="studentdb")
        self.i=self.h.cursor()
        self.getdata()

    def getdata(self):

        self.i.execute("select * from student")
        self.data=(())
        self.data=self.i.fetchall()
        if self.data:
            self.rowno = 0
            self.showdata()
        

    def showdata(self):

        self.clearall()

        self.e1.insert(0,self.data[self.rowno][0])
        self.e2.insert(0,self.data[self.rowno][3])
        self.e3.insert(0,self.data[self.rowno][2])
        self.e4.insert(0,self.data[self.rowno][1])

    def next(self):
        lastrowno=len(self.data)-1

        if(self.rowno==lastrowno):
            messagebox.showinfo(self.a,"last record")
        else:
            self.rowno=self.rowno+1
            self.showdata()

    def first(self):
        self.rowno=0
        self.showdata()

    def prev(self):
        firstrowno=len(self.data)+1

        if(self.rowno==firstrowno):
            messagebox.showinfo(self.a,"first record")
        else:
            self.rowno=self.rowno-1
            self.showdata()           


    def last(self):
        self.rowno=len(self.data)-1
        self.showdata()

    def clearall(self):
        self.e1.delete(0,END)
        self.e2.delete(0,END)
        self.e3.delete(0,END)
        self.e4.delete(0,END)

    def insert(self):
        rno=self.e1.get()
        name=self.e2.get()
        course=self.e3.get()
        fees=self.e4.get()

        insqry = "INSERT INTO student VALUES ('{}', '{}', '{}', '{}');".format(rno, fees, course, name)
        n=self.i.execute(insqry)
        self.h.commit()
        if(n>0):
            messagebox.showinfo(self.a,"Data inserted sucessfully")
            self.getdata()
        else:
            messagebox.showerror(self.a,"Data insertion error")

    def delete(self):
        rno=self.e1.get()

        delqry="delete from student where ID="+rno
        n=self.i.execute(delqry)
        self.h.commit()

        if(n>0):
            messagebox.showinfo(self.a,"Data deleted sucessfully")
            self.getdata()
        else:
            messagebox.showerror(self.a,"Data deletion error")


if __name__=="__main__":
    obj=GUI()
    


