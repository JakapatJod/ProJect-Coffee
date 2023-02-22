from tkinter import *

root = Tk()

root.geometry('1270x690+0+0')

root.resizable(0,0)

root.title('Menu Coffee System')
root.config(bg='black') # สี bg

topFrame = Frame(root,bd=10,relief=RIDGE,bg='black')
topFrame.pack(side=TOP)

LabelTitle = Label(topFrame,text='Coffee Menu',font=('Bebas',30,'bold'),fg='black',width=51)
LabelTitle.grid(row=0,column=0)

# frames
menuFrame = Frame(root,bd=10,relief=RIDGE)
menuFrame.pack(side=LEFT)

costFrame = Frame(menuFrame,bd=4,relief=RIDGE)
costFrame.pack(side=BOTTOM)

foodFrame = LabelFrame(menuFrame,text=('Bebas Neue',15,'bold'),bd=10,relief=RIDGE)
foodFrame.pack(side=LEFT)

foodFrame = LabelFrame(menuFrame,text=('Bebas Neue',15,'bold'),bd=10,relief=RIDGE)
foodFrame.pack(side=LEFT)

foodFrame = LabelFrame(menuFrame,text=('Bebas Neue',15,'bold'),bd=10,relief=RIDGE)
foodFrame.pack(side=LEFT)

root.mainloop()