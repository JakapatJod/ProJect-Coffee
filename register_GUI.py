from tkinter import *
from tkinter import messagebox
from PIL import ImageTk

def check_cfm():
    if userEntry.get()=='' or passwordEntry.get()==''or confirmEntry.get()=='' or emailEntry.get()=='' :
        messagebox.showerror('Error','All Fields Are Required')
    elif passwordEntry.get() != confirmEntry.get():
        messagebox.showerror('Error','Password Mismatch')
    elif check.get()==0:
        messagebox.showerror('Error','Please accept Terms & Condtions')
    

def login_page():
    signup_window.destroy()
    import Signin

signup_window = Tk()
signup_window.geometry('1280x720')
signup_window.resizable(False,False)
bgImage = ImageTk.PhotoImage(file='img/bg2.jpg')
signup_window.title("Register")

bgLabel = Label(signup_window,image=bgImage)
bgLabel.grid()

frames = Frame(signup_window)
frames.place(x=500,y=150)


heading = Label(frames,text='CREATE AN ACCOUNT',font=('Bebas',40,'bold'),fg='gray1')
heading.grid(row=0,column=0,padx=10,pady=10) # center heading

# Username
userLabel = Label(frames,text='Username',font = ('Bebas',15),fg='gray1')
userLabel.grid(row=1,column=0,sticky='w',padx=25)
userEntry = Entry(frames,width=30,font=('Bebas',20),fg='gold',bg='gray1')
userEntry.grid(row=2,column=0,sticky='w',padx=25)

# Password
passwordLabel = Label(frames,text='Password',font = ('Bebas',15),fg='gray1')
passwordLabel.grid(row=3,column=0,sticky='w',padx=25)
passwordEntry = Entry(frames,width=30,font=('Bebas',20),fg='gold',bg='gray1')
passwordEntry.grid(row=4,column=0,sticky='w',padx=25)

# Confirm password
confirmLabel = Label(frames,text='Confirm Password',font = ('Bebas',15),fg='gray1')
confirmLabel.grid(row=5,column=0,sticky='w',padx=25)
confirmEntry = Entry(frames,width=30,font=('Bebas',20),fg='gold',bg='gray1')
confirmEntry.grid(row=6,column=0,sticky='w',padx=25)

# Email
emailLabel = Label(frames,text='Email',font = ('Bebas',15),fg='gray1')
emailLabel.grid(row=7,column=0,sticky='w',padx=25)
emailEntry = Entry(frames,width=30,font=('Bebas',20),fg='gold',bg='gray1')
emailEntry.grid(row=8,column=0,sticky='w',padx=25)

check = IntVar()

# terms and con
termsandconditions = Checkbutton(frames,text='I agree to the Terms & Conditions',font=('Bebas',18),fg='red',bg='gray1'
                    ,activebackground='white',activeforeground='gold',cursor='hand2',variable=check)
termsandconditions.grid(row=9,column=0,pady=10)

# Button
signupButton = Button(frames,text='SignUp',font=('Bebas',15),bd=0,fg='white',bg='gray1',width=40,command=check_cfm)
signupButton.grid(row=10,column=0)

# alreadyaccount
alreadyaccount = Label(frames,text="Don't have an account ? ",font=('Bebas',15))
alreadyaccount.grid(row=11,column=0,sticky='w',padx=25)

# Loggin button
loginButton = Button(frames,text='Log in',font=('Bebas',14),fg='blue',bd=0,cursor='hand2',activebackground='white' , activeforeground='blue'
                ,command=login_page)
loginButton.place(x=208,y=454)

signup_window.mainloop()
