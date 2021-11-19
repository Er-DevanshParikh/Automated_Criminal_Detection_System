import os
from tkinter import messagebox
from tkinter import filedialog
from tkinter import *
import mysql.connector
import PIL
from PIL import ImageTk, Image
import cv2
import pickle
import numpy as np

def register_user():
    uid = uid_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    address = address_entry.get()
    dob = dob_entry.get()
    mobileno = mobileno_entry.get()
    email = email_entry.get()
    designation = designation_entry.get()
    # Open database connection
    db = mysql.connector.connect(host='localhost', user='root', password='', db='acds')
    print("Connected Sucsessfully")
    cursor = db.cursor()
    sql = """INSERT INTO  `acds_registration` (`uid`,`username`,`password`,`address`,`dob`,`mobileno`,`email`,`designation`) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"""
    my_data = (uid, username, password, address, dob, mobileno, email, designation)
    cursor.execute(sql, my_data)
    # print("Data Insert Sucsessfully")
    db.commit()
    # disconnect from server
    db.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)
    address_entry.delete(0, END)
    uid_entry.delete(0, END)
    address_entry.delete(0, END)
    dob_entry.delete(0, END)
    mobileno_entry.delete(0, END)
    email_entry.delete(0, END)
    designation_entry.delete(0, END)
    register_sucess()



def login_verify():
    username = username_login_entry.get()
    password = password_login_entry.get()
    # Open database connection
    db = mysql.connector.connect(host='localhost', user='root', password='', db='acds')
    print("Connected Sucsessfully")
    cursor = db.cursor()
    sql = """SELECT * FROM acds_registration where username=%s and password=%s"""
    my_data = (username, password)
    cursor.execute(sql, my_data)
    results = cursor.fetchall()
    if results:
        for i in results:
            login_sucess()
            break
    else:
        user_not_found()
    db.commit()
    # disconnect from server
    db.close()


def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.configure(background="purple")
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Successfully", fg="white", bg="purple").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()


def register_sucess():
    global register_sucess_screen
    register_sucess_screen = Toplevel(registration_screen)
    register_sucess_screen.configure(background="purple")
    register_sucess_screen.title("Success")
    register_sucess_screen.geometry("150x100")
    Label(register_sucess_screen, text="Registration Successfully ", fg="white", bg="purple").pack()
    Button(register_sucess_screen, text="OK", command=delete_register).pack()

def insert_sucess():
    global insert_sucess_screen
    insert_sucess_screen = Toplevel(main_record_form)
    insert_sucess_screen.configure(background="purple")
    insert_sucess_screen.title("Success")
    insert_sucess_screen.geometry("150x100")
    Label(insert_sucess_screen, text="Dataset Created Successfully ", fg="white", bg="purple").pack()
    Button(insert_sucess_screen, text="OK", command=delete_insert).pack()

# Deleting popups
def delete_login():
    login_screen.destroy()
    main_screen()
def delete_register():
    registration_screen.destroy()
    main_screen()

def delete_login_success():
    mainmenu()
def delete_insert():
    main_record_form.destroy()
    mainmenu()

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()


def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()


def record_info():
    global a, b, c, d, e, f, g, h, i, j, k
    a = criminalID_entry.get()
    b = criminalname_entry.get()
    c = fathername_entry.get()
    d = mothername_entry.get()
    e = address_entry.get()
    f = city_entry.get()
    g = state_entry.get()
    h = dob_entry.get()
    i = gender_entry.get()
    j = crimerecord_entry.get()
    k = crimestatus_entry.get()
    # Open database connection
    db = mysql.connector.connect(host='localhost', user='root', password='', db='acds')
    print("Connected Sucsessfully")
    cursor = db.cursor()
    sql = """INSERT INTO  `acds_criminal_record` (`Criminal ID`,`Criminal Name`,`Father Name`,`Mother Name`,`Address`,`City`,`State`,`Date Of Birth`,`Gender`,`Crime Record`,`Crime Status`) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    my_data = (a, b, c, d, e, f, g, h, i, j, k)
    cursor.execute(sql, my_data)
    print("Data Insert Sucsessfully")
    db.commit()
    # disconnect from server
    db.close()
    createdata(criminalID_entry)
    # Clear The Entry Widget
    criminalID_entry.delete(0, END)
    criminalname_entry.delete(0, END)
    fathername_entry.delete(0, END)
    mothername_entry.delete(0, END)
    address_entry.delete(0, END)
    city_entry.delete(0, END)
    state_entry.delete(0, END)
    dob_entry.delete(0, END)
    gender_entry.delete(0, END)
    crimerecord_entry.delete(0, END)
    crimestatus_entry.delete(0, END)
    main_record_form.destroy()

def record_form():
    global main_record_form
    #variable
    global criminalID, criminalname, dob, gender, address, city, state, bloodgroup, fathername, mothername, crimerecord,crimestatus
    global criminalID_entry, criminalname_entry, dob_entry,gender_entry, crimerecord_entry, address_entry, city_entry,state_entry
    global bloodgroup_entry, fathername_entry, mothername_entry, crimestatus_entry
    criminalID=StringVar()
    criminalname=StringVar()
    dob=StringVar()
    gender=StringVar()
    crimerecord=StringVar()
    address=StringVar()
    city=StringVar()
    state=StringVar()
    bloodgroup=StringVar()
    fathername=StringVar()
    mothername=StringVar()
    caseID=StringVar()
    crimestatus=StringVar()
    main_record_form=Tk()
    main_record_form.configure(background="purple")
    main_record_form.title("Criminal Data Record")
    # main_record_form.geometry('1500x900+200+100')
    main_record_form.attributes('-fullscreen', True)
    main_record_form.resizable(width = 200, height = 200)
    frame=LabelFrame(main_record_form,text="Personal Form",bg="purple",fg="white",padx=20,pady=30)
    frame.place(x=500,y=60)
    frame1=LabelFrame(main_record_form,text="Crime Details",bg="purple",fg="white",padx=20,pady=30)
    frame1.place(x=1000,y=60)
    label=Label(main_record_form,text="WELCOME \n AUTOMATED CRIMINAL DETECTION SYSTEM",fg="white",bg="purple",font=("Bold",15)).place(x=500,y=0)
    label_0=Label(main_record_form,text="New Data Record ",width=20,font=("Bold",20),fg="white",bg="purple")
    label_0.place(x=40,y=150)
    # label_0=Label(frame,text="Login Page",width=20,font=("Bold",20))
    # label_0.grid(row=1,column=1)
    # img = Image.open("acds.png")
    # img = img.resize((300, 250), Image.ANTIALIAS)
    # img = ImageTk.PhotoImage(img)
    # # create a label
    # panel = Label(main_record_form, image = img,bg="purple",anchor=CENTER).place(x=150,y=300)
    #ID
    label_1=Label(frame,text="Criminal ID *",width=20,font=("Bold",10),fg="white",bg="purple")
    label_1.grid(row=1,column=0)
    criminalID_entry=Entry(frame,textvariable=criminalID)
    criminalID_entry.grid(row=1,column=1,pady=10,padx=0)

    #username
    label_2=Label(frame,text="Criminal Name *",width=20,font=("Bold",10),fg="white",bg="purple")
    label_2.grid(row=4,column=0,pady=20,padx=0)
    criminalname_entry=Entry(frame,textvariable=criminalname)
    criminalname_entry.grid(row=4,column=1,pady=20,padx=0)

    #fathername
    label_3=Label(frame,text="Father Name *",width=20,font=("Bold",10),fg="white",bg="purple")
    label_3.grid(row=6,column=0,pady=20,padx=0)
    fathername_entry=Entry(frame,textvariable=fathername)
    fathername_entry.grid(row=6,column=1,pady=20,padx=0)

    #mothername
    label_4=Label(frame,text="Mother Name *",width=20,font=("Bold",10),fg="white",bg="purple")
    label_4.grid(row=8,column=0,pady=20,padx=0)
    mothername_entry=Entry(frame,textvariable=mothername)
    mothername_entry.grid(row=8,column=1,pady=20,padx=0)

    #address
    label_5=Label(frame,text="Permanent Address *",width=20,font=("Bold",10),fg="white",bg="purple")
    label_5.grid(row=10,column=0,pady=20,padx=0)
    address_entry=Entry(frame,textvariable=address)
    address_entry.grid(row=10,column=1,pady=20,padx=0)

    #city
    label_6=Label(frame,text="City *",width=20,font=("Bold",10),fg="white",bg="purple")
    label_6.grid(row=12,column=0,pady=20,padx=0)
    city_entry=Entry(frame,textvariable=city)
    city_entry.grid(row=12,column=1,pady=20,padx=0)

    #state
    label_7=Label(frame,text="State *",width=20,font=("Bold",10),fg="white",bg="purple")
    label_7.grid(row=14,column=0,pady=20,padx=0)
    state_entry=Entry(frame,textvariable=state)
    state_entry.grid(row=14,column=1,pady=20,padx=0)

    #DOB
    label_8=Label(frame,text="dob *",width=20,font=("Bold",10),fg="white",bg="purple")
    label_8.grid(row=16,column=0,pady=20,padx=0)
    dob_entry=Entry(frame,textvariable=dob)
    dob_entry.grid(row=16,column=1,pady=20,padx=0)

    #Gender
    label_9=Label(frame,text="Gender *",width=20,font=("Bold",10),fg="white",bg="purple")
    label_9.grid(row=18,column=0,pady=20,padx=0)
    gender_entry=Entry(frame,textvariable=gender)
    gender_entry.grid(row=18,column=1,pady=20,padx=0)

    #caseID
    label_10=Label(frame1,text="Crime Record *",width=20,font=("Bold",10),fg="white",bg="purple")
    label_10.grid(row=1,column=0)
    crimerecord_entry=Entry(frame1,textvariable=crimerecord)
    crimerecord_entry.grid(row=1,column=1,pady=20,padx=0)

    #Crime record
    label_11=Label(frame1,text="Crime Status *",width=20,font=("Bold",10),fg="white",bg="purple")
    label_11.grid(row=4,column=0,pady=20,padx=0)
    crimestatus_entry=Entry(frame1,textvariable=crimestatus)
    crimestatus_entry.grid(row=4,column=1,pady=20,padx=0)
    #Insert Button
    Button(main_record_form,text="Inserted",width=15,fg="white",bg="purple",command=record_info).place(x=1100,y=300)
    Button(main_record_form, text="Back To Mainscreen", width=20,height=2, bg="purple", fg="white",command=delete_insert).place(x=1090,y=600)
    main_record_form.mainloop()



def createdata(ID):
    detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    Id = ID.get()
    facedec=Tk()
    facedec.withdraw()
    path=filedialog.askopenfilename(initialdir=os.getcwd(),title="select your image",filetypes=(("JPG File","*.jpg"),("PNG File","*.png"),("ALL File","*.*")))
    sampleNum = 0
    while (True):
        img = cv2.imread(path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

            # incrementing sample number
            sampleNum = sampleNum + 1
            # saving the captured face in the dataset folder
            cv2.imwrite("datasetimg/User." + Id + '.' + str(sampleNum) + ".jpg", gray[y:y + h, x:x + w])

            cv2.imshow('frame', img)
        # wait for 100 miliseconds
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break
        # break if the sample number is morethan 20
        elif sampleNum > 100:
            break
    cv2.destroyAllWindows()
    messagebox.showinfo("Successfully ", "DataSet Created")
    # os.system("py menu.py")


def traindata():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    def getImagesAndLabels(path):
        # get the path of all the files in the folder
        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
        # create empth face list
        faceSamples = []
        # create empty ID list
        Ids = []
        # now looping through all the image paths and loading the Ids and the images
        for imagePath in imagePaths:
            # loading the image and converting it to gray scale
            pilImage = PIL.Image.open(imagePath).convert('L')
            # Now we are converting the PIL image into numpy array
            imageNp = np.array(pilImage, 'uint8')
            # getting the Id from the image
            Id = int(os.path.split(imagePath)[-1].split(".")[1])
            # extract the face from the training image sample
            faces = detector.detectMultiScale(imageNp)
            # If a face is there then append that in the list as well as Id of it
            for (x, y, w, h) in faces:
                faceSamples.append(imageNp[y:y + h, x:x + w])
                Ids.append(Id)
        return faceSamples, Ids

    faces, Ids = getImagesAndLabels('datasetimg')
    s = recognizer.train(faces, np.array(Ids))
    # print("Successfully trained")
    recognizer.write('datasettrainner/trainner.yml')
    messagebox.showinfo("Successfully ", "Successfully trained")

def getprofile(Id):
    db = mysql.connector.connect(host='localhost', user='root', password='', db='acds')
    print("Connected Sucsessfully")
    cursor = db.cursor()
    cmd = "SELECT * FROM acds_criminal_record WHERE ID=" + str(Id)
    cursor.execute(cmd)
    profile = NONE
    #tuple
    #s = cursor.fetchall()
    for row in cursor:
         profile = row
    db.commit()
    # disconnect from server
    db.close()
    return profile

def recognized():
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    #cam = cv2.VideoCapture(0)
    # face Recognized
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('datasettrainner/trainner.yml')
    facerec=Tk()
    facerec.withdraw()
    # font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 1, 1)
    font = cv2.FONT_HERSHEY_SIMPLEX
    path=filedialog.askopenfilename(initialdir=os.getcwd(),title="select your image",filetypes=(("JPG File","*.jpg"),("PNG File","*.png"),("ALL File","*.*")))
    while True:
        im = cv2.imread(path)
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.2, 5)
        for (x, y, w, h) in faces:
            rect = cv2.rectangle(im, (x, y), (x + w, y + h), (225, 0, 0), 2)
            Id, conf = recognizer.predict(gray[y:y + h, x:x + w])
            confidence = int(100*(1-conf/300))
            profile=getprofile(Id)
            if (profile != None):
                print("Id:" + str(profile[1]))  # Draw the text
                # print("Name:" + str(profile[2]))  # Draw the text
                # print("Father Name:" + str(profile[3]))  # Draw the text
                # print("Mother Name:" + str(profile[4]))  # Draw the text
                # print("Address:" + str(profile[5]))  # Draw the text
                # print("City:" + str(profile[6]))  # Draw the text
                # print("State:" + str(profile[7]))  # Draw the text
                # print("DOB:" + str(profile[8]))  # Draw the text
                # print("Gender :" + str(profile[9]))  # Draw the text
                # print("Criminal Record:" + str(profile[10]))  # Draw the text
                # print("Criminal Status:" + str(profile[11]))  # Draw the text
            else:
                Id="Unknown"
                print("Criminal Status:" + str(Id))  # Draw the text
                # cv2.putText(im,str(Id)+" "+str(conf),(x,y-10),font,0.55,(120,255,120),1)
                # cv2.putText(im, str(Id) + " " + str(conf), (x, y - 10), font, 0.55, (0, 0, 255), 1)
                # cv2.cv.PutText(cv2.cv.fromarray(im),str(Id), (x,y+h),font, 255)
        #height, width = im.shape[:2]
        cv2.namedWindow('Camera', cv2.WINDOW_FULLSCREEN)
        #cv2.resizeWindow('Camera', width, height)
        cv2.imshow('Camera', im)
        # cv2.resizeWindow('Camera',700,800)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    messagebox.showinfo("Criminal Information ","Id:" + str(profile[1])+"\n"+
                                "Name:" + str(profile[2])+"\n"+
                                "Father Name:" + str(profile[3])+"\n"+
                                "Mother Name:" + str(profile[4])+"\n"+
                                "Address:" + str(profile[5])+"\n"+
                                "City:" + str(profile[6])+"\n"+
                                "State:" + str(profile[7])+"\n"+
                                "DOB:" + str(profile[8])+"\n"+
                                "Gender :" + str(profile[9])+"\n"+
                                "Criminal Record:" + str(profile[10])+"\n"+
                                "Criminal Record:" + str(profile[10])+"\n",icon='warning')
    # noOfFile=len(os.listdir())+1
    # cv2.imwrite("Criminal"+str(noOfFile) + ".jpg", im[y:y+h,x:x+w])
    #cam.release()
    cv2.destroyAllWindows()
    # os.system("py menu.py")


def destroyexit():
    maindatasetscreen.destroy()
    main_screen()


def login():
    global login_screen
    login_screen = Toplevel(mainscreen)
    mainscreen.destroy()
    login_screen=Tk()
    login_screen.configure(background="purple")
    login_screen.title("Criminal Data Record")
    # login_screen.geometry('1500x900+200+100')
    login_screen.attributes('-fullscreen', True)
    login_screen.resizable(width = 200, height = 200)
    label=Label(login_screen,text="WELCOME \n AUTOMATED CRIMINAL DETECTION SYSTEM",anchor=CENTER,fg="white",bg="purple",font=("Bold",15)).pack()
    img = Image.open("acds.png")
    img = img.resize((300, 250), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    # create a label
    panel = Label(login_screen, image = img,bg="purple",anchor=CENTER).place(x=150,y=300)
    label_0=Label(login_screen,text="Login Page",width=20,font=("Bold",20),fg="white",bg="purple",anchor=CENTER).place(x=700,y=150)

    global username_login
    global password_login

    username_login = StringVar()
    password_login = StringVar()

    global username_login_entry
    global password_login_entry
    # label_0 = Label(login_screen, text="Login Page", width=20, font=("Bold", 20), fg="white", bg="purple")
    # label_0.place(x=100,y=200)

    # username
    label_1 = Label(login_screen, text="Username", width=20, font=("Bold", 10), fg="white", bg="purple",anchor=CENTER)
    label_1.place(x=690,y=250)
    username_login_entry = Entry(login_screen, textvariable=username_login)
    username_login_entry.place(x=850,y=250)

    # password
    label_2 = Label(login_screen, text="Password", width=20, font=("Bold", 10), fg="white", bg="purple",anchor=CENTER)
    label_2.place(x=690,y=300)
    password_login_entry = Entry(login_screen, show='*', textvariable=password_login)
    password_login_entry.place(x=850,y=300)

    Button(login_screen, text="Login", width=10, bg="purple", fg="white",command=login_verify).place(x=750,y=450)
    Button(login_screen, text="New User Registration", width=20, bg="purple", fg="white",command=delete_login).place(x=850,y=450)

    login_screen.mainloop()


def register():
    global registration_screen
    registration_screen = Toplevel(mainscreen)
    mainscreen.destroy()
    registration_screen = Tk()
    global uid, username, address, dob, mobileno, email, password, designation
    global uid_entry, username_entry, password_entry, address_entry, dob_entry, mobileno_entry, email_entry, designation_entry
    username = StringVar()
    password = StringVar()
    uid = StringVar()
    username = StringVar()
    address = StringVar()
    dob = StringVar()
    mobileno = StringVar()
    email = StringVar()
    password = StringVar()
    designation = StringVar()
    registration_screen.configure(background="purple")
    registration_screen.title("AUTOMATED CRIMINAL DETECTION SYSTEM")
    registration_screen.geometry('1500x900+200+100')
    # registration_screen.geometry('1500x900+200+100')
    registration_screen.attributes('-fullscreen', True)
    registration_screen.resizable(width = 200, height = 200)
    label=Label(registration_screen,text="WELCOME \n AUTOMATED CRIMINAL DETECTION SYSTEM",anchor=CENTER,fg="white",bg="purple",font=("Bold",15)).pack()
    img = Image.open("acds.png")
    img = img.resize((300, 250), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    # create a label
    panel = Label(registration_screen, image = img,bg="purple",anchor=CENTER).place(x=150,y=300)
    # label=Label(registration_screen,text="WELCOME \n AUTOMATED CRIMINAL DETECTION SYSTEM",width=100,font=("Bold",15)).pack()
    label_0 = Label(registration_screen, text="Registration Page", width=20, font=("Bold", 20), fg="white", bg="purple")
    label_0.place(x=800, y=100)

    # UID
    label_1 = Label(registration_screen, text="User ID", width=20, font=("Bold", 10), fg="white", bg="purple")
    label_1.place(x=820, y=200)
    uid_entry = Entry(registration_screen, textvariable=uid)
    uid_entry.place(x=950, y=200)

    # username
    label_3 = Label(registration_screen, text="Designation", width=20, font=("Bold", 10), fg="white", bg="purple")
    label_3.place(x=820, y=250)
    designation_entry = Entry(registration_screen, textvariable=designation)
    designation_entry.place(x=950, y=250)

    # UName
    label_2 = Label(registration_screen, text="UserName", width=20, font=("Bold", 10), fg="white", bg="purple")
    label_2.place(x=820, y=300)
    username_entry = Entry(registration_screen, textvariable=username)
    username_entry.place(x=950, y=300)

    # Address
    label_3 = Label(registration_screen, text="Address", width=20, font=("Bold", 10), fg="white", bg="purple")
    label_3.place(x=820, y=350)
    address_entry = Entry(registration_screen, textvariable=address)
    address_entry.place(x=950, y=350)

    # DOB
    label_4 = Label(registration_screen, text="DOB", width=20, font=("Bold", 10), fg="white", bg="purple")
    label_4.place(x=820, y=400)
    dob_entry = Entry(registration_screen, textvariable=dob)
    dob_entry.place(x=950, y=400)

    # mobileno
    label_5 = Label(registration_screen, text="Mobile No", width=20, font=("Bold", 10), fg="white", bg="purple")
    label_5.place(x=820, y=450)
    mobileno_entry = Entry(registration_screen, textvariable=mobileno)
    mobileno_entry.place(x=950, y=450)

    # email
    label_6 = Label(registration_screen, text="Email", width=20, font=("Bold", 10), fg="white", bg="purple")
    label_6.place(x=820, y=500)
    email_entry = Entry(registration_screen, textvariable=email)
    email_entry.place(x=950, y=500)

    # password
    label_4 = Label(registration_screen, text="Password", width=20, font=("Bold", 10), fg="white", bg="purple")
    label_4.place(x=820, y=550)
    password_entry = Entry(registration_screen, show='*', textvariable=password)
    password_entry.place(x=950, y=550)

    # Button
    Button(registration_screen, text="Register", width=15, bg="purple", fg="white",command=register_user).place(x=850,y=600)
    Button(registration_screen, text="Back to Login", width=15, bg="purple", fg="white",command=delete_register).place(x=980,y=600)
    registration_screen.mainloop()


def mainmenu():
    global maindatasetscreen
    maindatasetscreen = Toplevel(login_screen)
    log_user = username_login_entry.get()
    login_screen.destroy()
    maindatasetscreen = Tk()
    maindatasetscreen.title("Main Menu")
    maindatasetscreen.configure(background="purple")
    # maindatasetscreen.geometry('1500x900+200+100')
    maindatasetscreen.attributes('-fullscreen', True)
    maindatasetscreen.resizable(width = 200, height = 200)
    label=Label(maindatasetscreen,text="WELCOME \n AUTOMATED CRIMINAL DETECTION SYSTEM",anchor=CENTER,fg="white",bg="purple",font=("Bold",15)).pack()
    img = Image.open("acds.png")
    img = img.resize((300, 250), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    # create a label
    panel = Label(maindatasetscreen, image = img,bg="purple",anchor=CENTER).place(x=150,y=300)
    Label(maindatasetscreen, text="MAIN MENU", width=100,bg="purple",fg="white" ,font=("Bold", 15)).pack()
    Label(maindatasetscreen, text="Login Successfully!... Welcome {} ".format(log_user), fg="white",bg="purple", font="bold").pack()
    Button(text="Create Dataset", anchor=CENTER, font=("Bold", 20), fg="purple", bg="white", width=30, height=2,command=record_form).place(x=700, y=300)
    Button(text="Trained Dataset", fg="purple", font=("Bold", 20), bg="white", width=30, height=2,command=traindata).place(x=700, y=400)
    Button(text="Recognized", fg="purple", font=("Bold", 20), bg="white", width=30, height=2, command=recognized).place(x=700, y=500)
    Button(text="Exit", fg="purple", font=("Bold", 20), bg="white", width=30, height=2, command=destroyexit).place(x=700,y=600)
    # Button(text="Create Table",command=table).place(x=50,y=200)
    maindatasetscreen.mainloop()

def main_screen():
    global mainscreen
    mainscreen=Tk()
    mainscreen.configure(background="purple")
    mainscreen.title("Criminal Data Record")
    # mainscreen.geometry('1500x900+200+100')
    mainscreen.attributes('-fullscreen', True)
    mainscreen.resizable(width = 200, height = 200)
    label=Label(mainscreen,text="WELCOME \n AUTOMATED CRIMINAL DETECTION SYSTEM",anchor=CENTER,fg="white",bg="purple",font=("Bold",15)).pack()
    img = Image.open("acds.png")
    img = img.resize((300, 250), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    # create a label
    panel = Label(mainscreen, image = img,bg="purple",anchor=CENTER).place(x=150,y=300)
    label_0=Label(mainscreen,text="Main Screen",width=20,font=("Bold",20),fg="white",bg="purple",anchor=CENTER).place(x=800,y=150)
    label = Label(mainscreen,text="Please Click on Login Button if You Are not Registered Then Click on Registration Button",fg="white", bg="purple").place(x=730,y=200)
    Button(mainscreen, text="Login", width=30, height=2, bg="white", fg="purple",command=login).place(x=850, y=300)
    Button(mainscreen, text="Register", width=30, height=2, bg="white", fg="purple",command=register).place(x=850,y=400)
    mainscreen.mainloop()
main_screen()
