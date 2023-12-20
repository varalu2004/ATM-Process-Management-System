import tkinter
from tkinter import *
import sqlite3
from tkinter import messagebox
conn=sqlite3.connect("test.db")
conn.execute("""CREATE TABLE IF NOT EXISTS DATA
           (id INT PRIMARY KEY NOT NULL,
           cardnumber TEXT NOT NULL,
           pin TEXT NOT NULL,
          balance REAL);""")
def login():
    global Balance
    global bal
#conn.execute("INSERT INTO DATA (id,cardnumber,pin,balance) \
   #   VALUES (1,"64445298794","2004",78000.0)");
#conn.execute("INSERT INTO DATA (id,cardnumber,pin,balance) \
      #VALUES (2,"64445298795","2005",88000.0)");
#conn.execute("INSERT INTO DATA (id,cardnumber,pin,balance) \
 #     VALUES (3,"64445298745","20024",89000.0)");
 
    cursor=conn.execute('SELECT cardnumber,pin FROM DATA where cardnumber=? AND pin=?',(e.get(),e1.get()) )             
    row=cursor.fetchone()
    if row:
        options()
    else:
        messagebox.showinfo("info","login fail")
    cursor=conn.execute('SELECT balance FROM DATA where cardnumber=? AND pin=?',(e.get(),e1.get()))
    Balance=cursor.fetchone()
    bal=','.join(str(i) for i in Balance)
    conn.commit()
def destroy_allscreens():
    e.delete(0,'end')
    e1.delete(0,'end')
    e.icursor(0)
    for widget in root.winfo_children():
        if isinstance(widget,tkinter.Toplevel):
            widget.destroy()
def transactioncompleted():
    lastscreen=Toplevel(root)
    Label(lastscreen,text="Your transaction is successfully completed!",font=("calibri,30"),anchor=CENTER).grid(row=1,column=1,padx=100,pady=20)
    quit=Button(lastscreen,text="close",command=destroy_allscreens,width="20",height="2").grid(row=2,column=2,padx=120,pady=20)
def complete():
    global addaccount1,newbal
    addaccount=amount.get()
    addaccount1=float(addaccount)+float(bal)
    print(addaccount1)
    newbal=StringVar()
    conn.execute('UPDATE DATA SET balance=? WHERE cardnumber=?',(float(addaccount1),e.get()))
    conn.commit()
    Label(screen4,text="Do you want check your current balance:").grid(row=2,column=1,padx=100)
    yes=Button(screen4,text="Yes",width="5",height="2",command=checkbalance).grid(row=3,column=1,padx=100,pady=20)
    no=Button(screen4,text="No",width="5",height="2",command=transactioncompleted).grid(row=4,column=1,padx=100,pady=20)
    amount.delete(0,'end')
def withdrawfunct():
    global currentbal,currbal
    withdrawamt=withdrawamount.get()
    cursor=conn.execute('SELECT balance FROM DATA where cardnumber=? AND pin=?',(e.get(),e1.get()))
    Balance=cursor.fetchone()
    bal=','.join(str(i) for i in Balance)
    if(float(withdrawamt)>float(bal)):
        messagebox.showinfo("info","Insufficent Balance!")
    else:
        currentbal=float(bal)-float(withdrawamt)
        currbal=StringVar()
        conn.execute('UPDATE DATA SET balance=? WHERE cardnumber=?',(float(currentbal),e.get()))
        conn.commit()
        Label(screen6,text="Do you want check your current balance:").grid(row=2,column=1,padx=100)
        yes=Button(screen6,text="Yes",width="5",height="2",command=checkbalance).grid(row=3,column=1,padx=100,pady=10)
        no=Button(screen6,text="No",width="5",height="2",command=transactioncompleted).grid(row=4,column=1,padx=100,pady=10)
        withdrawamount.delete(0,'end')
   
def Deposit():
    global screen4
    screen4=Toplevel(root)
    screen4.geometry("750x500")
    global user_amount
    global amount
    user_amount=float()
    Label(screen4,text="Amount:").grid(row=0,column=1,padx=30,pady=20)
    amount=Entry(screen4,width=20,textvariable=user_amount)
    amount.grid(row=0,column=2,padx=45)
    enterbutton=Button(screen4,text="Next",height="2",width="20",command=complete).grid(row=1,column=2,padx=75,pady=20)
def checkbalance():
    global bal
    screen5=Toplevel(root)
    screen5.geometry("500x250")
    newbal=StringVar()
    cursor=conn.execute('SELECT balance FROM DATA where cardnumber=? AND pin=?',(e.get(),e1.get()))
    Balance=cursor.fetchone()
    bal=','.join(str(i) for i in Balance)
    Label(screen5,text="Current Balance:",font=('calibri,50')).grid(row=0,column=1,padx=30,pady=30)
    Label(screen5,text="Balance:",textvariable=newbal).grid(row=3,column=1,padx=80)
    newbal.set(str(bal))
    next=Button(screen5,text="Next",command=transactioncompleted,height="2",width="15").grid(row=4,column=1,padx=30,pady=20)
def withdraw():
    global screen6
    screen6=Toplevel(root)
    screen6.geometry("750x500")
    global withdraw_amount
    global withdrawamount
    global amount
    withdraw_amount=float()
    Label(screen6,text="Enter the withdrawl Amount:").grid(row=0,column=1,padx=30,pady=20)
    withdrawamount=Entry(screen6,width=20,textvariable=withdraw_amount)
    withdrawamount.grid(row=0,column=2,padx=45)
    enterbutton=Button(screen6,text="Next",height="2",width="20",command=withdrawfunct).grid(row=1,column=2,padx=75,pady=20)   
def options():
    global screen3
    screen3=Toplevel(root)
    screen3.geometry("750x500")
    screen3.title("Select Transcation")
    Label(screen3,text="Select Transaction",font=("calibri,30"),anchor=CENTER).grid(row=0,column=2,padx=100,pady=20)
    deposit=Button(screen3,text="DEPOSIT",width="30",height="2",command=Deposit).grid(row=1,column=0,padx=20,pady=20)
    balanceenquiry=Button(screen3,text="BALANCE ENQUIRY",width="30",height="2",command=checkbalance).grid(row=1,column=2,padx=40,pady=20)
    #transfer=Button(screen3,text="TRANSFER",width="30",height="2").grid(row=2,column=0,padx=20,pady=20)
    cashwithdrawl=Button(screen3,text="CASH WITHDRAWL",width="30",height="2",command=withdraw).grid(row=2,column=0,padx=40,pady=20)
    #pinchange=Button(screen3,text="PINCHANGE",width="30",height="2",anchor=CENTER).grid(row=3,column=0,padx=20,pady=20)
    #balanceenquiry=Button(screen3,text="BALANCE ENQUIRY",width="30",height="2").grid(row=3,column=2,padx=40,pady=20)
def switch_focus(event):
    if event.widget == e:
        e1.focus()
    else:
        e.focus()
  
def main_screen():
    global root
    root=Tk()
    root.geometry("500x500")
    root.title("ATM services")
    label=Label(root,text="Please enter your details",font=("calibri",15),anchor=CENTER).grid(row=0,column=1,pady=20)
    user_input=StringVar()
    password_input=StringVar()
    global e
    global e1
    username=Label(root,text="Cardnumber")
    username.grid(row=1,column=0,padx=25)
    e=Entry(root,width=25,textvariable=user_input)
    e.grid(row=1,column=1)
    password=Label(root,text="Password")
    password.grid(row=2,column=0,pady=20)
    e1=Entry(root,width=25,textvariable=password_input,show='*')
    e1.grid(row=2,column=1)
    enter=Button(root,text="Enter",padx=20,pady=5,command=login).grid(row=4,column=1)
    e.bind("<Return>", switch_focus)
    e1.bind("<Return>", switch_focus)
    root.mainloop()
main_screen()
