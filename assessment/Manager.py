stock={}

def show_manager_menu():
    print("Fruit Market Manager")
    print("1) Add Fruit stock")
    print("2) View Fruit stock")
    print("3) Update Fruit stock")

    choice_manager=int(input("Enter Your Choice:"))
    if choice_manager==1:
        add_fruit()
        repeat()
    elif choice_manager==2:
        view_fruit()
    elif choice_manager==3:
        update_fruit()
    else:
        print("Invalid Choice")

def repeat():
    rc=input("Do You want to perform more operation: press 'Y' for yes And press 'N' for No:" )
    if(rc=='y' or rc=='Y'):
        show_manager_menu()
    elif(rc=='n' or rc=='N'):
        print("******************************Thanks For Using**********************************")

def add_fruit():
    print("ADD FRUIT STOCK")
    fruit_name=input("Enter Fruit Name:")
    qty=int(input("Enter qty(in kg):"))
    price=int(input("Enter Price(for kg):"))
    demo={}
    demo.update({'qty':qty, 'price':price})
    stock.update({fruit_name:demo})


def view_fruit():
    print(stock)

def update_fruit():
    fruit_name=input("Which fruit you want to update:")
    temp=stock.get(fruit_name)
    if temp==None:
        print("Not Exists")
        update_fruit()
    uc=int(input("What you want to update:n1)price\n2)quantity"))
    if uc==1:
        n_price=int(input("enter New price:"))
        temp.update({'price':n_price})
        stock.update({fruit_name:temp})
        repeat()
    elif uc==2:
        n_qty=int(input("enter New Quantity:"))
        temp.update({'qty':n_qty})
        stock.update({fruit_name:temp})
        repeat()
    else:
        print("Invalid Choice")
        repeat()


