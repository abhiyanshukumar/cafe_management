from tkinter import *
import random
import time;
import datetime
import tkinter.messagebox as tmsg
cafe=Tk()
cafe.geometry("1300x700")
cafe.title("Restaurant management system")

#============== frames ==============================================

f1 = Frame(cafe, width=1250, height=50, bd=6,bg='#b85b56', relief='raised')
f1.pack(side=TOP)
f2 = Frame(cafe, width=500, height=600, bd=8,bg='#b85b56', relief='raised')
f2.pack(side=LEFT)
f3 = Frame(cafe, width=700, height=600, bd=8,bg='#b85b56', relief='raised')
f3.pack(side=RIGHT)

#================= Sub frame of f2 ============================================

f2a = Frame(f2, width=500, height=350, bd=8,bg="#b85b56", relief='raised')
f2a.pack(side=TOP)
f2b = Frame(f2, width=500, height=200, bd=8,bg="#b85b56", relief='raised')
f2b.pack(side=BOTTOM)

#========================sub frame of f2a =============================================

f2aa = Frame(f2a, width=250, height=350, bd=8,bg="#b85b56", relief='raised')
f2aa.pack(side=LEFT)
f2ab = Frame(f2a, width=250, height=350, bd=8,bg="#b85b56", relief='raised')
f2ab.pack(side=LEFT)

#========================sub frame of f2b =============================================

f2ba = Frame(f2b, width=450, height=200, bd=8, relief='raised',bg="#b85b56")
f2ba.pack(side=LEFT)
f2bb = Frame(f2b, width=450, height=200, bd=8, relief='raised',bg="#b85b56")
f2bb.pack(side=LEFT)


#====================sub frame of f3=================================

f3b = Frame(f3, width=400, height=50, bd=8, relief='raised')
f3b.pack(side=BOTTOM)
f3a = Frame(f3, width=400, height=50, bd=8, relief='raised')
f3a.pack(side=BOTTOM)
f3c = Frame(f3, width=550, height=400, bd=8, relief='raised')
f3c.pack(side=BOTTOM)


#==========Label of f1 ==============================================

lf1 = Label(f1, font='arial 40 bold', text="\tCAFE MANAGEMENT SYSTEM\t", bd=10)
lf1.grid(row=0, column=0)


#-----------------  CALCULATOR CLICK ------------------------------------------------

def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(screen.get())

        scvalue.set(value)

    elif text == "C":
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

#----------------------------------------------------------------------------------------

#============= start filling in f2a ======================================================

def qexit():
    qexit=tmsg.askyesno("Quit System", "Do you want to quit?")
    if qexit>0:
        cafe.destroy()
        return

def creset():
    eae1.set("0")
    eae2.set("0")
    eae3.set("0")
    eae4.set("0")
    eae5.set("0")
    eae6.set("0")
    eae7.set("0")
    eae8.set("0")

    eae9.set("0")
    eae10.set("0")
    eae11.set("0")
    eae12.set("0")
    eae13.set("0")
    eae14.set("0")
    eae15.set("0")
    eae16.set("0")

    var1.set("0")
    var2.set("0")
    var3.set("0")
    var4.set("0")
    var5.set("0")
    var6.set("0")
    var7.set("0")
    var8.set("0")

    var9.set("0")
    var10.set("0")
    var11.set("0")
    var12.set("0")
    var13.set("0")
    var14.set("0")
    var15.set("0")
    var16.set("0")


    ea1.configure(state=DISABLED)
    ea2.configure(state=DISABLED)
    ea3.configure(state=DISABLED)
    ea4.configure(state=DISABLED)
    ea5.configure(state=DISABLED)
    ea6.configure(state=DISABLED)
    ea7.configure(state=DISABLED)
    ea8.configure(state=DISABLED)
    ea9.configure(state=DISABLED)
    ea10.configure(state=DISABLED)
    ea11.configure(state=DISABLED)
    ea12.configure(state=DISABLED)
    ea13.configure(state=DISABLED)
    ea14.configure(state=DISABLED)
    ea15.configure(state=DISABLED)
    ea16.configure(state=DISABLED)
    PaidTax.set("")
    SubTotal.set("")
    TotalCost.set("")
    CostOfStarter.set("")
    CostOfMainDish.set("")
    treceipt.delete("1.0", END)
#====================================================================================================================================

def checkbuttonvalue():
	if(var1.get()==1):
		ea1.configure(state=NORMAL)
	elif(var1.get()==0):
		ea1.configure(state=DISABLED)
		eae1.set("0")

	if(var2.get()==1):
		ea2.configure(state=NORMAL)
	elif(var2.get()==0):
		ea2.configure(state=DISABLED)
		eae2.set("0")

	if(var3.get()==1):
		ea3.configure(state=NORMAL)
	elif(var3.get()==0):
		ea3.configure(state=DISABLED)
		eae3.set("0")

	if(var4.get()==1):
		ea4.configure(state=NORMAL)
	elif(var4.get()==0):
		ea4.configure(state=DISABLED)
		eae4.set("0")

	if(var5.get()==1):
		ea5.configure(state=NORMAL)
	elif(var5.get()==0):
		ea5.configure(state=DISABLED)
		eae5.set("0")

	if(var6.get()==1):
		ea6.configure(state=NORMAL)
	elif(var6.get()==0):
		ea6.configure(state=DISABLED)
		eae6.set("0")

	if(var7.get()==1):
		ea7.configure(state=NORMAL)
	elif(var7.get()==0):
		ea7.configure(state=DISABLED)
		eae7.set("0")

	if(var8.get()==1):
		ea8.configure(state=NORMAL)
	elif(var8.get()==0):
		ea8.configure(state=DISABLED)
		eae8.set("0")

	if(var9.get()==1):
		ea9.configure(state=NORMAL)
	elif(var9.get()==0):
		ea9.configure(state=DISABLED)
		eae9.set("0")

	if(var10.get()==1):
		ea10.configure(state=NORMAL)
	elif(var10.get()==0):
		ea10.configure(state=DISABLED)
		eae10.set("0")

	if(var11.get()==1):
		ea11.configure(state=NORMAL)
	elif(var11.get()==0):
		ea11.configure(state=DISABLED)
		eae11.set("0")

	if(var12.get()==1):
		ea12.configure(state=NORMAL)
	elif(var12.get()==0):
		ea12.configure(state=DISABLED)
		eae12.set("0")

	if(var13.get()==1):
		ea13.configure(state=NORMAL)
	elif(var13.get()==0):
		ea13.configure(state=DISABLED)
		eae13.set("0")

	if(var14.get()==1):
		ea14.configure(state=NORMAL)
	elif(var14.get()==0):
		ea14.configure(state=DISABLED)
		eae14.set("0")

	if(var15.get()==1):
		ea15.configure(state=NORMAL)
	elif(var15.get()==0):
		ea15.configure(state=DISABLED)
		eae15.set("0")

	if(var16.get()==1):
		ea16.configure(state=NORMAL)
	elif(var16.get()==0):
		ea16.configure(state=DISABLED)
		eae16.set("0")


#================================================cost of item======================================================================

def CostofItem():
	item1 = float(eae1.get())
	item2 = float(eae2.get())
	item3 = float(eae3.get())
	item4 = float(eae4.get())
	item5 = float(eae5.get())
	item6 = float(eae6.get())
	item7 = float(eae7.get())
	item8 = float(eae8.get())

	item9 = float(eae9.get())
	item10 = float(eae10.get())
	item11 = float(eae11.get())
	item12 = float(eae12.get())
	item13 = float(eae13.get())
	item14 = float(eae14.get())
	item15 = float(eae15.get())
	item16 = float(eae16.get())



	PriceOfStarter = (item1*100)+(item2*110)+(item3*120)+(item4*130)+(item5*140)+(item6*150)+(item7*160)+(item8*170)
	PriceOfMainDish = (item9*120)+(item10*130)+(item11*140)+(item12*150)+(item13*160)+(item14*170)+(item15*180)+(item16*180)

	StartersPrice= "Rs.", str('%.2f'%(PriceOfStarter))
	MainDishPrice= "Rs.", str('%.2f'%(PriceOfMainDish))


	
	PriceOfSubtotal =  "Rs.", str('%.2f'%(PriceOfStarter + PriceOfMainDish+1.59))
	PriceOfTax = "Rs.", str('%.2f'%(0.14*(PriceOfStarter + PriceOfMainDish)))
	PriceOfTotal = "Rs.", str('%.2f'%((PriceOfStarter + PriceOfMainDish) + (0.14*(PriceOfStarter + PriceOfMainDish)) ))
	# PriceOfServicecharge = "Rs. ", str('%.2f'%(1.59))
	
	CostOfDrink.set(StartersPrice)
	CostOfDesert.set(MainDishPrice)

	service_charge.set("Rs. 1.59")
	PaidTax.set(PriceOfTax)
	SubTotal.set(PriceOfSubtotal)
	TotalCost.set(PriceOfTotal)

#--------------------- Receipt ------------------------------------------------------------------------------------------------------------------------

def Receipt():
	treceipt.delete("1.0",END)
	x=random.randint(10850,500230)
	randomref=str(x)
	Receipt_Ref.set("BILL"+randomref)

	treceipt.insert(END,'Receipt Ref:\t\t\t'+Receipt_Ref.get()+'\t\t'+DateOfOrder.get()+"\n")
	treceipt.insert(END,'Items\t\t\t\t\t'+"No. of Items \n\n")
	treceipt.insert(END,'Virgin Mojito:\t\t\t\t\t'+ eae1.get()+"\n")
	treceipt.insert(END,'Oreo Shake:\t\t\t\t\t'+ eae2.get()+"\n")
	treceipt.insert(END,'Lemonade:\t\t\t\t\t'+ eae3.get()+"\n")
	treceipt.insert(END,'Crunchy Frappa:\t\t\t\t\t'+ eae4.get()+"\n")
	treceipt.insert(END,'Blueberry Delight:\t\t\t\t\t'+ eae5.get()+"\n")
	treceipt.insert(END,'Black Coffee:\t\t\t\t\t'+ eae6.get()+"\n")
	treceipt.insert(END,'Red-Bull:\t\t\t\t\t'+ eae7.get()+"\n")
	treceipt.insert(END,'Hot-Tea:\t\t\t\t\t'+ eae8.get()+"\n")
	treceipt.insert(END,'Chocolate Cheesecake:\t\t\t\t\t'+ eae9.get()+"\n")
	treceipt.insert(END,'Sticky Toffee Pudding:\t\t\t\t\t'+ eae10.get()+"\n")
	treceipt.insert(END,'Fried Ice Cream:\t\t\t\t\t'+ eae11.get()+"\n")
	treceipt.insert(END,'Banana Boat Pie:\t\t\t\t\t'+ eae12.get()+"\n")
	treceipt.insert(END,'Strawberry Pudding:\t\t\t\t\t'+ eae13.get()+"\n")
	treceipt.insert(END,'Rum Cake:\t\t\t\t\t'+ eae14.get()+"\n")
	treceipt.insert(END,'Nutella Cheesecake:\t\t\t\t\t'+ eae15.get()+"\n")
	treceipt.insert(END,'Brownie Gelato:\t\t\t\t\t'+ eae16.get()+"\n")
	treceipt.insert(END,'=======================PRICE=====================\t\t\t\t'+"\n")
	treceipt.insert(END,'Cost Of Drinks:\t\t\t\t'+CostOfDrink.get()+"\n")
	treceipt.insert(END,'Cost Of Deserts:\t\t\t\t'+CostOfDesert.get()+"\n")
	treceipt.insert(END,'Service Charge:\t\t\t\t'+service_charge.get()+"\n")
	treceipt.insert(END,'Tax Paid:\t\t\t\t'+PaidTax.get()+"\n")
	treceipt.insert(END,'Total Cost:\t\t\t\t'+TotalCost.get()+"\n")

	text_area=treceipt.get('1.0','end-1c')

	file_name=Receipt_Ref.get()
	save_file=open(file_name,'w')
	save_file.write(text_area)
	save_file.close()

#------------------------------------------------------------------------------------------


scvalue = StringVar()
scvalue.set("")
screen = Entry(f3, textvar=scvalue, bg="#9cfff0", font="lucida 20")
screen.pack(side=TOP, fill=X, ipadx=8, pady=5)

#=================BUTTON============================================================
f3ca = Frame(f3c)
b1 = Button(f3ca, text="7", padx=45, bg="#b85b56", font="lucida 10 bold")
b1.bind("<Button-1>", click)
b1.pack(side=LEFT, anchor="nw")

b2 = Button(f3ca, text="8", padx=45, bg="#b85b56", font="lucida 10 bold")
b2.bind("<Button-1>", click)
b2.pack(side=LEFT, anchor="nw")

b3 = Button(f3ca, text="9", padx=45, bg="#b85b56", font="lucida 10 bold")
b3.bind("<Button-1>", click)
b3.pack(side=LEFT, anchor="nw")

b4 = Button(f3ca, text="+", padx=45, bg="#b85b56", font="lucida 10 bold")
b4.bind("<Button-1>", click)
b4.pack(side=LEFT, anchor="nw")
f3ca.pack(side=TOP)

f3cb = Frame(f3c)
b5 = Button(f3cb, text="4", padx=45, bg="#b85b56", font="lucida 10 bold")
b5.bind("<Button-1>", click)
b5.pack(side=LEFT, anchor="nw")

b6 = Button(f3cb, text="5", padx=45, bg="#b85b56", font="lucida 10 bold")
b6.bind("<Button-1>", click)
b6.pack(side=LEFT, anchor="nw")

b7 = Button(f3cb, text="6", padx=45, bg="#b85b56", font="lucida 10 bold")
b7.bind("<Button-1>", click)
b7.pack(side=LEFT, anchor="nw")

b8 = Button(f3cb, text="-", padx=45, bg="#b85b56", font="lucida 10 bold")
b8.bind("<Button-1>", click)
b8.pack(side=LEFT, anchor="nw")
f3cb.pack(side=TOP)

f3cc = Frame(f3c)
b9 = Button(f3cc, text="1", padx=45, bg="#b85b56", font="lucida 10 bold")
b9.bind("<Button-1>", click)
b9.pack(side=LEFT, anchor="nw")

b10 = Button(f3cc, text="2", padx=45, bg="#b85b56", font="lucida 10 bold")
b10.bind("<Button-1>", click)
b10.pack(side=LEFT, anchor="nw")
b11 = Button(f3cc, text="3", padx=45, bg="#b85b56", font="lucida 10 bold")
b11.bind("<Button-1>", click)
b11.pack(side=LEFT, anchor="nw")

b12 = Button(f3cc, text="*", padx=45, bg="#b85b56", font="lucida 10 bold")
b12.bind("<Button-1>", click)
b12.pack(side=LEFT, anchor="nw")
f3cc.pack()

f3cd = Frame(f3c)
b13 = Button(f3cd, text="0", padx=45, bg="#b85b56", font="lucida 10 bold")
b13.bind("<Button-1>", click)
b13.pack(side=LEFT, anchor="nw")

b14 = Button(f3cd, text="C", padx=45, bg="#b85b56", font="lucida 10 bold")
b14.bind("<Button-1>", click)
b14.pack(side=LEFT, anchor="nw")

b15 = Button(f3cd, text="=", padx=45, bg="#b85b56", font="lucida 10 bold")
b15.bind("<Button-1>", click)
b15.pack(side=LEFT, anchor="nw")

b16 = Button(f3cd, text="/", padx=45, bg="#b85b56", font="lucida 10 bold")
b16.bind("<Button-1>", click)
b16.pack(side=LEFT, anchor="nw")
f3cd.pack()

#====================================================================================================================================

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


DateOfOrder=StringVar()
Receipt_Ref=StringVar()
PaidTax=StringVar()
SubTotal=StringVar()
TotalCost=StringVar()
CostOfDrink=StringVar()
CostOfDesert=StringVar()
service_charge=StringVar()

eae1 = StringVar()
eae2 = StringVar()
eae3 = StringVar()
eae4 = StringVar()
eae5 = StringVar()
eae6 = StringVar()
eae7 = StringVar()
eae8 = StringVar()

eae9 = StringVar()
eae10 = StringVar()
eae11 = StringVar()
eae12 = StringVar()
eae13 = StringVar()
eae14 = StringVar()
eae15 = StringVar()
eae16 = StringVar()

eae1.set("0")
eae2.set("0")
eae3.set("0")
eae4.set("0")
eae5.set("0")
eae6.set("0")
eae7.set("0")
eae8.set("0")

eae9.set("0")
eae10.set("0")
eae11.set("0")
eae12.set("0")
eae13.set("0")
eae14.set("0")
eae15.set("0")
eae16.set("0")


service_charge.set("1.59")

DateOfOrder.set(time.strftime("%d/%m/%y"))

var1.set("0")
var2.set("0")
var3.set("0")
var4.set("0")
var5.set("0")
var6.set("0")
var7.set("0")
var8.set("0")

var9.set("0")
var10.set("0")
var11.set("0")
var12.set("0")
var13.set("0")
var14.set("0")
var15.set("0")
var16.set("0")

ldrink = Label(f2aa,text="DRINKS",font="arial 16 bold",bg="#b85b56")
ldrink.grid(row=0)

ca1 = Checkbutton(f2aa, text="Virgin Mojito \t\t", variable=var1, onvalue=1, offvalue=0, font='arial 14 bold', command=checkbuttonvalue)
ca1.grid(row=1, column=0)
ca2 = Checkbutton(f2aa, text="Oreo Shake \t\t", variable=var2, onvalue=1, offvalue=0, font='arial 14 bold', command=checkbuttonvalue)
ca2.grid(row=2, column=0)
ca3 = Checkbutton(f2aa, text="Lemonade\t\t", variable=var3, onvalue=1, offvalue=0, font='arial 14 bold', command=checkbuttonvalue)
ca3.grid(row=3, column=0)
ca4 = Checkbutton(f2aa, text="Crunchy Frappa \t\t", variable=var4, onvalue=1, offvalue=0, font='arial 14 bold', command=checkbuttonvalue)
ca4.grid(row=4, column=0)
ca5 = Checkbutton(f2aa, text="Blueberry Delight \t\t", variable=var5, onvalue=1, offvalue=0, font='arial 14 bold', command=checkbuttonvalue)
ca5.grid(row=5, column=0)
ca6 = Checkbutton(f2aa, text="Black Coffee \t\t", variable=var6, onvalue=1, offvalue=0, font='arial 14 bold', command=checkbuttonvalue)
ca6.grid(row=6, column=0)
ca7 = Checkbutton(f2aa, text="Red-Bull \t\t\t", variable=var7, onvalue=1, offvalue=0, font='arial 14 bold', command=checkbuttonvalue)
ca7.grid(row=7, column=0)
ca8 = Checkbutton(f2aa, text="Hot-Tea \t\t\t", variable=var8, onvalue=1, offvalue=0, font='arial 14 bold', command=checkbuttonvalue)
ca8.grid(row=8, column=0)


ldesert = Label(f2ab,text="DESERTS",font="arial 16 bold",bg="#b85b56")
ldesert.grid(row=0)

ca9 = Checkbutton(f2ab, text="Chocolate Cheesecake \t\t", variable=var9, onvalue=1, offvalue=0, font='arial 14 bold', command=checkbuttonvalue)
ca9.grid(row=1, column=0)
ca10 = Checkbutton(f2ab, text="Sticky Toffee Pudding \t\t", variable=var10, onvalue=1, offvalue=0, font='arial 14 bold', command=checkbuttonvalue)
ca10.grid(row=2, column=0)
ca11 = Checkbutton(f2ab, text="Fried Ice Cream \t\t\t", variable=var11, onvalue=1, offvalue=0, font='arial 14 bold', command=checkbuttonvalue)
ca11.grid(row=3, column=0)
ca12 = Checkbutton(f2ab, text="Banana Boat Pie \t\t\t", variable=var12, onvalue=1, offvalue=0, font='arial 14 bold', command=checkbuttonvalue)
ca12.grid(row=4, column=0)
ca13 = Checkbutton(f2ab, text="Strawberry Pudding \t\t", variable=var13, onvalue=1, offvalue=0, font='arial 14 bold', command=checkbuttonvalue)
ca13.grid(row=5, column=0)
ca14 = Checkbutton(f2ab, text="Rum Cake \t\t\t", variable=var14, onvalue=1, offvalue=0, font='arial 14 bold', command=checkbuttonvalue)
ca14.grid(row=6, column=0)
ca15 = Checkbutton(f2ab, text="Nutella  Cheesecake \t\t", variable=var15, onvalue=1, offvalue=0, font='arial 14 bold', command=checkbuttonvalue)
ca15.grid(row=7, column=0)
ca16 = Checkbutton(f2ab, texpt="Brownie Gelato \t\t\t", variable=var16, onvalue=1, offvalue=0, font='arial 14 bold', command=checkbuttonvalue)
ca16.grid(row=8, column=0)



ea1 = Entry(f2aa, bd=8, width=6, justify='left', font='arial 16 bold',textvariable = eae1, state=DISABLED)
ea1.grid(row=1, column=2)
ea2 = Entry(f2aa, bd=8, width=6, justify='left', font='arial 16 bold',textvariable = eae2,  state=DISABLED)
ea2.grid(row=2, column=2)
ea3 = Entry(f2aa, bd=8, width=6, justify='left', font='arial 16 bold',textvariable = eae3,  state=DISABLED)
ea3.grid(row=3, column=2)
ea4 = Entry(f2aa, bd=8, width=6, justify='left', font='arial 16 bold',textvariable = eae4,  state=DISABLED)
ea4.grid(row=4, column=2)
ea5 = Entry(f2aa, bd=8, width=6, justify='left', font='arial 16 bold',textvariable = eae5,  state=DISABLED)
ea5.grid(row=5, column=2)
ea6 = Entry(f2aa, bd=8, width=6, justify='left', font='arial 16 bold',textvariable = eae6,  state=DISABLED)
ea6.grid(row=6, column=2)
ea7 = Entry(f2aa, bd=8, width=6, justify='left', font='arial 16 bold',textvariable = eae7,  state=DISABLED)
ea7.grid(row=7, column=2)
ea8 = Entry(f2aa, bd=8, width=6, justify='left', font='arial 16 bold',textvariable = eae8,  state=DISABLED)
ea8.grid(row=8, column=2)





ea9 = Entry(f2ab, bd=8, width=6, justify='left', font='arial 16 bold',textvariable = eae9,  state=DISABLED)
ea9.grid(row=1, column=2)
ea10 = Entry(f2ab, bd=8, width=6, justify='left', font='arial 16 bold',textvariable = eae10,  state=DISABLED)
ea10.grid(row=2, column=2)
ea11 = Entry(f2ab, bd=8, width=6, justify='left', font='arial 16 bold',textvariable = eae11,  state=DISABLED)
ea11.grid(row=3, column=2)
ea12 = Entry(f2ab, bd=8, width=6, justify='left', font='arial 16 bold',textvariable = eae12,  state=DISABLED)
ea12.grid(row=4, column=2)
ea13 = Entry(f2ab, bd=8, width=6, justify='left', font='arial 16 bold',textvariable = eae13,  state=DISABLED)
ea13.grid(row=5, column=2)
ea14 = Entry(f2ab, bd=8, width=6, justify='left', font='arial 16 bold',textvariable = eae14,  state=DISABLED)
ea14.grid(row=6, column=2)
ea15 = Entry(f2ab, bd=8, width=6, justify='left', font='arial 16 bold',textvariable = eae15,  state=DISABLED)
ea15.grid(row=7, column=2)
ea16 = Entry(f2ab, bd=8, width=6, justify='left', font='arial 16 bold',textvariable = eae16,  state=DISABLED)
ea16.grid(row=8, column=2)



#=================== INFORMATION ============================================

rlabel = Label(f3a, font='arial 12 bold', bd=2, text='Receipt')
rlabel.grid(row=0, column=0)
treceipt = Text(f3a, font='arial 12 bold', bd=8, width=59,height=15)
treceipt.grid(row=1, column=0)

#================cost item info =================================================

lcodrink = Label(f2ba, font='arial 14 bold', text="Cost of Drinks", bd=8).grid(row=0, column=0, sticky=W)
ecodrink = Entry(f2ba, font='arial 14 bold', bd=8, justify='left', textvariable=CostOfDrink).grid(row=0, column=1, sticky=W)
lcodesert = Label(f2ba, font='arial 14 bold', text="Cost of Deserts", bd=8).grid(row=1, column=0, sticky=W)
ecodesert = Entry(f2ba, font='arial 14 bold', bd=8, justify='left', textvariable=CostOfDesert).grid(row=1, column=1, sticky=W)

#================ Payment info =====================================================
lservicecharge = Label(f2bb, font='arial 14 bold', text="Service Charge", bd=8).grid(row=0, column=0, sticky=W)
eservicecharge = Entry(f2bb, font='arial 14 bold', bd=8, justify='left', textvariable=service_charge).grid(row=0, column=1, sticky=W)
ltax = Label(f2ba, font='arial 14 bold', text="Tax", bd=8).grid(row=2, column=0, sticky=W)
etax =Entry(f2ba, font='arial 14 bold', bd=8, justify='left', textvariable=PaidTax).grid(row=2, column=1, sticky=W)
lsubtotal = Label(f2bb, font='arial 14 bold', text="Sub Total", bd=8).grid(row=1, column=0, sticky=W)
esubtotal =Entry(f2bb, font='arial 14 bold', bd=8, justify='left', textvariable=SubTotal).grid(row=1, column=1, sticky=W)
ltotal = Label(f2bb, font='arial 14 bold', text="Total", bd=8).grid(row=2, column=0, sticky=W)
etotal =Entry(f2bb, font='arial 14 bold', bd=8, justify='left', textvariable=TotalCost).grid(row=2, column=1, sticky=W)

#==================button total, receipt, exit ================================

total = Button(f3b, padx=16, pady=1, bd=4, fg='black', font='arial 16 bold', width=5, text="Total", command=CostofItem).grid(row=0, column=0)
receipt = Button(f3b, padx=16, pady=1, bd=4, fg='black', font='arial 16 bold', width=5, text="Receipt", command=Receipt).grid(row=0, column=1)
reset = Button(f3b, padx=16, pady=1, bd=4, fg='black', font='arial 16 bold', width=5, text="Reset", command=creset).grid(row=0, column=2)
exit = Button(f3b, padx=16, pady=1, bd=4, fg='black', font='arial 16 bold', width=5, text="Exit", command=qexit).grid(row=0, column=3)

#===============================================================================

cafe.configure(background='#b85b56')
cafe.mainloop()