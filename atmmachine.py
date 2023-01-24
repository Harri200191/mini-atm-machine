import winsound
from win32com.client import Dispatch

speak = Dispatch("SAPI.SpVoice").Speak

PINsList =[]
namelist = []

def new_customer_setup():
    name = input("Enter your name = ")
    namelist.append(name)
    PIN = input("Enter your 4 digit PIN = ")
    while len(PIN)!= 4:
        winsound.Beep(440, 500)
        print("Must be 4 digits. Try again.")
        PIN = input("Enter your 4 digit PIN = ")
    
    TempPin = input("Enter your PIN again to verify = ")
    while TempPin != PIN:
        winsound.Beep(440, 500)
        print("PIN's do not match. Try again.")
        TempPin = input("Enter your PIN again to verify. If you forgot your PIN, enter 'YES' = ")
        if TempPin == "YES":
            winsound.Beep(440, 500)
            print("Your proccess will repeat now!")
            new_customer_setup()
    print("PIN matched! Added to database")
    PINsList.append(PIN)
            
def old_customer_setup():
    winsound.Beep(440, 500)
    print("Welcome!")
    Checkpin = input("Enter your 4 digit pin = ")
    
    count=0
    flag2 = False
    
    while count<=4 and flag2 == False:
        for x in PINsList:
            if Checkpin == x:
                flag2 = True
                index = PINsList.index(x)
            else:
                flag2 = False
        count = count+1
        if flag2 == False:
            winsound.Beep(440, 500)
            print("No match found. Try again!")
            Checkpin = input("Enter your 4 digit pin = ")
            
    if flag2 == False:
        winsound.Beep(440, 500)
        print("You excceded the 4 allowed tries. Try again in some time!")
    else:
        winsound.Beep(440, 500)
        savedname = namelist[index]

        speak("Welcome to HBL! We hope you have a great experience!")
        money = int(input("Enter the amount of money you want to withdraw = "))
        while money<500 or money >100000:
            winsound.Beep(440, 500)
            print("You must take at least 500 and at most 100000 rupees. Try again")
            money = int(input("Enter the amount of money you want to withdraw = "))
    
flag = True 
while flag == True:
    winsound.Beep(440, 500)
    print("DEAR CUSTOMER. WELCOME TO HBL ATM MACHINE!")
    print("Are you a new customer or an existing one?")
    choice = int(input("Press 1 if new and 0 if existing ="))
    
    while choice!= 0 and choice !=1:
        winsound.Beep(440, 500)
        print("You need to enter 1 and 0 only. Try again.")
        choice = int(input("Press 1 if new and 0 if existing ="))
      
    
    if choice == 1:
        
        new_customer_setup()
    else:
        old_customer_setup()
        
    winsound.Beep(440, 500)
    print("THANK YOU FOR USING HBL.")
    
    choiceend = int(input("PRESS 1 IF YOU WANT TO REPEAT AND 0 IF YOU WANT TO END = "))
    
    while choiceend!= 0 and choiceend !=1:
        winsound.Beep(440, 500)
        print("You need to enter 1 and 0 only. Try again.")
        choiceend = int(input("PRESS 1 IF YOU WANT TO REPEAT AND 0 IF YOU WANT TO END = "))
    if choiceend == 0:
        flag = False
        
winsound.Beep(440, 500) 
winsound.Beep(440, 500)
winsound.Beep(440, 500)
winsound.Beep(440, 500)
winsound.Beep(440, 500)
winsound.Beep(440, 500)
winsound.Beep(440, 500)
winsound.Beep(440, 500)
