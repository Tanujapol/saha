from tkinter import *
from tkinter import messagebox
from datetime import datetime
#import pyttsx3
from mysql.connector import connect
from string import *


username='0'
root = Tk()
root.title('SAHA')
root.resizable(False,False)
root.geometry("1536x864+0+0")
w=1536
h=864
attributes=('Segoe UI Emoji',30,'bold')
conn = connect(
    host = 'localhost',
    user = 'root', 
    password = 'nyfa@27octP',
    database = 'hack1'
)
cursor = conn.cursor()


def home():
    ff=Frame(root,width=w,height=h,bg="#f47c3c")
    ff.place(x=0,y=0)
    f=Frame(root,width=750,height=h,bg="#f47c3c")
    f.place(x=800,y=0)
    f1=Frame(root,width=750,height=810,bg="white")
    f1.place(x=10,y=10)
    f2=Frame(root,width=600,height=250,bg="black")
    f2.place(x=80,y=530)
    c1=Label(f2,text="Contact us",fg='white',bg='black',font=('Arial',35,'bold'))
    c1.place(x=130,y=0)
    c2=Label(f2,text="Please send your quiers to gmail or",fg='white',bg='black',font=('Arial',20,'bold'))
    c2.place(x=30,y=80)
    c3=Label(f2,text="Contact us through phone 01234566",fg='white',bg='black',font=('Arial',20,'bold'))
    c3.place(x=30,y=160)
    h1=Label(f1,text="SAHA",fg='#f47c3c',bg='white',font=('Arial Black',45,'italic'))
    h1.place(x=250,y=100)
    h1=Label(f1,text="Give what you can!!",fg='#f47c3c',bg='white',font=('Cooper Black',25))
    h1.place(x=200,y=200)
    
    img5=PhotoImage(file='saha.png')
    im5=Label(f1,image=img5,border=0)
    im5.place(x=240,y=250)

    b1=Button(f,text='Sign up',bg="black",fg="white",font=("Arial",30,'bold'),width=20,command=signup)
    b1.place(x=150,y=200)

    b2=Button(f,text='Login',bg="black",fg="white",font=("Arial",30,'bold'),width=20,command=login)
    b2.place(x=150,y=400)
    def exit():
       f.destroy()
       ff.destroy()
       f1.destroy()
       root.destroy()
       img5.blank()
    logout_button=Button(f,text='Exit',bg='white',fg='#f47c3c',font=('Cooper Black',20,'bold'),command=exit)
    logout_button.place(x=350,y=600)


def end():
    f111=Frame(root,width=w,height=h,bg="black")
    f111.place(x=0,y=0)
    heading=Label(f111,text='Feedback successfully uploaded!',fg='white',bg='black',font=('Pacifico',30,'bold'))
    heading.place(x=500,y=350)
    def exit():
       f111.destroy()
       users_page()
    logout_button=Button(f111,text='Exit',bg='white',fg='#f47c3c',font=('Cooper Black',20,'bold'),command=exit)
    logout_button.place(x=650,y=700)



def feedback():
    f11=Frame(root,width=w,height=h,bg="black")
    f11.place(x=0,y=0)
    heading=Label(f11,text='FEEDBACK',fg='white',bg='black',font=('Pacifico',44,'bold'),width=10)
    heading.place(x=550,y=180)
    login_b=Button(f11,text='Upload the details',bg="orange",fg="white",font=("Pacifico",20,'bold'),width=40,command=end)
    login_b.place(x=400,y=350)
    def back():
       f11.destroy()
       #img3.blank()
       for_anim()
    back_button=Button(f11,text='Back',bg='steel blue',fg='white',font=('Cooper Black',20,'bold'),command=back)
    back_button.place(x=700,y=650)



def login():
    f=Frame(root,width=w,height=h,bg="black")
    f.place(x=0,y=0)
    fr=Frame(root,width=850,height=h,bg="black")
    fr.place(x=650,y=0)
    heading=Label(fr,text='Log in',fg='white',bg='black',font=('Pacifico',44,'bold'),width=10)
    heading.place(x=230,y=180)

    name=Label(fr,text="Username",font=("Pacifico",30),bg="black",fg="white")
    name.place(x=100,y=300)
    user = Entry(fr,width=15,fg='black',border=1,bg="white",font=("Arial",25))
    user.place(x=300,y=300)
    '''heading=Label(fr,text='Login',fg='black',bg='#f47c3c',font=('Times new roman',44,'bold'))
    heading.place(x=350,y=5)

    name1=Label(fr,text="Name",font=("Arial",30),bg="#f47c3c")
    name1.place(x=100,y=150)
    user1 = Entry(fr,width=15,fg='black',border=1,bg="white",font=("Arail",30))
    user1.place(x=300,y=150)'''

    img3=PhotoImage(file='lock2.png')
    im2=Label(f,image=img3)
    im2.place(x=0,y=0)

    password1=Label(fr,text="password",fg='white',font=("Pacifico",30),bg="black")
    password1.place(x=100,y=400)
    password22 = Entry(fr,show="*",width=15,fg='black',border=2,bg="white",font=("Arial",25))
    password22.place(x=300,y=400)
    def validate_login():
        username = user.get()
        password0 = password22.get()
        # Replace these with your actual username and password
        cursor.execute('select * from users;')
        data = cursor.fetchall()
        names = [item[0] for item in data]
        passw = [pas[1] for pas in data]
        if username in names and password0 in passw and names.index(username)==passw.index(password0):
            messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
            users_page()
        else:
            messagebox.showerror("ERROR","Invalid username and password")
        return username

    login_b=Button(fr,text='Login',bg="red",fg="white",font=("Pacifico",20,'bold'),width=12,command=validate_login)
    login_b.place(x=320,y=500)
    def back():
       fr.destroy()
       img3.blank()
       home()
    back_button=Button(fr,text='Back',bg='steel blue',fg='white',font=('Cooper Black',20,'bold'),command=back)
    back_button.place(x=360,y=600)

def signup():
    frame11=Frame(root,width=w,height=h,bg="black")
    frame11.place(x=0,y=0)
    frame=Frame(root,width=850,height=h,bg="black")
    frame.place(x=750,y=0)
    heading=Label(frame,text='Sign up',fg='white',bg='black',font=('Pacifico',44,'bold'),width=10)
    heading.place(x=230,y=80)

    name=Label(frame,text="Name",font=("Pacifico",30),bg="black",fg="white")
    name.place(x=100,y=200)
    user = Entry(frame,width=15,fg='black',border=1,bg="white",font=("Arial",30))
    user.place(x=300,y=200)

    email=Label(frame,text="Email",font=("Pacifico",30),bg="black",fg="white")
    email.place(x=100,y=300)
    email1 = Entry(frame,width=15,fg='black',border=1,bg="white",font=("Arial",30))
    email1.place(x=300,y=300)

    img1=PhotoImage(file='login9.png')
    im=Label(frame11,image=img1)
    im.place(x=0,y=0)

    password1=Label(frame,text="Password",font=("Pacifico",30),bg="black",fg="white")
    password1.place(x=100,y=400)
    password = Entry(frame,show="*",width=15,fg='black',border=2,bg="white",font=("Arial",30))
    password.place(x=300,y=400)
    def validate_signup():
        username = user.get()
        password0 = password.get()
        email2=email1.get()
        cursor.execute('select * from users;')
        data = cursor.fetchall()
        names = [item[0] for item in data]
        passw = [pas[1] for pas in data]
        # Replace these with your actual username and password
        insert_query = "INSERT INTO users (username, password, email) VALUES (%s, %s, %s)"
        user_data = (username, password0, email2)
        cursor.execute(insert_query, user_data)
        conn.commit()
        if username in names and password0 in passw:
            messagebox.showerror("ERROR","You have already signed up, please login!!")
        else:
          messagebox.showinfo("Signup Successful", "Welcome, " + username + "!")
          users_page()
    def back():
       frame.destroy()
       img1.blank()
       #frame11.destroy()
       home()
    back_button=Button(frame,text='Back',bg='steel blue',fg='white',font=('Pacifico',20,'bold'),command=back)
    back_button.place(x=390,y=600)
    signup=Button(frame,text='Sign up',bg="red",fg="white",font=("Pacifico",20,'bold'),command=validate_signup,width=10)
    signup.place(x=350,y=500)


def for_anim():
    m2=Frame(root,width=w,height=h,bg='black')
    m2.place(x=0,y=0)


    heading=Label(m2,text='Notifications',fg='white',bg='black',font=('Georgia',44,'bold'))
    heading.place(x=550,y=50)

    b11=Label(m2,text='Donation1',bg="steelblue",fg="white",font=("pacifico",20,'bold'),width=30,height=2)
    b11.place(x=490,y=200)

    b22=Label(m2,text='Donation2',bg="steelblue",fg="white",font=("pacifico",20,'bold'),width=30,height=2)
    b22.place(x=490,y=350)
    def back():
       m2.destroy()
       #img2.blank()
       recieve()
    back_button=Button(m2,text='Back',bg='white',fg='steel blue',font=('Cooper Black',20),command=back)
    back_button.place(x=680,y=700)

def last():
    f=Frame(root,width=w,height=h,bg='black')
    f.place(x=0,y=0)

    thx=Label(f,text="Thank You for having a kind heart and donating to the needy!!",fg='white',bg='black',font=attributes)
    thx.place(x=150,y=300)
    def exit():
       f.destroy()
       users_page()
    logout_button=Button(f,text='Exit',bg='white',fg='#f47c3c',font=('Cooper Black',20,'bold'),width=20,command=exit)
    logout_button.place(x=450,y=700)


def for_people():

    m1=Frame(root,width=w,height=h,bg='black')
    m1.place(x=0,y=0)

    heading=Label(m1,text='Notifications',fg='white',bg='black',font=('Georgia',44,'bold'))
    heading.place(x=550,y=50)

    b11=Button(m1,text='Donation1',bg="steelblue",fg="white",font=("pacifico",20,'bold'),command=feedback,width=30,height=2)
    b11.place(x=490,y=200)

    b22=Label(m1,text='Donation2',bg="steelblue",fg="white",font=("pacifico",20,'bold'),width=30,height=2)
    b22.place(x=490,y=350)
    def back():
       m1.destroy()
       #img2.blank()
       recieve()
    back_button=Button(m1,text='Back',bg='white',fg='steel blue',font=('Cooper Black',20),command=back)
    back_button.place(x=680,y=700)



def ngo():

    n_frame=Frame(root,width=w,height=h,bg='white')
    n_frame.place(x=0,y=0)

    n_head=Label(n_frame,text='NGOs LIST',fg='black',bg='white',font=('Georgia',44,'bold'))
    n_head.place(x=550,y=50)

    n_button1=Button(n_frame,text='NGO-1',bg='#f47c3c',fg='white',font=('pacifico',20,'bold'),width=60,height=2)
    n_button1.place(x=300,y=160)

    n_button2=Button(n_frame,text='NGO-2',bg='#f47c3c',fg='white',font=('pacifico',20,'bold'),width=60,height=2)
    n_button2.place(x=300,y=290)


    n_button3=Button(n_frame,text='NGO-3',bg='#f47c3c',fg='white',font=('pacifico',20,'bold'),width=60,height=2)
    n_button3.place(x=300,y=420)

    n_button4=Button(n_frame,text='NGO-4',bg='#f47c3c',fg='white',font=('pacifico',20,'bold'),width=60,height=2)
    n_button4.place(x=300,y=550)

    Im=PhotoImage(file="ngo.png")
    Im1=Label(n_frame,image=Im,border=0)
    Im1.place(x=150,y=140)
    def back():
       n_frame.destroy()
       for_whom()
       Im.blank()
    logout_button=Button(n_frame,text='Back',bg='steel blue',fg='white',font=('Arial Black',15,'bold'),command=back)
    logout_button.place(x=30,y=30)

    back_button=Button(n_frame,text='PROCEED',bg='white',fg='black',font=('Cooper Black',20,'bold'),command=last)
    back_button.place(x=700,y=700)







def recieve():
    m=Frame(root,width=w,height=h,bg='black')
    m.place(x=0,y=0)

    heading=Label(m,text='Reciever',fg='white',bg='black',font=('Georgia',44,'bold'))
    heading.place(x=600,y=50)

    b11=Button(m,text='For People',bg="steelblue",fg="white",font=("pacifico",30,'bold'),width=20,command=for_people)
    b11.place(x=490,y=200)

    b22=Button(m,text='For Animals',bg="steelblue",fg="white",font=("pacifico",30,'bold'),width=20,command=for_anim)
    b22.place(x=490,y=350)

    img2=PhotoImage(file='rec.png')
    im1=Label(m,image=img2,border=0)
    im1.place(x=0,y=500)

    def back():
       m.destroy()
       img2.blank()
       home()
    back_button=Button(m,text='Logout',bg='white',fg='steel blue',font=('Cooper Black',20),command=back)
    back_button.place(x=680,y=500)


def users_page():
    fram=Frame(root,width=w,height=h,bg='white')
    fram.place(x=0,y=0)

    frame2=Frame(fram,width=w,height=105,bg='#f47c3c')
    frame2.place(x=0,y=0)

    h1=Label(fram,text="SAHA",fg='white',font=('Arial Black',45),background='#f47c3c')
    h1.place(x=625,y=10)

    donate_button=Button(fram,text='DONATE',bg='#f47c3c',fg='white',font=('Cooper Black',40,'bold'),command=for_whom)
    donate_button.place(x=560,y=200)
    recieve_button=Button(fram,text='RECIEVE',bg='#f47c3c',fg='white',font=('Cooper Black',40,'bold'),command=recieve)
    recieve_button.place(x=560,y=440)
    def logout():
       fram.destroy()
       home()
    logout_button=Button(fram,text='Logout',bg='white',fg='#f47c3c',font=('Cooper Black',20,'bold'),command=logout)
    logout_button.place(x=1300,y=40)



def for_whom():
    fra=Frame(root,width=w,height=h,bg='white')
    fra.place(x=0,y=0)
    frame2=Frame(fra,width=w,height=105,bg='#f47c3c')
    frame2.place(x=0,y=0)

    h1=Label(fra,text="SAHA",fg='white',font=('Arial Black',45),background='#f47c3c')
    h1.place(x=625,y=10)

    homeless=Button(fra,text='Food for Homeless',bg='#f47c3c',fg='white',font=('Cooper Black',35,'bold'),command=details_page_donor)
    homeless.place(x=500,y=200)
    animals=Button(fra,text='Food for Animals',bg='#f47c3c',fg='white',font=('Cooper Black',35,'bold'),command=for_animals)
    animals.place(x=500,y=440)
    def back():
       fra.destroy()
       users_page()
    logout_button=Button(fra,text='Back',bg='#f47c3c',fg='white',font=('Cooper Black',20,'bold'),command=back)
    logout_button.place(x=740,y=680)



def for_animals():
    frame10=Frame(root,width=w,height=h,bg='white')
    frame10.place(x=0,y=0)
    det=Label(frame10,text="DONATE FOOD",fg='black',bg='white',font=('Pacifico',44,'bold'))
    det.place(x=550,y=20)
    #det1=Label(frame1,text="Fill the details:",fg='black',bg='white',font=attributes)
    #det1.place(x=500,y=70)
    det2=Label(frame10,text="Name:",fg='black',bg='white',font=attributes)
    det2.place(x=450,y=130)
    ent1=Entry(frame10,text="Name:",fg='black',bg='white',font=('Arial',25,'bold'))
    ent1.place(x=700,y=140)
    det3=Label(frame10,text="Mobile No:",fg='black',bg='white',font=attributes)
    det3.place(x=450,y=190)
    ent2=Entry(frame10,fg='black',bg='white',font=('Arial',25,'bold'))
    ent2.place(x=700,y=200)
    det4=Label(frame10,text="Location:",fg='black',bg='white',font=attributes)
    det4.place(x=450,y=240)
    options=StringVar()
    options.set('Bhimavram')
    drop=OptionMenu(frame10,options,'Bhimavaram','Visakoduru','Guntur','Hyderabad','Vizag','Ongole','Kakinada','Kanigiri','Amalapuram')
    drop.config(width=20,font=('Arial',18,'bold'))  # Set the width of the dropdown button
    drop.pack(pady=20)
    drop.place(x=700,y=260)
    det6=Label(frame10,text="Quantity:",fg='black',bg='white',font=attributes)
    det6.place(x=450,y=500)
    ent3=Entry(frame10,fg='black',bg='white',font=('Arial',25,'bold'))
    ent3.place(x=700,y=520)
    options0=StringVar()
    options0.set('01')
    drop0=OptionMenu(frame10,options0,'01','02','03','04','05','06','07','08','09','10','11','12')
    drop0.place(x=700,y=630)
    options1=StringVar()
    options1.set('00')
    drop1=OptionMenu(frame10,options1,'00','05','10','15','20','25','30','35','40','45','50','55')
    drop1.place(x=750,y=630)
    options2=StringVar()
    options2.set('am')
    drop3=OptionMenu(frame10,options2,'am','pm')
    drop3.place(x=800,y=630)
    det7=Label(frame10,text="Time",fg='black',bg='white',font=attributes)
    det7.place(x=450,y=610)
    donate=Button(frame10,text='Donate',fg='white',bg='red',font=('Arial Black',20),command=ngo)
    donate.place(x=700,y=700)

    img4=PhotoImage(file='don.png')
    im0=Label(frame10,image=img4,border=0)
    im0.place(x=100,y=300)
    img5=PhotoImage(file='don.png')
    im9=Label(frame10,image=img5,border=0)
    im9.place(x=1200,y=300)

    def back():
       frame10.destroy()
       for_whom()
       img4.blank()
       img5.blank()
    logout_button=Button(frame10,text='Back',bg='steel blue',fg='white',font=('Arial Black',15,'bold'),command=back)
    logout_button.place(x=30,y=30)



def details_page_donor():
    frame1=Frame(root,width=w,height=h,bg='white')
    frame1.place(x=0,y=0)
    det=Label(frame1,text="DONATE FOOD",fg='black',bg='white',font=('Pacifico',44,'bold'))
    det.place(x=550,y=20)
    det2=Label(frame1,text="Name:",fg='black',bg='white',font=attributes)
    det2.place(x=450,y=130)
    ent1=Entry(frame1,text="Name:",fg='black',bg='white',font=('Arial',25,'bold'))
    ent1.place(x=700,y=140)
    det3=Label(frame1,text="Mobile No:",fg='black',bg='white',font=attributes)
    det3.place(x=450,y=190)
    ent2=Entry(frame1,fg='black',bg='white',font=('Arial',25,'bold'))
    ent2.place(x=700,y=200)
    det4=Label(frame1,text="Location:",fg='black',bg='white',font=attributes)
    det4.place(x=450,y=240)
    options=StringVar()
    options.set('Bhimavram')
    drop=OptionMenu(frame1,options,'Bhimavaram','Visakoduru','Guntur','Hyderabad','Vizag','Ongole','Kakinada','Kanigiri','Amalapuram')
    drop.config(width=20,font=('Arial',18,'bold'))  # Set the width of the dropdown button
    drop.pack(pady=20)
    drop.place(x=700,y=260)
    det5=Label(frame1,text="Food Type",fg='black',bg='white',font=attributes)
    det5.place(x=450,y=350)
    a1=IntVar()
    a2=IntVar()
    a=[a1,a2]
    type=['veg','non-veg']
    i=0
    j=0
    k=0
    for check in type:
       check1=Checkbutton(frame1,text=check,bg='white',fg='black',variable=a[i],font=('Algerian',20),width=20)
       check1.place(x=450+k,y=450)
       j=j+45
       i=i+1
       k=k+300
    det6=Label(frame1,text="Quantity:",fg='black',bg='white',font=attributes)
    det6.place(x=450,y=500)
    ent3=Entry(frame1,fg='black',bg='white',font=('Arial',25,'bold'))
    ent3.place(x=700,y=520)
    options0=StringVar()
    options0.set('01')
    drop0=OptionMenu(frame1,options0,'01','02','03','04','05','06','07','08','09','10','11','12')
    drop0.place(x=700,y=630)
    options1=StringVar()
    options1.set('00')
    drop1=OptionMenu(frame1,options1,'00','05','10','15','20','25','30','35','40','45','50','55')
    drop1.place(x=750,y=630)
    options2=StringVar()
    options2.set('am')
    drop3=OptionMenu(frame1,options2,'am','pm')
    drop3.place(x=800,y=630)
    det7=Label(frame1,text="Time",fg='black',bg='white',font=attributes)
    det7.place(x=450,y=610)
    donate=Button(frame1,text='Donate',fg='white',bg='red',font=('Arial Black',20),command=ngo)
    donate.place(x=700,y=700)

    img4=PhotoImage(file='don.png')
    im0=Label(frame1,image=img4,border=0)
    im0.place(x=100,y=300)
    img5=PhotoImage(file='don.png')
    im9=Label(frame1,image=img5,border=0)
    im9.place(x=1200,y=300)

    def back():
       frame1.destroy()
       for_whom()
       img4.blank()
       img5.blank()
    logout_button=Button(frame1,text='Back',bg='steel blue',fg='white',font=('Arial Black',15,'bold'),command=back)
    logout_button.place(x=30,y=30)



home()
root.mainloop()


