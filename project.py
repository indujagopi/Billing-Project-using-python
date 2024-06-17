from tkinter import*
from tkinter import messagebox
import random,os,tempfile

        
def clear():

    bathsoapentry.delete(0,END)
    facecreamentry.delete(0,END)
    facewashentry.delete(0,END)
    hairsprayentry.delete(0,END)
    hairgelentry.delete(0,END)
    bodylotionentry.delete(0,END)

    riceentry.delete(0,END)
    oilentry.delete(0,END)
    daalentry.delete(0,END)
    wheatentry.delete(0,END)
    sugarentry.delete(0,END)
    teaentry.delete(0,END)

    maazaentry.delete(0,END)
    pepsientry.delete(0,END)
    spriteentry.delete(0,END)
    dewentry.delete(0,END)
    frootientry.delete(0,END)
    cokeentry.delete(0,END)
    
    bathsoapentry.insert(0,0)
    facecreamentry.insert(0,0)
    facewashentry.insert(0,0)
    hairsprayentry.insert(0,0)
    hairgelentry.insert(0,0)
    bodylotionentry.insert(0,0)

    riceentry.insert(0,0)
    oilentry.insert(0,0)
    daalentry.insert(0,0)
    wheatentry.insert(0,0)
    sugarentry.insert(0,0)
    teaentry.insert(0,0)

    maazaentry.insert(0,0)
    pepsientry.insert(0,0)
    spriteentry.insert(0,0)
    dewentry.insert(0,0)
    frootientry.insert(0,0)
    cokeentry.insert(0,0)

    cosmetictaxentry.delete(0,END)
    grocerytaxentry.delete(0,END)
    drinkstaxentry.delete(0,END)

    cosmeticpriceentry.delete(0,END)
    grocerypriceentry.delete(0,END)
    drinkspriceentry.delete(0,END)

    nameEntry.delete(0,END)
    phoneEntry.delete(0,END)
    billnumberEntry.delete(0,END)

    textarea.delete(1.0,END)

def print_bill():
    if textarea.get(1.0,END)=='\n':
        messagebox.showerror('Error','Bill is empty')
    else:
        file=tempfile.mktemp('.txt')
        open(file,'w').write(textarea.get(1.0,END))
        os.startfile(file,'print')


def search_bill():
    for i in os.listdir('bills/'):
        if i.split('.')[0]==billnumberEntry.get():
            f=open(f'bills/{i}','r')
            textarea.delete(1.0,END)
            for data in f:
                textarea.insert(END,data)
            f.close()
            break
    else:
        messagebox.showerror('Error','Invalid Bill Number')


if not os.path.exists('bills'):
    os.mkdir('bills')    

def save_bill():
    global billnumber
    result=messagebox.askyesno('Confirm','Do you want to save the bill?')
    if result:
        bill_content=textarea.get(1.0,END)
        file=open(f'bills/{billnumber}.txt','w')
        file.write(bill_content)
        file.close()
    
        messagebox.showinfo('Success',f'bill number {billnumber} is saved successfully')
        billnumber=random.randint(500,1000)

billnumber=random.randint(500,1000)

def bill_area():
    
        if nameEntry.get()=='' or phoneEntry.get()=='':
            messagebox.showerror('Error','Customer Details are required')
        elif cosmeticpriceentry.get()=='' and grocerypriceentry.get()=='' and drinkspriceentry.get()=='':
            messagebox.showerror('Error','No Products are selected')
        elif cosmeticpriceentry.get()=='0 Rs' and grocerypriceentry.get()=='0 Rs' and drinkspriceentry.get()=='0 Rs':
            messagebox.showerror('Error','No Products are selected')
        else:
            textarea.delete(1.0,END)
            textarea.insert(END,'\t\t**Welcome Customer**')
            textarea.insert(END,f'\n\nBill Number: {billnumber}')
            textarea.insert(END,f'\nCustomer Name: {nameEntry.get()}')
            textarea.insert(END,f'\nCustomer Phone Number: {phoneEntry.get()}')
            textarea.insert(END,'\n=======================================================')
            textarea.insert(END,'\nProduct\t\t\tQuantity\t\t\tPrice')
            textarea.insert(END,'\n=======================================================')

                   
        #cosmetics
            if bathsoapentry.get()!='0':
                textarea.insert(END,f'\nBath Soap\t\t\t{bathsoapentry.get()}\t\t\t{soapprice} Rs')
            if facecreamentry.get()!='0':
                textarea.insert(END,f'\nFace Cream\t\t\t{facecreamentry.get()}\t\t\t{facecreamprice} Rs')
            if facewashentry.get()!='0':
                textarea.insert(END,f'\nFace Wash\t\t\t{facewashentry.get()}\t\t\t{facewashprice} Rs')
            if hairsprayentry.get()!='0':
                textarea.insert(END,f'\nHair Spray\t\t\t{hairsprayentry.get()}\t\t\t{hairsprayprice} Rs')
            if hairgelentry.get()!='0':
                textarea.insert(END,f'\nHair Gel\t\t\t{hairgelentry.get()}\t\t\t{hairgelprice} Rs')
            if bodylotionentry.get()!='0':
                textarea.insert(END,f'\nBody Lotion\t\t\t{bodylotionentry.get()}\t\t\t{bodylotionprice} Rs')

       #grocery
            if riceentry.get()!='0':
                textarea.insert(END,f'\nRice\t\t\t{riceentry.get()}\t\t\t{riceprice} Rs')
            if oilentry.get()!='0':
                textarea.insert(END,f'\nOil\t\t\t{oilentry.get()}\t\t\t{oilprice} Rs')
            if daalentry.get()!='0':
                textarea.insert(END,f'\nDaal\t\t\t{daalentry.get()}\t\t\t{daalprice} Rs')
            if wheatentry.get()!='0':
                textarea.insert(END,f'\nWheat\t\t\t{wheatentry.get()}\t\t\t{wheatprice} Rs')
            if sugarentry.get()!='0':
                textarea.insert(END,f'\nSugar\t\t\t{sugarentry.get()}\t\t\t{sugarprice} Rs')
            if teaentry.get()!='0':
                textarea.insert(END,f'\nTea\t\t\t{teaentry.get()}\t\t\t{teaprice} Rs')

       #drinks
            if maazaentry.get()!='0':
                textarea.insert(END,f'\nMaaza\t\t\t{maazaentry.get()}\t\t\t{maazaprice} Rs')
            if pepsientry.get()!='0':
                textarea.insert(END,f'\nPepsi\t\t\t{pepsientry.get()}\t\t\t{pepsiprice} Rs')
            if spriteentry.get()!='0':
                textarea.insert(END,f'\nSprite\t\t\t{spriteentry.get()}\t\t\t{spriteprice} Rs')
            if dewentry.get()!='0':
                textarea.insert(END,f'\nDew\t\t\t{dewentry.get()}\t\t\t{dewprice} Rs')
            if frootientry.get()!='0':
                textarea.insert(END,f'\nFrooti\t\t\t{frootientry.get()}\t\t\t{frootiprice} Rs')
            if cokeentry.get()!='0':
                textarea.insert(END,f'\nCoke\t\t\t{cokeentry.get()}\t\t\t{cokeprice} Rs')

            textarea.insert(END,'\n-------------------------------------------------------')

            if cosmetictaxentry.get()!='0.0 Rs':
                textarea.insert(END,f'\nCosmetic Tax\t\t\t\t\t{cosmetictaxentry.get()}')
            if grocerytaxentry.get()!='0.0 Rs':
                textarea.insert(END,f'\nGrocery Tax\t\t\t\t\t{grocerytaxentry.get()}')
            if drinkstaxentry.get()!='0.0 Rs':
                textarea.insert(END,f'\nDrinks Tax\t\t\t\t\t{drinkstaxentry.get()}')

            textarea.insert(END,'\n-------------------------------------------------------')

            textarea.insert(END,f'\nTotal Bill\t\t\t\t\t{totalbill}')

            textarea.insert(END,'\n-------------------------------------------------------')

            save_bill()

def total():

    #cosmetics price
    global soapprice,facecreamprice,facewashprice,hairsprayprice,hairgelprice,bodylotionprice

    soapprice=int(bathsoapentry.get())*20
    facecreamprice=int(facecreamentry.get())*50
    facewashprice=int(facewashentry.get())*100
    hairsprayprice=int(hairsprayentry.get())*150
    hairgelprice=int(hairgelentry.get())*60
    bodylotionprice=int(bodylotionentry.get())*60

    totalcosmeticprice=soapprice+facecreamprice+facewashprice+hairsprayprice+hairgelprice+bodylotionprice
    cosmeticpriceentry.delete(0,END)
    cosmeticpriceentry.insert(0,f'{totalcosmeticprice} Rs')
    cosmetictax=totalcosmeticprice*0.12
    cosmetictaxentry.delete(0,END)
    cosmetictaxentry.insert(0,str(cosmetictax) + ' Rs')

    #grocery price
    global riceprice,oilprice,daalprice,wheatprice,sugarprice,teaprice

    riceprice=int(riceentry.get())*200
    oilprice=int(oilentry.get())*150
    daalprice=int(daalentry.get())*120
    wheatprice=int(wheatentry.get())*70
    sugarprice=int(sugarentry.get())*70
    teaprice=int(teaentry.get())*100

    totalgroceryprice=riceprice+oilprice+daalprice+wheatprice+sugarprice+teaprice
    grocerypriceentry.delete(0,END)
    grocerypriceentry.insert(0,f'{totalgroceryprice} Rs')
    grocerytax=totalgroceryprice*0.05
    grocerytaxentry.delete(0,END)
    grocerytaxentry.insert(0,str(grocerytax) + ' Rs')

    #colddrinks price
    global maazaprice,pepsiprice,spriteprice,dewprice,frootiprice,cokeprice

    maazaprice=int(maazaentry.get())*20
    pepsiprice=int(pepsientry.get())*20
    spriteprice=int(spriteentry.get())*20
    dewprice=int(dewentry.get())*30
    frootiprice=int(frootientry.get())*20
    cokeprice=int(cokeentry.get())*20

    totaldrinksprice=maazaprice+pepsiprice+spriteprice+dewprice+frootiprice+cokeprice
    drinkspriceentry.delete(0,END)
    drinkspriceentry.insert(0,f'{totaldrinksprice} Rs')
    drinkstax=totaldrinksprice*0.08
    drinkstaxentry.delete(0,END)
    drinkstaxentry.insert(0,str(drinkstax) + ' Rs')

    global totalbill
    totalbill=totalcosmeticprice+totalgroceryprice+totaldrinksprice+cosmetictax+grocerytax+drinkstax
 
    
    

root=Tk()
root.title('Retail Billing System')
root.geometry('1270x685')
root.iconbitmap('bill.ico')



headinglabel=Label(root,text='Retail Billing System',font=('Lucida Calligraphy',30,'bold'),
                   bg='lightseagreen',fg='black',bd=2,relief=GROOVE)
headinglabel.pack(fill=X)


customer_details_frame=LabelFrame(root,text='Customer Details',font=('Lucida Calligraphy',25,'bold'),
                                  fg='black',bd=6,relief=GROOVE,bg='lightseagreen')
customer_details_frame.pack(fill=X)


nameLabel=Label(customer_details_frame,text='Name',font=('Lucida Calligraphy',15,'bold'),
                bg='lightseagreen',fg='black')
phoneLabel=Label(customer_details_frame,text='Phone Number',font=('Lucida Calligraphy',15,'bold'),
                 bg='lightseagreen',fg='black')
billnumberLabel=Label(customer_details_frame,text='Bill Number',font=('Lucida Calligraphy',15,'bold'),
                 bg='lightseagreen',fg='black')


nameLabel.grid(row=0,column=0,padx=10)
phoneLabel.grid(row=0,column=2,padx=10,pady=2)
billnumberLabel.grid(row=0,column=4,padx=15,pady=2)


nameEntry=Entry(customer_details_frame,font=('Lucida Calligraphy',15),bd=7,width=18)
phoneEntry=Entry(customer_details_frame,font=('Lucida Calligraphy',15),bd=7,width=18)
billnumberEntry=Entry(customer_details_frame,font=('Lucida Calligraphy',15),bd=7,width=10)


nameEntry.grid(row=0,column=1,padx=8)
phoneEntry.grid(row=0,column=3,padx=8)
billnumberEntry.grid(row=0,column=5,padx=8)

searchbutton=Button(customer_details_frame,text='SEARCH',
                    font=('Lucida Calligraphy',12,'bold'),bd=7,command=search_bill)
searchbutton.grid(row=0,column=6,padx=10,pady=8)

productsframe=Frame(root)
productsframe.pack()

cosmeticsframe=LabelFrame(productsframe,text='Cosmetics',font=('Lucida Calligraphy',15,'bold'),
                                  fg='black',bd=8,relief=GROOVE,bg='lightseagreen')
cosmeticsframe.grid(row=0,column=0)

bathsoaplabel=Label(cosmeticsframe,text='Bath Soap',font=('Lucida Calligraphy',12,'bold'),
                    bg='lightseagreen',fg='black')
facecreamlabel=Label(cosmeticsframe,text='Face Cream',font=('Lucida Calligraphy',12,'bold'),
                    bg='lightseagreen',fg='black')
facewashlabel=Label(cosmeticsframe,text='Face Wash',font=('Lucida Calligraphy',12,'bold'),
                    bg='lightseagreen',fg='black')
hairspraylabel=Label(cosmeticsframe,text='Hair Spray',font=('Lucida Calligraphy',12,'bold'),
                    bg='lightseagreen',fg='black')
hairgellabel=Label(cosmeticsframe,text='Hair Gel',font=('Lucida Calligraphy',12,'bold'),
                    bg='lightseagreen',fg='black')
bodylotionlabel=Label(cosmeticsframe,text='Body Lotion',font=('Lucida Calligraphy',12,'bold'),
                    bg='lightseagreen',fg='black')

bathsoaplabel.grid(row=0,column=0,pady=10,padx=6,sticky='W')
facecreamlabel.grid(row=1,column=0,pady=10,padx=6,sticky='W')
facewashlabel.grid(row=2,column=0,pady=10,padx=6,sticky='W')
hairspraylabel.grid(row=3,column=0,pady=10,padx=6,sticky='W')
hairgellabel.grid(row=4,column=0,pady=10,padx=6,sticky='W')
bodylotionlabel.grid(row=5,column=0,pady=10,padx=6,sticky='W')

bathsoapentry=Entry(cosmeticsframe,font=('Lucida Calligraphy',15,'bold'),width=8,bd=5)
facecreamentry=Entry(cosmeticsframe,font=('Lucida Calligraphy',15,'bold'),width=8,bd=5)
facewashentry=Entry(cosmeticsframe,font=('Lucida Calligraphy',15,'bold'),width=8,bd=5)
hairsprayentry=Entry(cosmeticsframe,font=('Lucida Calligraphy',15,'bold'),width=8,bd=5)
hairgelentry=Entry(cosmeticsframe,font=('Lucida Calligraphy',15,'bold'),width=8,bd=5)
bodylotionentry=Entry(cosmeticsframe,font=('Lucida Calligraphy',15,'bold'),width=8,bd=5)


bathsoapentry.grid(row=0,column=1,pady=8,padx=20)
facecreamentry.grid(row=1,column=1,pady=8,padx=20)
facewashentry.grid(row=2,column=1,pady=8,padx=20)
hairsprayentry.grid(row=3,column=1,pady=8,padx=20)
hairgelentry.grid(row=4,column=1,pady=8,padx=20)
bodylotionentry.grid(row=5,column=1,pady=8,padx=20)

bathsoapentry.insert(0,0)
facecreamentry.insert(0,0)
facewashentry.insert(0,0)
hairsprayentry.insert(0,0)
hairgelentry.insert(0,0)
bodylotionentry.insert(0,0)


groceryframe=LabelFrame(productsframe,text='Grocery',font=('Lucida Calligraphy',15,'bold'),
                                  fg='black',bd=8,relief=GROOVE,bg='lightseagreen')
groceryframe.grid(row=0,column=1)

ricelabel=Label(groceryframe,text='Rice',font=('Lucida Calligraphy',12,'bold'),
                    bg='lightseagreen',fg='black')
oillabel=Label(groceryframe,text='Oil',font=('Lucida Calligraphy',12,'bold'),
                    bg='lightseagreen',fg='black')
daallabel=Label(groceryframe,text='Daal',font=('Lucida Calligraphy',12,'bold'),
                    bg='lightseagreen',fg='black')
wheatlabel=Label(groceryframe,text='Wheat',font=('Lucida Calligraphy',12,'bold'),
                    bg='lightseagreen',fg='black')
sugarlabel=Label(groceryframe,text='Sugar',font=('Lucida Calligraphy',12,'bold'),
                    bg='lightseagreen',fg='black')
tealabel=Label(groceryframe,text='Tea',font=('Lucida Calligraphy',12,'bold'),
                    bg='lightseagreen',fg='black')


ricelabel.grid(row=0,column=0,pady=8,padx=20,sticky='W')
oillabel.grid(row=1,column=0,pady=8,padx=20,sticky='W')
daallabel.grid(row=2,column=0,pady=8,padx=20,sticky='W')
wheatlabel.grid(row=3,column=0,pady=8,padx=20,sticky='W')
sugarlabel.grid(row=4,column=0,pady=8,padx=20,sticky='W')
tealabel.grid(row=5,column=0,pady=8,padx=20,sticky='W')

riceentry=Entry(groceryframe,font=('Lucida Calligraphy',15,'bold'),width=8,bd=5)
oilentry=Entry(groceryframe,font=('Lucida Calligraphy',15,'bold'),width=8,bd=5)
daalentry=Entry(groceryframe,font=('Lucida Calligraphy',15,'bold'),width=8,bd=5)
wheatentry=Entry(groceryframe,font=('Lucida Calligraphy',15,'bold'),width=8,bd=5)
sugarentry=Entry(groceryframe,font=('Lucida Calligraphy',15,'bold'),width=8,bd=5)
teaentry=Entry(groceryframe,font=('Lucida Calligraphy',15,'bold'),width=8,bd=5)

riceentry.grid(row=0,column=1,pady=8,padx=20)
oilentry.grid(row=1,column=1,pady=8,padx=20)
daalentry.grid(row=2,column=1,pady=8,padx=20)
wheatentry.grid(row=3,column=1,pady=8,padx=20)
sugarentry.grid(row=4,column=1,pady=8,padx=20)
teaentry.grid(row=5,column=1,pady=8,padx=20)

riceentry.insert(0,0)
oilentry.insert(0,0)
daalentry.insert(0,0)
wheatentry.insert(0,0)
sugarentry.insert(0,0)
teaentry.insert(0,0)


drinksframe=LabelFrame(productsframe,text='Cold Drinks',font=('Lucida Calligraphy',15,'bold'),
                                  fg='black',bd=8,relief=GROOVE,bg='lightseagreen')
drinksframe.grid(row=0,column=2)

maazalabel=Label(drinksframe,text='Maaza',font=('Lucida Calligraphy',12,'bold'),
                    bg='lightseagreen',fg='black')
pepsilabel=Label(drinksframe,text='Pepsi',font=('Lucida Calligraphy',12,'bold'),
                    bg='lightseagreen',fg='black')
spritelabel=Label(drinksframe,text='Sprite',font=('Lucida Calligraphy',12,'bold'),
                    bg='lightseagreen',fg='black')
dewlabel=Label(drinksframe,text='Dew',font=('Lucida Calligraphy',12,'bold'),
                    bg='lightseagreen',fg='black')
frootilabel=Label(drinksframe,text='Frooti',font=('Lucida Calligraphy',12,'bold'),
                    bg='lightseagreen',fg='black')
cokelabel=Label(drinksframe,text='coke',font=('Lucida Calligraphy',12,'bold'),
                    bg='lightseagreen',fg='black')

maazalabel.grid(row=0,column=0,pady=8,padx=20,sticky='W')
pepsilabel.grid(row=1,column=0,pady=8,padx=20,sticky='W')
spritelabel.grid(row=2,column=0,pady=8,padx=20,sticky='W')
dewlabel.grid(row=3,column=0,pady=8,padx=20,sticky='W')
frootilabel.grid(row=4,column=0,pady=8,padx=20,sticky='W')
cokelabel.grid(row=5,column=0,pady=8,padx=20,sticky='W')

maazaentry=Entry(drinksframe,font=('Lucida Calligraphy',15,'bold'),width=8,bd=5)
pepsientry=Entry(drinksframe,font=('Lucida Calligraphy',15,'bold'),width=8,bd=5)
spriteentry=Entry(drinksframe,font=('Lucida Calligraphy',15,'bold'),width=8,bd=5)
dewentry=Entry(drinksframe,font=('Lucida Calligraphy',15,'bold'),width=8,bd=5)
frootientry=Entry(drinksframe,font=('Lucida Calligraphy',15,'bold'),width=8,bd=5)
cokeentry=Entry(drinksframe,font=('Lucida Calligraphy',15,'bold'),width=8,bd=5)

maazaentry.grid(row=0,column=1,pady=8,padx=20)
pepsientry.grid(row=1,column=1,pady=8,padx=20)
spriteentry.grid(row=2,column=1,pady=8,padx=20)
dewentry.grid(row=3,column=1,pady=8,padx=20)
frootientry.grid(row=4,column=1,pady=8,padx=20)
cokeentry.grid(row=5,column=1,pady=8,padx=20)

maazaentry.insert(0,0)
pepsientry.insert(0,0)
spriteentry.insert(0,0)
dewentry.insert(0,0)
frootientry.insert(0,0)
cokeentry.insert(0,0)

billframe=Frame(productsframe,bd=4,relief=GROOVE)
billframe.grid(row=0,column=3)

billarealabel=Label(billframe,text='Bill Area',font=('Lucida Calligraphy',15,'bold'),bd=7,
                    relief=GROOVE)
billarealabel.pack(fill=X)

scrollbar=Scrollbar(billframe,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)
textarea=Text(billframe,height=18,width=55,yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)

billmenuframe=LabelFrame(root,text='Bill Menu',font=('Lucida Calligraphy',12,'bold'),
                                  fg='black',bd=5,relief=GROOVE,bg='lightseagreen')
billmenuframe.pack()


cosmeticpricelabel=Label(billmenuframe,text='Cosmetic Price',font=('Lucida Calligraphy',10,'bold'),
                    bg='lightseagreen',fg='black')
cosmeticpricelabel.grid(row=0,column=0,pady=6,padx=10,sticky='W')
cosmeticpriceentry=Entry(billmenuframe,font=('times new roman',10,'bold'),width=15,bd=5)
cosmeticpriceentry.grid(row=0,column=1,pady=6,padx=10)

grocerypricelabel=Label(billmenuframe,text='Grocery Price',font=('Lucida Calligraphy',10,'bold'),
                    bg='lightseagreen',fg='black')
grocerypricelabel.grid(row=1,column=0,pady=6,padx=10,sticky='W')
grocerypriceentry=Entry(billmenuframe,font=('Lucida Calligraphy',10,'bold'),width=15,bd=5)
grocerypriceentry.grid(row=1,column=1,pady=6,padx=10)

drinkspricelabel=Label(billmenuframe,text='Cold Drinks Price',font=('Lucida Calligraphy',10,'bold'),
                    bg='lightseagreen',fg='black')
drinkspricelabel.grid(row=2,column=0,pady=6,padx=10,sticky='W')
drinkspriceentry=Entry(billmenuframe,font=('Lucida Calligraphy',10,'bold'),width=15,bd=5)
drinkspriceentry.grid(row=2,column=1,pady=6,padx=10)


cosmetictaxlabel=Label(billmenuframe,text='Cosmetic Tax',font=('Lucida Calligraphy',10,'bold'),
                    bg='lightseagreen',fg='black')
cosmetictaxlabel.grid(row=0,column=2,pady=6,padx=10,sticky='W')
cosmetictaxentry=Entry(billmenuframe,font=('Lucida Calligraphy',10,'bold'),width=15,bd=5)
cosmetictaxentry.grid(row=0,column=3,pady=6,padx=10)


grocerytaxlabel=Label(billmenuframe,text='Grocery Tax',font=('Lucida Calligraphy',10,'bold'),
                    bg='lightseagreen',fg='black')
grocerytaxlabel.grid(row=1,column=2,pady=6,padx=10,sticky='W')
grocerytaxentry=Entry(billmenuframe,font=('Lucida Calligraphy',10,'bold'),width=15,bd=5)
grocerytaxentry.grid(row=1,column=3,pady=6,padx=10)


drinkstaxlabel=Label(billmenuframe,text='Cold Drinks Tax',font=('Lucida Calligraphy',10,'bold'),
                    bg='lightseagreen',fg='black')
drinkstaxlabel.grid(row=2,column=2,pady=6,padx=10,sticky='W')
drinkstaxentry=Entry(billmenuframe,font=('Lucida Calligraphy',10,'bold'),width=15,bd=5)
drinkstaxentry.grid(row=2,column=3,pady=6,padx=10)


buttonframe=Frame(billmenuframe,bd=8,relief=GROOVE)
buttonframe.grid(row=0,column=4,rowspan=3)

totalbutton=Button(buttonframe,text='Total',font=('Lucida Calligraphy',15,'bold'),bg='lightseagreen',
                   fg='black',bd=5,width=8,pady=10,command=total)
totalbutton.grid(row=0,column=0,pady=30,padx=13)

billbutton=Button(buttonframe,text='Bill',font=('Lucida Calligraphy',15,'bold'),bg='lightseagreen',
                  fg='black',bd=5,width=8,pady=10,command=bill_area)
billbutton.grid(row=0,column=1,pady=30,padx=13)


printbutton=Button(buttonframe,text='Print',font=('Lucida Calligraphy',15,'bold'),bg='lightseagreen',
                   fg='black',bd=5,width=8,pady=10,command=print_bill)
printbutton.grid(row=0,column=3,pady=30,padx=13)

clearbutton=Button(buttonframe,text='Clear',font=('Lucida Calligraphy',15,'bold'),bg='lightseagreen',
                   fg='black',bd=5,width=8,pady=10,command=clear)
clearbutton.grid(row=0,column=4,pady=30,padx=13)


root.mainloop()
