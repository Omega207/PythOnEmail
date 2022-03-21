from tkinter import *
import smtplib

#Main Screen
master = Tk()
master.title('PythOnEmail')

#Functions
def send():
    try:
        username = temp_username.get()
        password = temp_password.get()
        to = temp_receiver.get()
        subject = temp_subject.get()
        body = temp_body.get()
        if username=="" or password=="" or to=="" or subject=="" or body=="":
            notif.config(text="All fields required", fg="red")
            return
        else:
            finalMessage = 'Subject: {]\n\n{}'.format(subject, body)
            server = smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login(username, password)
            server.sendmail(username,to,finalMessage)
            notif.config(text="Email has been sent successfully", fg="green")
    except:
        notif.config(text="Error sending email. Please try again", fg="red")
def reset():
    usernameEntry.delete(0, 'end')
    passwordEntry.delete(0, 'end')
    receiverEntry.delete(0, 'end')
    subjectEntry.delete(0, 'end')
    subjectBody.delete(0, 'end')

#Graphics
Label(master, text="Welcome to PythOnEmail, where you can freely send emails to your friends and family.", font=('Ubuntu',15)).grid(row=0, sticky=N)
Label(master, text="Use the forum below to send an email.", font=('Ubuntu',11)).grid(row=1, sticky=W, padx=5)


Label(master, text="Email", font=('Arial Rounded MT Bold',11)).grid(row=2, sticky=W, padx=5)
Label(master, text="Password", font=('Arial Rounded MT Bold',11)).grid(row=3, sticky=W, padx=5)
Label(master, text="To", font=('Arial Rounded MT Bold',11)).grid(row=4, sticky=W, padx=5)
Label(master, text="Subject", font=('Arial Rounded MT Bold',11)).grid(row=5, sticky=W, padx=5)
Label(master, text="Body", font=('Arial Rounded MT Bold',11)).grid(row=6, sticky=W, padx=5)


notif = Label(master, text="", font=('Arial Rounded MT Bold',11)).grid(row=7, sticky=S, padx=5)

#Storage
temp_username = StringVar()
temp_password = StringVar()
temp_receiver = StringVar()
temp_subject = StringVar()
temp_body = StringVar()

#Entries
usernameEntry = Entry(master, textvariable=temp_username)
usernameEntry.grid(row=2,column=0)
passwordEntry = Entry(master, show="*", textvariable=temp_password)
passwordEntry.grid(row=3,column=0)
receiverEntry = Entry(master, textvariable=temp_receiver)
receiverEntry.grid(row=4,column=0)
subjectEntry = Entry(master, textvariable=temp_subject)
subjectEntry.grid(row=5,column=0)
subjectBody = Entry(master, textvariable=temp_body)
subjectBody.grid(row=6,column=0)

#Buttons
Button(master, text="Send", command=send).grid(row=7, sticky=W, pady=15, padx=5)
Button(master, text="Reset", command=reset).grid(row=7, sticky=W, pady=45, padx=45)

master.mainloop()
