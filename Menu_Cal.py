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

coffeeFrame = LabelFrame(menuFrame,text='Coffee\tHOT  COLD',font=('Bebas Neue',20,'bold'),bd=10,relief=RIDGE,bg='gold',fg='black')
coffeeFrame.pack(side=LEFT)

teaFrame = LabelFrame(menuFrame,text='Tea\t        HOT  COLD',font=('Bebas Neue',20,'bold'),bd=10,relief=RIDGE,bg='black',fg='Red')
teaFrame.pack(side=LEFT)

dessertFrame = LabelFrame(menuFrame,text='Dessert',font=('Bebas Neue',20,'bold'),bd=10,relief=RIDGE)
dessertFrame.pack(side=LEFT)

rightFrame = Frame(root,bd=15,relief=RIDGE)
rightFrame.pack(side=RIGHT)

calculatorFrame = Frame(rightFrame,bd=1,relief=RIDGE)
calculatorFrame.pack

recieptFrame = Frame(rightFrame,bd=4,relief=RIDGE)
recieptFrame.pack()

buttonFrame = Frame(rightFrame,bd=4,relief=RIDGE)
buttonFrame.pack()

# Variables
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()
var17 = IntVar()
var18 = IntVar()


# Varriable Coffee
e_esp1 = StringVar()
e_esp2 = StringVar()

e_cap1 = StringVar()
e_cap2 = StringVar()

e_lat1 = StringVar()
e_lat2 = StringVar()

e_moc1 = StringVar()
e_moc2 = StringVar()

e_ame1 = StringVar()
e_ame2 = StringVar()

e_mac1 = StringVar()
e_mac2 = StringVar()

# Varriable Tea
e_green1 = StringVar()
e_green2 = StringVar()

e_black1 = StringVar()
e_black2 = StringVar()

e_choco1 = StringVar()
e_choco2 = StringVar()

e_white1 = StringVar()
e_white2 = StringVar()

e_milk1 = StringVar()
e_milk2 = StringVar()

e_thai1 = StringVar()
e_thai2 = StringVar()



# -----------------------------------------------------------------------------------------
# Coffee
espresso = Checkbutton(coffeeFrame,text='Espresso',font=('Bebas Neue',15),onvalue=1,offvalue=0,variable=var1,bg='gold',fg='black')
espresso.grid(row=0,column=0)

cappucino = Checkbutton(coffeeFrame,text='Cappucino',font=('Bebas Neue',15),onvalue=1,offvalue=0,variable=var2,bg='gold',fg='black')
cappucino.grid(row=1,column=0)

latte = Checkbutton(coffeeFrame,text='Latte',font=('Bebas Neue',15),onvalue=1,offvalue=0,variable=var3,bg='gold',fg='black')
latte.grid(row=2,column=0)

mocha = Checkbutton(coffeeFrame,text='Mocha',font=('Bebas Neue',15),onvalue=1,offvalue=0,variable=var4,bg='gold',fg='black')
mocha.grid(row=3,column=0)

americano = Checkbutton(coffeeFrame,text='Americano',font=('Bebas Neue',15),onvalue=1,offvalue=0,variable=var5,bg='gold',fg='black')
americano.grid(row=4,column=0)

macchiato = Checkbutton(coffeeFrame,text='Macchiato',font=('Bebas Neue',15),onvalue=1,offvalue=0,variable=var6,bg='gold',fg='black')
macchiato.grid(row=5,column=0)

# Entry Fields for Coffee Items
# Espresso
textespresso = Entry(coffeeFrame,font=('Bebas Neue',15),bd=2,width=5,state=DISABLED,textvariable= e_esp1)
textespresso.grid(row=0,column=1)
textespresso2 = Entry(coffeeFrame,font=('Bebas Neue',15),bd=2,width=5,state=DISABLED,textvariable= e_esp2)
textespresso2.grid(row=0,column=2)

# Cappucino
textcappucino = Entry(coffeeFrame,font=('Bebas Neue',15),bd=2,width=5,state=DISABLED,textvariable= e_cap1)
textcappucino.grid(row=1,column=1)
textcappucino2 = Entry(coffeeFrame,font=('Bebas Neue',15),bd=2,width=5,state=DISABLED,textvariable= e_cap2)
textcappucino2.grid(row=1,column=2)

# Latte
textlatte = Entry(coffeeFrame,font=('Bebas Neue',15),bd=2,width=5,state=DISABLED,textvariable= e_lat1)
textlatte.grid(row=2,column=1)
textlatte2 = Entry(coffeeFrame,font=('Bebas Neue',15),bd=2,width=5,state=DISABLED,textvariable= e_lat2)
textlatte2.grid(row=2,column=2)

# Mocha
textmocha = Entry(coffeeFrame,font=('Bebas Neue',15),bd=2,width=5,state=DISABLED,textvariable= e_moc1)
textmocha.grid(row=3,column=1)
textmocha2 = Entry(coffeeFrame,font=('Bebas Neue',15),bd=2,width=5,state=DISABLED,textvariable= e_moc2)
textmocha2.grid(row=3,column=2)

# Americano
textamericano = Entry(coffeeFrame,font=('Bebas Neue',15),bd=2,width=5,state=DISABLED,textvariable= e_ame1)
textamericano.grid(row=4,column=1)
textamericano2 = Entry(coffeeFrame,font=('Bebas Neue',15),bd=2,width=5,state=DISABLED,textvariable= e_ame2)
textamericano2.grid(row=4,column=2)

# Macchiato
textmacchiato = Entry(coffeeFrame,font=('Bebas Neue',15),bd=2,width=5,state=DISABLED,textvariable= e_mac1)
textmacchiato.grid(row=5,column=1)
textmacchiato2 = Entry(coffeeFrame,font=('Bebas Neue',15),bd=2,width=5,state=DISABLED,textvariable= e_mac2)
textmacchiato2.grid(row=5,column=2)

# -----------------------------------------------------------------------------------------
# Tea
greentea = Checkbutton(teaFrame,text='Green tea',font=('Bebas Neue',15),onvalue=1,offvalue=0,variable=var7,bg='black',fg='Red')
greentea.grid(row=0,column=0)

blacktea = Checkbutton(teaFrame,text='Black tea',font=('Bebas Neue',15),onvalue=1,offvalue=0,variable=var8,bg='black',fg='Red')
blacktea.grid(row=1,column=0)

chocolate = Checkbutton(teaFrame,text='Chocolate',font=('Bebas Neue',15),onvalue=1,offvalue=0,variable=var9,bg='black',fg='Red')
chocolate.grid(row=2,column=0)

whitechocolate = Checkbutton(teaFrame,text='White Chocolate',font=('Bebas Neue',15),onvalue=1,offvalue=0,variable=var10,bg='black',fg='Red')
whitechocolate.grid(row=3,column=0)

milk = Checkbutton(teaFrame,text='Milk',font=('Bebas Neue',15),onvalue=1,offvalue=0,variable=var11,bg='black',fg='Red')
milk.grid(row=4,column=0)

thaitea = Checkbutton(teaFrame,text='Thai Tea',font=('Bebas Neue',15),onvalue=1,offvalue=0,variable=var12,bg='black',fg='Red')
thaitea.grid(row=5,column=0)

# Entry Fields for Coffee Items
# Green Tea
textgreen = Entry(teaFrame,font=('Bebas Neue',15),bd=2,width=5,state=DISABLED,textvariable= e_green1)
textgreen.grid(row=0,column=1)
textgreen2 = Entry(teaFrame,font=('Bebas Neue',15),bd=2,width=5,state=DISABLED,textvariable= e_green2)
textgreen2.grid(row=0,column=2)

# Black Tea
textblack = Entry(teaFrame,font=('Bebas Neue',15),bd=2,width=5,state=DISABLED,textvariable= e_black1)
textblack.grid(row=1,column=1)
textblack2 = Entry(teaFrame,font=('Bebas Neue',15),bd=2,width=5,state=DISABLED,textvariable= e_black2)
textblack2.grid(row=1,column=2)

# Chocolate
textchoco = Entry(teaFrame,font=('Bebas Neue',15),bd=2,width=5,state=DISABLED,textvariable= e_choco1)
textchoco.grid(row=2,column=1)
textchoco2 = Entry(teaFrame,font=('Bebas Neue',15),bd=2,width=5,state=DISABLED,textvariable= e_choco2)
textchoco2.grid(row=2,column=2)

# White Chocolate
textwhite = Entry(teaFrame,font=('Bebas Neue',15),bd=2,width=5,state=DISABLED,textvariable= e_white1)
textwhite.grid(row=3,column=1)
textwhite2 = Entry(teaFrame,font=('Bebas Neue',15),bd=2,width=5,state=DISABLED,textvariable= e_white2)
textwhite2.grid(row=3,column=2)

# Milk
textmilk = Entry(teaFrame,font=('Bebas Neue',15),bd=2,width=5,state=DISABLED,textvariable= e_milk1)
textmilk.grid(row=4,column=1)
textmilk2 = Entry(teaFrame,font=('Bebas Neue',15),bd=2,width=5,state=DISABLED,textvariable= e_milk2)
textmilk2.grid(row=4,column=2)

# Thai Tea
textthai = Entry(teaFrame,font=('Bebas Neue',15),bd=2,width=5,state=DISABLED,textvariable= e_thai1)
textthai.grid(row=5,column=1)
textthai2 = Entry(teaFrame,font=('Bebas Neue',15),bd=2,width=5,state=DISABLED,textvariable= e_thai2)
textthai2.grid(row=5,column=2)

# -----------------------------------------------------------------------------------------
root.mainloop()