import random
from time import sleep

class booking_acc():
    def __init__(self,username,password):
        self.username = username
        self.password = password

created_acc = [booking_acc("ram","1234")]
loginaccount = None

while True:
    print("1.Create Account\n""2.Login")
    select_opt = int(input("Select an option : "))
    print()
    if select_opt==1:
        username = input("Create a username : ")
        password = input("Create a password : ")
        created_acc.append(booking_acc(username,password))
        if username == "" and password == "":
            print("Enter details to create account")
        else:    
            print(f"{username} your account is created successfully")
    elif select_opt==2:
        username = input("Enter a username : ")
        password = input("Enter a password : ")
        for acc in created_acc:
            if acc.username == username and acc.password == password:
                loginaccount = acc
                print(f"{username} you are logged in")
                break
        if loginaccount is None:
            print("Invalid Details")        
        else:
            print("Book your ticket")
            break        
    else:
        print("Enter valid details")         
  
  
print("-------------------------------------")
print("TRAINS AVAILABLE : ") 

class train_details:
    def __init__(self,trains_run_no,trains_name,trains_from_to,avail_ticket):
        self.trains_run_no = trains_run_no
        self.trains_name = trains_name
        self.trains_from_to = trains_from_to
        self.avail_ticket = avail_ticket

    def display_avail_trains(self):
        for i,j in zip(trains_run_no,trains_from_to):
            print(f"{trains_run_no.index(i)+1})",i,j)
            

    def selecta_train(self):
        while True:
            select_train = int(input("Select your train : "))
            if select_train >= 1 and select_train <= len(trains_run_no):
                index_value = select_train - 1
                print("TRAIN NO :",trains_run_no[index_value],
                      "\nTRAIN NAME:",trains_name[index_value],
                      "\nARRIVAL: ",trains_from_to[index_value],
                      " :DEPT","\nAvailable : ",avail_ticket[index_value])
                return select_train
            else:
                print("Invalid train selection")


    def ticket_confirm(self,selecta_train):
        while True:
            pnr_no = random.randint(1000000000,9999999999)
            confirmation = input("To Book your Ticket\nType y or n : ")

            if confirmation.lower() == "y":
                pass_name = input("Enter your Name : ")
                pass_age = int(input("Enter your age : "))
                print("Checking................")
                sleep(2)
                print()
                print("-------------RAIL BOOKING-------------")
                    
                select_train = selecta_train-1
                print(f"PNR NO. : {pnr_no}")
                print(trains_name[select_train],"TRAIN NO :",
                    trains_run_no[select_train],
                    f"\npassenger name:{pass_name}",
                    f"\npassenger age:{pass_age}",
                    "\nARRIVAL:---------------",trains_from_to[select_train],"---------------:DEPT")
                print("YOUR TICKET WAS CONFIRMED","\nHAPPY JOURNEY")
                break

            else:
                print("Ticket not booked")
                    

trains_run_no = ["07644", "12864", "18464", "22502", "12602", "17230"]
trains_name = ["Hyderabad Special Fare", "Howrah SF Express", "Prasanti Express", "New Delhi Rajdhani", "Chennai Mail", "Sabari Express"]
trains_from_to = ["TPTY - HYD", "TPTY - VSKP", "BZA - BHU", "NDLS - BCT", "MAS - MS", "HYB - CBE"]
avail_ticket = [90,150,85,72,26,104]


train_info = train_details(trains_run_no, trains_name, trains_from_to, avail_ticket)
train_info.display_avail_trains()
train_info.ticket_confirm(train_info.selecta_train())