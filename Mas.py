from tkinter import *

def register_user():
    username_info = username.get()
    password_info = password.get()
    file=open(username_info+".txt","w")
    file.write(username_info+"\n")
    file.write(password_info)
    file.close()

    username_Entry.delete(0,END)
    password_Entry.delete(0,END)
    Label(screen,text = "Register successfull",fg = "green",font=("calibri",11)).pack()

def register():
    global screen1
    screen1=Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x250")
    global username
    global password
    global username_Entry
    global password_Entry
    username=StringVar()
    password=StringVar()

    Label(screen1,text="Please Enter Details below").pack()
    Label(screen1, text="").pack()
    Label(screen1,text="username *").pack()
    username_Entry=Entry(screen1,textvariable=username)
    username_Entry.pack()
    Label(screen1,text="password *").pack()
    password_Entry=Entry(screen1,textvariable=password)
    password_Entry.pack()
    Label(screen1, text="").pack()
    Button(screen1,text = "Register", width=12,height=1,command=register_user).pack()

def login():
    print("Login success")
def main_screen():
    global screen
    screen =Tk()
    screen.geometry("300x250")
    screen.title("Notes 1.0")
    Label(text = "Notes 1.0", bg="grey",width="300",height="3",font=("Calibri",13)).pack()
    Label (text ="").pack()
    Button (text ="Login",width="30",height=" 3",command=login).pack()
    Label(text="").pack()
    Button(text = "Register",width="30",height=" 3",command=register).pack()
    screen.mainloop()
main_screen()