import sys
import signal
import time
import os
import webbrowser

# Since this is patient information, you must log into the application
print("You must enter your username and password to access the application\n You have 3 attempts or application quits")

attempts = 0

username = "medication"
password = "T1mer"

while True:
    usern = input("Enter Username: ")
    print()
    userp = input("Enter Password: ")
    attempts += 1
    if attempts == 3:
        print("Too many incorrect attempts. Goodbye")
        exit()
    else:
        if usern == username and userp == password:
            print("\nAccess Granted. Welcome " + username)
            break
        else:
            print("\nIncorrect credentials. Try again")
            
print ("Welcome to RemindRx!")

print("Enter your firstname: ")
firstname=input()
print("Enter your lastname: ")
lastname=input()
fullname=(firstname  + " " + lastname )

print(fullname)

print("Enter name of medication :")
medication_name=input()

print(medication_name)

print("Enter the directions for medication : ")
med_direction = input()

print(med_direction)

print("Enter time of day medication is to be taken : ") #need input format for the time so end user will know how to enter it!
time_take=input()
print(time_take)



