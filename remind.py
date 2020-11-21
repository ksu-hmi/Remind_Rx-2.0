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



