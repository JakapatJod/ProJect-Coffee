from tkinter import *
# Functions Coffee

def Espresso():
    if var1.get()==1:
        textespresso.config(state=NORMAL)
        textespresso.delete(0,END)
        textespresso.focus()
    else:
        textespresso.config(state=DISABLED)
        e_esp1.set('0')
    
    if var1.get()==1:
        textespresso2.config(state=NORMAL)
        textespresso2.delete(0,END)
        textespresso2.focus()
    else:
        textespresso2.config(state=DISABLED)
        e_esp2.set('0')

def Cappucino():
    if var2.get()==1:
        textcappucino.config(state=NORMAL)
        textcappucino.delete(0,END)
        textcappucino.focus()
    else:
        textcappucino.config(state=DISABLED)
        e_cap1.set('0')
    
    if var2.get()==1:
        textcappucino.config(state=NORMAL)
        textcappucino2.delete(0,END)
        textcappucino2.focus()
    else:
        textcappucino2.config(state=DISABLED)
        e_cap2.set('0')
    
root = Tk()

root.geometry('1280x780+0+0')

root.resizable(0,0)

root.title('Menu Coffee System')
root.config(bg='black') # สี bg

topFrame = Frame(root,bd=10,relief=RIDGE,bg='dark orange',pady=10)
topFrame.pack(side=TOP)

LabelTitle = Label(topFrame,text='Coffee Menu',font=('Bebas',50,'bold'),fg='black',width=43)
LabelTitle.grid(row=0,column=0)

# frames
menuFrame = Frame(root,bd=10,relief=RIDGE,bg='dark orange')
menuFrame.pack(side=LEFT)

costFrame = Frame(menuFrame,bd=4,relief=RIDGE,bg='dark orange')
costFrame.pack(side=BOTTOM)

coffeeFrame = LabelFrame(menuFrame,text='Coffee\tHOT  COLD',font=('Bebas Neue',20,'bold'),bd=10,relief=RIDGE,bg='gold',fg='black')
coffeeFrame.pack(side=LEFT)

teaFrame = LabelFrame(menuFrame,text='Tea\t        HOT  COLD',font=('Bebas Neue',20,'bold'),bd=10,relief=RIDGE,bg='black',fg='Red')
teaFrame.pack(side=LEFT)

dessertFrame = LabelFrame(menuFrame,text='Dessert',font=('Bebas Neue',20,'bold'),bd=10,relief=RIDGE,bg='sandy brown',fg='black',padx=8)
dessertFrame.pack(side=LEFT)

rightFrame = Frame(root,bd=15,relief=RIDGE)
rightFrame.pack(side=RIGHT)

calculatorFrame = Frame(rightFrame,bd=1,relief=RIDGE)
calculatorFrame.pack()

recieptFrame = Frame(rightFrame,bd=4,relief=RIDGE)
recieptFrame.pack()

buttonFrame = Frame(rightFrame,bd=3,relief=RIDGE)
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

# Varriable Dessert
e_cup = StringVar()
e_donut = StringVar()
e_chee = StringVar()
e_pud = StringVar()
e_waf = StringVar()
e_cake = StringVar()

# Set 0 Coffee
e_esp1.set('0')
e_esp2.set('0')

e_cap1.set('0')
e_cap2.set('0')

e_lat1.set('0')
e_lat2.set('0')

e_moc1.set('0')
e_moc2.set('0')

e_ame1.set('0')
e_ame2.set('0')

e_mac1.set('0')
e_mac2.set('0')

# Set 0 Tea
e_green1.set('0')
e_green2.set('0')

e_black1.set('0')
e_black2.set('0')

e_choco1.set('0')
e_choco2.set('0')

e_white1.set('0')
e_white2.set('0')

e_milk1.set('0')
e_milk2.set('0')

e_thai1.set('0')
e_thai2.set('0')

# Set 0 Dessert

e_cup.set('0')
e_donut.set('0')
e_chee.set('0')
e_pud.set('0')
e_waf.set('0')
e_cake.set('0')

# Varriable Cost
costofcoffeevar = StringVar()
costofteavar = StringVar()
costofdessertvar = StringVar()
subtotalvar = StringVar()
servicetaxvar = StringVar()
totalcostvar = StringVar()

# -----------------------------------------------------------------------------------------
# Coffee
espresso = Checkbutton(coffeeFrame,text='Espresso',font=('Bebas Neue',20),onvalue=1,offvalue=0,variable=var1,bg='gold',fg='black'
            ,command=Espresso)
espresso.grid(row=0,column=0)

cappucino = Checkbutton(coffeeFrame,text='Cappucino',font=('Bebas Neue',20),onvalue=1,offvalue=0,variable=var2,bg='gold',fg='black'
            ,command=Cappucino)
cappucino.grid(row=1,column=0)

latte = Checkbutton(coffeeFrame,text='Latte',font=('Bebas Neue',20),onvalue=1,offvalue=0,variable=var3,bg='gold',fg='black')
latte.grid(row=2,column=0)

mocha = Checkbutton(coffeeFrame,text='Mocha',font=('Bebas Neue',20),onvalue=1,offvalue=0,variable=var4,bg='gold',fg='black')
mocha.grid(row=3,column=0)

americano = Checkbutton(coffeeFrame,text='Americano',font=('Bebas Neue',20),onvalue=1,offvalue=0,variable=var5,bg='gold',fg='black')
americano.grid(row=4,column=0)

macchiato = Checkbutton(coffeeFrame,text='Macchiato',font=('Bebas Neue',20),onvalue=1,offvalue=0,variable=var6,bg='gold',fg='black')
macchiato.grid(row=5,column=0)

# Entry Fields for Coffee Items
# Espresso
textespresso = Entry(coffeeFrame,font=('Bebas Neue',20),bd=2,width=5,state=DISABLED,textvariable= e_esp1)
textespresso.grid(row=0,column=1)
textespresso2 = Entry(coffeeFrame,font=('Bebas Neue',20),bd=2,width=5,state=DISABLED,textvariable= e_esp2)
textespresso2.grid(row=0,column=2)

# Cappucino
textcappucino = Entry(coffeeFrame,font=('Bebas Neue',20),bd=2,width=5,state=DISABLED,textvariable= e_cap1)
textcappucino.grid(row=1,column=1)
textcappucino2 = Entry(coffeeFrame,font=('Bebas Neue',20),bd=2,width=5,state=DISABLED,textvariable= e_cap2)
textcappucino2.grid(row=1,column=2)

# Latte
textlatte = Entry(coffeeFrame,font=('Bebas Neue',20),bd=2,width=5,state=DISABLED,textvariable= e_lat1)
textlatte.grid(row=2,column=1)
textlatte2 = Entry(coffeeFrame,font=('Bebas Neue',20),bd=2,width=5,state=DISABLED,textvariable= e_lat2)
textlatte2.grid(row=2,column=2)

# Mocha
textmocha = Entry(coffeeFrame,font=('Bebas Neue',20),bd=2,width=5,state=DISABLED,textvariable= e_moc1)
textmocha.grid(row=3,column=1)
textmocha2 = Entry(coffeeFrame,font=('Bebas Neue',20),bd=2,width=5,state=DISABLED,textvariable= e_moc2)
textmocha2.grid(row=3,column=2)

# Americano
textamericano = Entry(coffeeFrame,font=('Bebas Neue',20),bd=2,width=5,state=DISABLED,textvariable= e_ame1)
textamericano.grid(row=4,column=1)
textamericano2 = Entry(coffeeFrame,font=('Bebas Neue',20),bd=2,width=5,state=DISABLED,textvariable= e_ame2)
textamericano2.grid(row=4,column=2)

# Macchiato
textmacchiato = Entry(coffeeFrame,font=('Bebas Neue',20),bd=2,width=5,state=DISABLED,textvariable= e_mac1)
textmacchiato.grid(row=5,column=1)
textmacchiato2 = Entry(coffeeFrame,font=('Bebas Neue',20),bd=2,width=5,state=DISABLED,textvariable= e_mac2)
textmacchiato2.grid(row=5,column=2)

# -----------------------------------------------------------------------------------------
# Tea
greentea = Checkbutton(teaFrame,text='Green tea',font=('Bebas Neue',20),onvalue=1,offvalue=0,variable=var7,bg='black',fg='Red')
greentea.grid(row=0,column=0)

blacktea = Checkbutton(teaFrame,text='Black tea',font=('Bebas Neue',20),onvalue=1,offvalue=0,variable=var8,bg='black',fg='Red')
blacktea.grid(row=1,column=0)

chocolate = Checkbutton(teaFrame,text='Chocolate',font=('Bebas Neue',20),onvalue=1,offvalue=0,variable=var9,bg='black',fg='Red')
chocolate.grid(row=2,column=0)

whitechocolate = Checkbutton(teaFrame,text='White Chocolate',font=('Bebas Neue',20),onvalue=1,offvalue=0,variable=var10,bg='black',fg='Red')
whitechocolate.grid(row=3,column=0)

milk = Checkbutton(teaFrame,text='Milk',font=('Bebas Neue',20),onvalue=1,offvalue=0,variable=var11,bg='black',fg='Red')
milk.grid(row=4,column=0)

thaitea = Checkbutton(teaFrame,text='Thai Tea',font=('Bebas Neue',20),onvalue=1,offvalue=0,variable=var12,bg='black',fg='Red')
thaitea.grid(row=5,column=0)

# Entry Fields for Coffee Items
# Green Tea
textgreen = Entry(teaFrame,font=('Bebas Neue',20),bd=2,width=5,state=DISABLED,textvariable= e_green1)
textgreen.grid(row=0,column=1)
textgreen2 = Entry(teaFrame,font=('Bebas Neue',20),bd=2,width=5,state=DISABLED,textvariable= e_green2)
textgreen2.grid(row=0,column=2)

# Black Tea
textblack = Entry(teaFrame,font=('Bebas Neue',20),bd=2,width=5,state=DISABLED,textvariable= e_black1)
textblack.grid(row=1,column=1)
textblack2 = Entry(teaFrame,font=('Bebas Neue',20),bd=2,width=5,state=DISABLED,textvariable= e_black2)
textblack2.grid(row=1,column=2)

# Chocolate
textchoco = Entry(teaFrame,font=('Bebas Neue',20),bd=2,width=5,state=DISABLED,textvariable= e_choco1)
textchoco.grid(row=2,column=1)
textchoco2 = Entry(teaFrame,font=('Bebas Neue',20),bd=2,width=5,state=DISABLED,textvariable= e_choco2)
textchoco2.grid(row=2,column=2)

# White Chocolate
textwhite = Entry(teaFrame,font=('Bebas Neue',20),bd=2,width=5,state=DISABLED,textvariable= e_white1)
textwhite.grid(row=3,column=1)
textwhite2 = Entry(teaFrame,font=('Bebas Neue',20),bd=2,width=5,state=DISABLED,textvariable= e_white2)
textwhite2.grid(row=3,column=2)

# Milk
textmilk = Entry(teaFrame,font=('Bebas Neue',20),bd=2,width=5,state=DISABLED,textvariable= e_milk1)
textmilk.grid(row=4,column=1)
textmilk2 = Entry(teaFrame,font=('Bebas Neue',20),bd=2,width=5,state=DISABLED,textvariable= e_milk2)
textmilk2.grid(row=4,column=2)

# Thai Tea
textthai = Entry(teaFrame,font=('Bebas Neue',20),bd=2,width=5,state=DISABLED,textvariable= e_thai1)
textthai.grid(row=5,column=1)
textthai2 = Entry(teaFrame,font=('Bebas Neue',20),bd=2,width=5,state=DISABLED,textvariable= e_thai2)
textthai2.grid(row=5,column=2)

# -----------------------------------------------------------------------------------------
# Dessert
cupcake = Checkbutton(dessertFrame,text='Cupcake',font=('Bebas Neue',20),onvalue=1,offvalue=0,variable=var13,bg='sandy brown',fg='black')
cupcake.grid(row=0,column=0)

dounut = Checkbutton(dessertFrame,text='Dounut',font=('Bebas Neue',20),onvalue=1,offvalue=0,variable=var14,bg='sandy brown',fg='black')
dounut.grid(row=1,column=0)

cheesecake = Checkbutton(dessertFrame,text='Cheesecake',font=('Bebas Neue',20),onvalue=1,offvalue=0,variable=var15,bg='sandy brown',fg='black')
cheesecake.grid(row=2,column=0)

pudding = Checkbutton(dessertFrame,text='Pudding',font=('Bebas Neue',20),onvalue=1,offvalue=0,variable=var16,bg='sandy brown',fg='black')
pudding.grid(row=3,column=0)

waffle = Checkbutton(dessertFrame,text='Waffle',font=('Bebas Neue',20),onvalue=1,offvalue=0,variable=var17,bg='sandy brown',fg='black')
waffle.grid(row=4,column=0)

cake = Checkbutton(dessertFrame,text='Cake',font=('Bebas Neue',20),onvalue=1,offvalue=0,variable=var18,bg='sandy brown',fg='black')
cake.grid(row=5,column=0)

# Entry Fields for Coffee Items
# Cupcake
textcupcake = Entry(dessertFrame,font=('Bebas Neue',20),bd=2,width=5,state=DISABLED,textvariable= e_cup)
textcupcake.grid(row=0,column=1)

# Donut
textdonut = Entry(dessertFrame,font=('Bebas Neue',20),bd=2,width=5,state=DISABLED,textvariable= e_donut)
textdonut.grid(row=1,column=1)

# Cheese cake
textcheesecake = Entry(dessertFrame,font=('Bebas Neue',20),bd=2,width=5,state=DISABLED,textvariable= e_chee)
textcheesecake.grid(row=2,column=1)

# Pudding
textpudding = Entry(dessertFrame,font=('Bebas Neue',20),bd=2,width=5,state=DISABLED,textvariable= e_pud)
textpudding.grid(row=3,column=1)

# Waffle
textwaffle = Entry(dessertFrame,font=('Bebas Neue',20),bd=2,width=5,state=DISABLED,textvariable= e_waf)
textwaffle.grid(row=4,column=1)

# Cake
textcake = Entry(dessertFrame,font=('Bebas Neue',20),bd=2,width=5,state=DISABLED,textvariable= e_cake)
textcake.grid(row=5,column=1)

# -----------------------------------------------------------------------------------------
# Costlabels total
labelCostofCoffee = Label(costFrame,text='Cost of coffee',font=('Bebas Neue',20),bg='dark orange',fg='black')
labelCostofCoffee.grid(row=0,column=0)
textCostofCoffee = Entry(costFrame,font=('Bebas Neue',20),bd=6,width=14,state='readonly',textvariable=costofcoffeevar)
textCostofCoffee.grid(row=0,column=1,padx=54)

labelCostofTea = Label(costFrame,text='Cost of Tea',font=('Bebas Neue',20),bg='dark orange',fg='black')
labelCostofTea.grid(row=1,column=0)
textCostofTea = Entry(costFrame,font=('Bebas Neue',20),bd=6,width=14,state='readonly',textvariable=costofteavar)
textCostofTea.grid(row=1,column=1,padx=54)

labelCostofDessert = Label(costFrame,text='Cost of Dessert',font=('Bebas Neue',20),bg='dark orange',fg='black')
labelCostofDessert.grid(row=2,column=0)
textCostofDessert = Entry(costFrame,font=('Bebas Neue',20),bd=6,width=14,state='readonly',textvariable=costofdessertvar)
textCostofDessert.grid(row=2,column=1,padx=54)

labelSubtotal = Label(costFrame,text='Sub Total',font=('Bebas Neue',20),bg='dark orange',fg='black')
labelSubtotal.grid(row=0,column=2)
textSubtotal = Entry(costFrame,font=('Bebas Neue',20),bd=6,width=14,state='readonly',textvariable=subtotalvar)
textSubtotal.grid(row=0,column=3,padx=54)

labelServiceTax = Label(costFrame,text='Service Tax',font=('Bebas Neue',20),bg='dark orange',fg='black')
labelServiceTax.grid(row=1,column=2)
textServiceTax = Entry(costFrame,font=('Bebas Neue',20),bd=6,width=14,state='readonly',textvariable=servicetaxvar)
textServiceTax.grid(row=1,column=3,padx=54)

labelTotalcost = Label(costFrame,text='Total Cost',font=('Bebas Neue',20),bg='dark orange',fg='black')
labelTotalcost.grid(row=2,column=2)
textTotalcost = Entry(costFrame,font=('Bebas Neue',20),bd=6,width=14,state='readonly',textvariable=totalcostvar)
textTotalcost.grid(row=2,column=3 ,padx=54)

# -----------------------------------------------------------------------------------------
# Button

buttonTotal = Button(buttonFrame,text='Total',font=('Bebas Neue',15,'bold'),bg='dark orange',fg='black',bd=2,padx=5)
buttonTotal.grid(row=0,column=0)

buttonRecipt = Button(buttonFrame,text='Receipt',font=('Bebas Neue',15,'bold'),bg='dark orange',fg='black',bd=2,padx=5)
buttonRecipt.grid(row=0,column=1)

buttonSave = Button(buttonFrame,text='Save',font=('Bebas Neue',15,'bold'),bg='dark orange',fg='black',bd=2,padx=5)
buttonSave.grid(row=0,column=2)

buttonSend = Button(buttonFrame,text='Send',font=('Bebas Neue',15,'bold'),bg='dark orange',fg='black',bd=2,padx=5)
buttonSend.grid(row=0,column=3)

buttonReset = Button(buttonFrame,text='Reset',font=('Bebas Neue',15,'bold'),bg='dark orange',fg='black',bd=2,padx=5)
buttonReset.grid(row=0,column=4)

buttonLogout = Button(buttonFrame,text='Logout',font=('Bebas Neue',15,'bold'),bg='dark orange',fg='black',bd=2,padx=5)
buttonLogout.grid(row=0,column=5)

# -----------------------------------------------------------------------------------------
# Text area receipt
textReceipt = Text(recieptFrame,font=('Bebas Neue',18),bd=3,width=42,height=10)
textReceipt.grid(row=0,column=0)

# -----------------------------------------------------------------------------------------
# Calculator
operator = ''
def buttonClick(numbers):
    global operator
    operator = operator + numbers
    calculatorField.delete(0,END)
    calculatorField.insert(END,operator)

def clear():
    global operator
    operator = ''
    calculatorField.delete(0,END)

def answer():
    global operator
    result = str(eval(operator))
    calculatorField.delete(0,END)
    calculatorField.insert(0,result)
    operator = ''


calculatorField = Entry(calculatorFrame,font=('Bebas Neue',15),width=32,bd=4)
calculatorField.grid(row=0,column=0,columnspan=4)

button7 = Button(calculatorFrame,text='7',font=('Bebas Neue',15),fg='black',bg='dark orange',bd=6,width=6
            ,command=lambda:buttonClick('7'))
button7.grid(row=1,column=0)

button8 = Button(calculatorFrame,text='8',font=('Bebas Neue',15),fg='black',bg='dark orange',bd=6,width=6
            ,command=lambda:buttonClick('8'))
button8.grid(row=1,column=1)

button9 = Button(calculatorFrame,text='9',font=('Bebas Neue',15),fg='black',bg='dark orange',bd=6,width=6
            ,command=lambda:buttonClick('9'))
button9.grid(row=1,column=2)

buttonPlus = Button(calculatorFrame,text='+',font=('Bebas Neue',15),fg='black',bg='dark orange',bd=6,width=6
            ,command=lambda:buttonClick('+'))
buttonPlus.grid(row=1,column=3)

button4 = Button(calculatorFrame,text='4',font=('Bebas Neue',15),fg='black',bg='dark orange',bd=6,width=6
            ,command=lambda:buttonClick('4'))
button4.grid(row=2,column=0)

button5 = Button(calculatorFrame,text='5',font=('Bebas Neue',15),fg='black',bg='dark orange',bd=6,width=6
            ,command=lambda:buttonClick('5'))
button5.grid(row=2,column=1)

button6 = Button(calculatorFrame,text='6',font=('Bebas Neue',15),fg='black',bg='dark orange',bd=6,width=6
            ,command=lambda:buttonClick('6'))
button6.grid(row=2,column=2)

buttonMinus = Button(calculatorFrame,text='-',font=('Bebas Neue',15),fg='black',bg='dark orange',bd=6,width=6
            ,command=lambda:buttonClick('-'))
buttonMinus.grid(row=2,column=3)

button1 = Button(calculatorFrame,text='1',font=('Bebas Neue',15),fg='black',bg='dark orange',bd=6,width=6
            ,command=lambda:buttonClick('1'))
button1.grid(row=3,column=0)

button2 = Button(calculatorFrame,text='2',font=('Bebas Neue',15),fg='black',bg='dark orange',bd=6,width=6
            ,command=lambda:buttonClick('2'))
button2.grid(row=3,column=1)

button3 = Button(calculatorFrame,text='3',font=('Bebas Neue',15),fg='black',bg='dark orange',bd=6,width=6
            ,command=lambda:buttonClick('3'))
button3.grid(row=3,column=2)

buttonMult = Button(calculatorFrame,text='*',font=('Bebas Neue',15),fg='black',bg='dark orange',bd=6,width=6
            ,command=lambda:buttonClick('*'))
buttonMult.grid(row=3,column=3)

buttonAns = Button(calculatorFrame,text='Ans',font=('Bebas Neue',15),fg='black',bg='dark orange',bd=6,width=6
            ,command=answer)
buttonAns.grid(row=4,column=0)

buttonClear = Button(calculatorFrame,text='Clear',font=('Bebas Neue',15),fg='black',bg='dark orange',bd=6,width=6
            ,command=clear)
buttonClear.grid(row=4,column=1)

button0 = Button(calculatorFrame,text='0',font=('Bebas Neue',15),fg='black',bg='dark orange',bd=6,width=6
            ,command=lambda:buttonClick('0'))
button0.grid(row=4,column=2)

buttonDive = Button(calculatorFrame,text='/',font=('Bebas Neue',15),fg='black',bg='dark orange',bd=6,width=6
            ,command=lambda:buttonClick('/'))
buttonDive.grid(row=4,column=3)

root.mainloop() 