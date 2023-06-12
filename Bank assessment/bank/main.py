import maindata

def showboth():
    print("1) Banker details")
    print("2) customer details")
    choice_type=int(input("Enter Your Choice:"))
    if choice_type==1:
        maindata.showbanker()
    elif choice_type==2:
        maindata.showcustomer()
    else:
        print("Invalid choice")
showboth()