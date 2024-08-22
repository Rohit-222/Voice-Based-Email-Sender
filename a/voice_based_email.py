import speech_recognition as sr
from tkinter import *
import tkinter as tk
import os
import smtplib
import pyttsx3
import pyaudio
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()
# speech to text and text to speech

# function for registation
def register() :
    global register_screen
    register_screen = Toplevel ( main_screen )
    register_screen.title ( "Register" )
    register_screen.geometry ( "600x650" )

    global username
    global password
    global email
    global age
    global gender
    global username_entry
    global password_entry
    global email_entry
    global age_entry
    global gender_entry

    username = StringVar ( )
    password = StringVar ( )
    email = StringVar ( )
    age = StringVar ( )
    gender = StringVar ( )

    Label ( register_screen, text="Please enter registration details below", font=('bold',20, 'bold'),
            fg="black", bg='white' ).pack ( )
    Label ( register_screen, text="" ).pack ( )
    talk('please registatre yourself ')

    username_lable = Label ( register_screen, text="Username", font=("Goudy old style", 20, "bold"),
                             fg='orangered', bg='white' )
    username_lable.pack ( )

    username_entry = Entry ( register_screen, textvariable=username, font=("times new roman", 15, "bold"),
                             bg='lightgray' )
    username_entry.pack ( )

    password_lable = Label ( register_screen, text="Password", font=("Goudy old style", 20, "bold"),
                             fg='orangered', bg='white' )
    password_lable.pack ( )
    password_entry = Entry ( register_screen, textvariable=password, show='*', font=("times new roman", 15, "bold"),
                             bg='lightgray' )
    password_entry.pack ( )
    Label ( register_screen, text="**please enter your email password**" ).pack ( )
    Label ( register_screen, text="" ).pack ( )

    email_lable = Label ( register_screen, text="Email", font=("Goudy old style", 20, "bold"),
                          fg='orangered', bg='white' )
    email_lable.pack ( )
    email_entry = Entry ( register_screen, textvariable=email, font=("times new roman", 15, "bold"),
                          bg='lightgray' )
    email_entry.pack ( )
    Label ( register_screen, text="**please enter correct email id**" ).pack ( )
    Label ( register_screen, text="" ).pack ( )

    age_lable = Label ( register_screen, text="Age", font=("Goudy old style", 20, "bold"),
                        fg='orangered', bg='white' )
    age_lable.pack ( )
    age_entry = Entry ( register_screen, textvariable=age, font=("times new roman", 15, "bold"),
                        bg='lightgray' )
    age_entry.pack ( )

    gender_lable = Label ( register_screen, text="Gender", font=("Goudy old style", 20, "bold"),
                           fg='orangered', bg='white' )
    gender_lable.pack ( )
    gender_entry = Entry ( register_screen, textvariable=gender, font=("times new roman", 15, "bold"),
                           bg='lightgray' )
    gender_entry.pack ( )

    Label ( register_screen, text="" ).pack ( )
    Button ( register_screen, text="Register", command=register_user, font=("times new roman", 15), fg="white",
             bg="orangered", bd=0, width=10, height=1 ).pack ( )



# Designing window for login
def login() :
    global login_screen
    login_screen = Toplevel ( main_screen )
    login_screen.title ( "Login" )
    login_screen.geometry ( "650x400" )
    Label ( login_screen, text="Please enter login details below to login", font=('blod', 20, 'bold'),
            fg="black" ).pack ( )
    Label ( login_screen, text="" ).pack ( )
    talk ( 'for using this application please do login ' )
    global username_verify
    global password_verify

    username_verify = StringVar ( )
    password_verify = StringVar ( )

    global username_login_entry
    global password_login_entry

    Label ( login_screen, text="Username", font=("Goudy old style", 20, "bold"),
            fg='orangered', bg='white' ).pack ( )
    username_login_entry = Entry ( login_screen, textvariable=username_verify, font=("times new roman", 15, "bold"),
                                   bg='lightgray' )
    username_login_entry.pack ( )
    Label ( login_screen, text="" ).pack ( )
    Label ( login_screen, text="Password", font=("Goudy old style", 20, "bold"),
            fg='orangered', bg='white' ).pack ( )
    password_login_entry = Entry ( login_screen, textvariable=password_verify, show='*',
                                   font=("times new roman", 15, "bold"),
                                   bg='lightgray' )
    password_login_entry.pack ( )
    Label ( login_screen, text="" ).pack ( )
    Button ( login_screen, text="Login", command=login_verify, font=("times new roman", 15), fg="white", bg="orangered",
             bd=0, width=10, height=1 ).pack ( )
    # Button ( login_screen, text="main page", width=10, height=1, command=main_page_screen ).pack ( )


#file handling concept
# Implementing event on register button
def register_user() :
    username_info = username.get ( )
    password_info = password.get ( )
    email_info = email.get ( )
    age_info = age.get ( )
    gender_info = gender.get ( )

    file = open ( username_info, "w" )
    file.write ( username_info + "\n" )
    file.write ( password_info + "\n" )
    file.write ( age_info + "\n" )
    file.write ( email_info + "\n" )
    file.write ( gender_info )

    file.close ( )

    username_entry.delete ( 0, END )
    password_entry.delete ( 0, END )
    talk('Registation sucessfully')
    Label ( register_screen, text="Registration Success", fg="green", font=("calibri bold", 11) ).pack ( )


# Implementing event on login button
#login varification process
def login_verify() :
    global sender
    global password
    username1 = username_verify.get ( )
    password1 = password_verify.get ( )
    username_login_entry.delete ( 0, END )
    password_login_entry.delete ( 0, END )

    list_of_files = os.listdir ( )
    if username1 in list_of_files :
        file1 = open ( username1, "r" )
        verify = file1.read ( ).splitlines ( )
        if password1 in verify :
            sender = verify[3]
            password = verify[1]
            login_sucess ( )
            email_page ( )
        else :
            password_not_recognised ( )


    else :
        user_not_found ( )
        talk ( 'user not found' )


# Designing popup for login success
#pop msg
def login_sucess() :
    global login_success_screen
    login_success_screen = Toplevel ( login_screen )
    login_success_screen.title ( "Success" )
    login_success_screen.geometry ( "250x150" )
    talk('login sucessful')
    Label ( login_success_screen, text="Login Success", font=("arial black", 20), fg="green" ).pack ( )
    #Label ( login_success_screen, text=sender, fg="green", font=("calibri bold", 11) ).pack ( )
    #Label ( login_success_screen, text=password, fg="green", font=("calibri bold", 11) ).pack ( )
    Button ( login_success_screen, text="OK", command=delete_login_success, fg="green" ).pack ( )



#main system starts from here
# main page
def email_page() :
    global email_screen
    email_screen = Tk ( )
    email_screen.title ( "****** Email Main Menu *******" )
    email_screen.geometry ( '550x700' )

    email_screen['bg'] = 'gray38'

    f = ("Times bold", 14)
    Label ( email_screen, text="Email virtual assistant", bg="gold1", width="350", height="5",
            font=("bold", 20, "bold") ).pack ( )
    Label ( email_screen, text="Select Your Choice", width="25", height=3, font=("arial black", 15) ).pack ( )
    Label ( email_screen, text="" ).pack ( )
    Button ( email_screen, text="Favourite contact list", font=("arial black", 12), height="2", width="20",command=fav_contanct ).pack ( )
    Label ( email_screen, text="" ).pack ( )
    Button ( email_screen, text="Send Mail", font=("arial black", 12), height="1", width="20" , command=send_now).pack ( )
    Label ( email_screen, text="" ).pack ( )
    Button ( email_screen, text="HELP", font=("arial black", 12), height="1", width="20", command=help_page ).pack ( )
    Label ( email_screen, text="" ).pack ( )
    Button ( email_screen, text="Logout", font=("arial black", 12), height="1", width="20",command=exit_app ).pack ( )
    Label ( email_screen, text="" ).pack ( )




#option1 fav contcat list
def fav_contanct() :
    global fav_contanct_screen
    fav_contanct_screen= Tk ( )
    fav_contanct_screen.title ( "****** fav contact *******" )
    fav_contanct_screen.geometry ( '550x700' )
    fav_contanct_screen['bg'] = 'gray38'

    #fav_contanct = StringVar ( )
    f = ("Times bold", 14)
    Label ( fav_contanct_screen, text="Create Favourite Email ID", bg="gold1", width="350", height="5",
            font=("bold", 20, "bold") ).pack ( )
    talk('Create your favorite contact list')
    def printValue() :
        pname = playe_name.get ( )
        Label (  fav_contanct_screen, text="" ).pack ( )
        Label ( fav_contanct_screen, text=f'{pname}, CREATEED', pady=10, bg='#ffbf00' ).pack ( )

    playe_name = Entry ( fav_contanct_screen )
    playe_name.pack ( pady=10 )
    # Label ( fav_contanct_screen, text="Pelase enter your favourte email id and their nicknames",
          #  font=("Calibri", 13) ).pack ( )
    Button (
        fav_contanct_screen,
        text="ADD",
        padx=10,
        pady=10,
        command=printValue
    ).pack ( )

    fav_contanct_screen.mainloop ( )




#main email sending process

def send_now():
    os.system ( 'python voice_basic_imp.py' ) #commented on 05/07/20201
    #get_email_info ( )



#window for help center
def help_page():
    global help_screen
    help_screen = Tk ( )
    help_screen.title ( "****** Email Main Menu *******" )
    help_screen.geometry ( '400x300' )

    help_screen['bg'] = '#ffbf00'
    f = ("Times bold", 14)
    Label (help_screen, text="Help center", bg="grey", width="400", height="5",
            font=("Calibri", 13) ).pack ( )
    talk ( 'how can i help you? ' )
    Label ( help_screen, text="FOR ANY QUERY CONTACT OUR TOLL FREE NUMBER : +1234567890", font=("Calibri", 13) ).pack ( )
    Label ( help_screen, text="" ).pack ( )
    Label ( help_screen, text="OUR EMAIL ID : emailvirtualassistantdeveloper@gmail.com", font=("Calibri", 13) ).pack ( )
    Label ( help_screen, text="" ).pack ( )




#log out here crated separate window for this but we dont add that
def logout_page():
    global logout_screen
    logout_screen = Tk ( )
    logout_screen.title ( "****** logout *******" )
    logout_screen.geometry ( '400x300' )
    logout_screen['bg'] = '#ffbf00'
    f = ("Times bold", 14)
    Button ( logout_screen, text="Do You Want To Exit?", font=("arial black", 12), height="1", width="20",command=exit_app ).pack ( )
    Label ( logout_screen, text="" ).pack ( )

#log out app
def exit_app():
      email_screen.destroy ()




#for closing all the screens
# Designing popup for login invalid password
# Designing popup for user not found

def user_not_found() :
    global user_not_found_screen
    user_not_found_screen = Toplevel ( login_screen )
    user_not_found_screen.title ( "Success" )
    user_not_found_screen.geometry ( "150x100" )
    talk('User not found please varify your email id or password')
    Label ( user_not_found_screen, text="User Not Found", font=("times new roman", 15), fg="white", bg="orangered",
            bd=0, width=15, height=1 ).pack ( )
    Button ( user_not_found_screen, text="OK", command=delete_user_not_found_screen ).pack ( )


# Deleting screens

def delete_login_success() :
    login_success_screen.destroy ( )
    login_screen.destroy ( )
    main_screen.destroy ( )


def delete_password_not_recognised() :
    password_not_recog_screen.destroy ( )


def delete_user_not_found_screen() :
    user_not_found_screen.destroy ( )


def main_page_screen() :
    main_page_screen.destroy ( )

#main window
# Designing Main(first) window
def main_account_screen() :
    global main_screen
    main_screen = Tk ( )
    main_screen.title ( "Account Login" )
    main_screen.geometry ( '450x600' )

    main_screen['bg'] = 'gray38'
    main_screen.state ( 'zoomed' )
    f = ("Times bold", 14)
    Label ( text="Email virtual assistant", bg="gold1",width="400", height="5",
            font=("bold", 20, "bold") ).pack ( )
    Label ( text="Select Your Choice",width="30", height=3,font=("arial black", 13) ).pack ( )
    Label ( text="" ).pack ( )
    Button ( text="Login", height="1", width="20", font=("arial black", 13), command=login ).pack ( )
    Label ( text="" ).pack ( )
    Button ( text="Register", height="1", width="20", font=("arial black", 13), command=register ).pack ( )
    talk ( 'Hello user .........welcome to email virtual assistant.........' )

    main_screen.mainloop ( )











#email sending code
def rec():
    r = sr.Recognizer()
    #msg.configure(text="Say something")
    while True:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        try:
            txt = r.recognize_google(audio)
            #msg.configure(text=txt)
            return(txt)
        except Exception as e:
            print(e)
            break

def get_info():
    try:
        print("I am waiting for you to say something....")
        info =rec()
        print(info)
        send_now_screen.destroy ( )
        return info.lower()
    except:
        talk ( "sorry we cant here you" )

def send_email(receiver, subject ,message):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    #sender=sys.argv[1]
    #password=sys.argv[2]


    #enter your email and passwoord

    # Program to check input
    # type in Python
    sender = input ( "Enter sender email id" )
    print ( sender )
    password = input ( "Enter password :" )
    print ( password )
    # Printing type of input value
    print ( "sender" )
    print ( " password " )

    server.login(sender, password)
    email = EmailMessage()
    email['From']= sender
    email['To']= receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


email_list ={

        'apurva': 'ak@gmail.com'

    }

# Function to convert text to speech
def talk(text1) :
    # Initialize the engine
    engine = pyttsx3.init ( )
    engine.say (text1 )
    engine.runAndWait ( )

# Loop infinitely for user to
# speak

def get_email_info():
    #global send_now_screen
    #send_now_screen = Tk ( )
    #send_now_screen.title ( "****** voice email sending *******" )
    #send_now_screen.geometry ( '100x100' )
    #send_now_screen['bg'] = '#ffbf00'

    talk ( 'hello user ............'

           )
    print( 'hello user ............'
           'i am email virtual assistant .......'
           ' how can i help you?? do you want to send email?? '
           'follow the instructions for sending email...................'
           'Warning : please make sure that you turn on email access to this application'
           )

    talk ( ' welcome to the email bot ..........' )
    print( ' welcome to the email bot ..........' )

    talk('To Whom you want to send email')
    #Label ( send_now_screen, text='To Whom you want to send email' ).pack ( )
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    #Label ( send_now_screen, text=receiver ).pack ( )
    talk('What is the subject of your email?')
    #Label ( send_now_screen, text='What is the subject of your email?' ).pack ( )
    subject = get_info()
    #Label ( send_now_screen, text=subject ).pack ( )
    talk('Tell me the text in your email')
    #Label ( send_now_screen, text='Tell me the text in your email' ).pack ( )
    message = get_info()
    #Label ( send_now_screen, text= message ).pack ( )
    send_email(receiver, subject, message)
    talk('Your email is sent')
    talk('Do you want to send more email?')
    send_more = get_info()
    if 'yes' in send_more:
            get_email_info()



main_account_screen ( )