import sys
import signal
import time
import os
import webbrowser

# Log into the app
print("Please enter your username and password to access the application\n You have 3 attempts or application quits")

attempts = 0

username = "medication"
password = "T1mer"

while True:
    usern = input("Enter Username: ")
    print()
    userp = input("Enter Password: ")
    attempts += 1
    if attempts == 3:
        print("Too many incorrect attempts. Please try again in few minutes")
        exit()
    else:
        if usern == username and userp == password:
            print("\nAccess Granted. Welcome " + username)
            break
        else:
            print("\nIncorrect credentials. Try again")
            
print ("Welcome to RemindRx!")

print("Enter your first name: ")
first_name=input()
print("Enter your last name: ")
last_name=input()
full_name=(first_name  + " " + last_name )

print(full_name)

print("Hello", first_name,"!", "Enter name of medication :")
medication_name=input()

print(medication_name)

print("Enter the directions for medication : ")
med_direction = input()

print(med_direction)

print("Enter time of day medication is to be taken : ") #need input format for the time so end user will know how to enter it!
time_take=input()
print(time_take)
print(time_take,med_direction)



#Importing all the necessary libraries to form the alarm clock:
from tkinter import *
import datetime
import time
import winsound

def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print("The Set Date is:",date)
        print(now)
        if now == set_alarm_timer:
            print("Time to Wake up")
        winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
        break
def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)
    
   
# Create GUI in tinker
clock = Tk()
clock.title("DataFlair Alarm Clock")
clock.geometry("400x200")
time_format=Label(clock, text= "Enter time in 24 hour format!", fg="red",bg="black",font="Arial").place(x=60,y=120)
addTime = Label(clock,text = "Hour  Min   Sec",font=60).place(x = 110)
setYourAlarm = Label(clock,text = "When to wake you up",fg="blue",relief = "solid",font=("Helevetica",7,"bold")).place(x=0, y=29)
# The Variables we require to set the alarm(initialization):
hour = StringVar()
min = StringVar()
sec = StringVar()
#Time required to set the alarm clock:
hourTime= Entry(clock,textvariable = hour,bg = "pink",width = 15).place(x=110,y=30)
minTime= Entry(clock,textvariable = min,bg = "pink",width = 15).place(x=150,y=30)
secTime = Entry(clock,textvariable = sec,bg = "pink",width = 15).place(x=200,y=30)
#To take the time input by user:
submit = Button(clock,text = "Set Alarm",fg="red",width = 10,command = actual_time).place(x =110,y=70)
clock.mainloop()
#Execution of the window.
python3 DataFlair-Alarm-Clock.py
