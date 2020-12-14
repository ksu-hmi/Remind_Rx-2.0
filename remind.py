#Importing all the necessary libraries:
from tkinter import *
import datetime
import time
import sys
import signal
import os
import webbrowser
import time


# Log into the app
print ("RemindRx")

print("Enter Email address: ")
create_username=input()
print("Create Password: ")
create_password=input()
print("Enter your first name: ")
first_name=input()
print("Enter your last name: ")
last_name=input()
print("Enter your phone number: ")
phone_number=input()
full_name=(first_name  + " " + last_name )


print("Welcome", first_name + "!", "Your profile is set up")
print("Log in to access the application\n You have 3 attempts or application quits")

attempts = 0

username = create_username
password = create_password

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
            print("\nAccess Granted. Welcome " + first_name)
            break
        else:
            print("\nIncorrect credentials. Try again")
            


def print_menu():
    print()
    print("Welcome to RemindRx! Press enter to select option")
    print()

    choice = input("""
            1. Add A Medication
            2. Delete A Medication
            3. Review Your Medication List
            4. Set an Alarm for Medication
            5. Exit
            """)

print_menu()


choice = input("Select the menu item that you want edit [1-5]: ")
choice = int(choice)
medication_name=[]

while choice != 5:
    if choice == 1:
        print ("Add A Medication")
        med_add = input("Enter the medication Name to add to your list: ")
        medication_name.append(med_add)
        print("Updated Medication List: ", medication_name) 
        print("Enter the directions for medication : ")
        med_direction = input()
        
    elif choice == 2:
        print ("Delete A Medication")
        med_remove = input("Enter the medication that you are removing from your list: ")   
        medication_name.remove(med_remove)
        print("Updated medication list: ", medication_name)
        continue
    elif choice == 3:
        print ("Review Your Medication List")
        print("Current medication list: ", "\n", medication_name)
        
    elif choice == 4:
        print ("Set an Alarm for Medication")

        alarm_HH = input("Enter the hour you want to take the medication - in 24 hour format: ")
        alarm_MM = input("Enter the minute you want to take the medication: ")

print("Hello", first_name,"!", "Enter name of medication :")
medication_name=input()

print(medication_name)

print("Enter the directions for medication : ")
med_direction = input()

print(med_direction)
#need input format for the time so end user will know how to enter it!
print("Enter time of day medication is to be taken : ") 
time_take=input('Please input the time for the alarm in format HHMM: \n ')
print(time_take)
print("Hello", first_name,"!", "Remember to take", med_direction, "at", time_take)

def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print("The Set Date is:",date)
        print(now)
        if now == set_alarm_timer:
            print("Time to take med")
        winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
        break
def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)
    
   
# Create GUI in tinker
clock = Tk()
clock.title("RemindRx")
clock.geometry("400x200")
time_format=Label(clock, text= "Enter time in 24 hour format!", fg="red",bg="black",font="Arial").place(x=60,y=120)
addTime = Label(clock,text = "Hour  Min   Sec",font=60).place(x = 110)
setYourAlarm = Label(clock,text = "Remember to take your med",fg="blue",relief = "solid",font=("Helevetica",7,"bold")).place(x=0, y=29)
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