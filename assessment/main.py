import Manager
import Customer
def start():

    print('''Welcome to Fruit Market
                1)Manager
                2)Customer
                ''')

    role=int(input("Select your choice:"))
    if role==1:
        Manager.show_manager_menu()
    elif role==2:
        pass
    else:
        print("Invalid Role choice")
start()
    