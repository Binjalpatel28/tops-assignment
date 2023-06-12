
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)
cursor = mydb.cursor()
cursor.execute("use bank_database")



#create a table of banker 

# cursor.execute("""CREATE TABLE banker(
#     id INT PRIMARY KEY AUTO_INCREMENT,
#     name VARCHAR(50) NOT NULL,
#     email VARCHAR(50) NOT NULL UNIQUE,
#     password VARCHAR(50) NOT NULL,
#     balance FLOAT NOT NULL
# )""")


# create a table of customer 

# cursor.execute("""CREATE TABLE customer(
#     id INT PRIMARY KEY AUTO_INCREMENT,
#     name VARCHAR(50) NOT NULL,
#     email VARCHAR(50) NOT NULL UNIQUE,
#     password VARCHAR(50) NOT NULL,
#     balance FLOAT NOT NULL
# )""")

#create a table of account


# cursor.execute("""CREATE TABLE account_details(
#     id INT PRIMARY KEY AUTO_INCREMENT,
#     name VARCHAR(50) NOT NULL,
#     type VARCHAR(50) NOT NULL UNIQUE,
#     balance FLOAT NOT NULL,
#     user int,
#     FOREIGN KEY (user) REFERENCES banker(id)
# )""")


# cursor.execute("""INSERT INTO banker (name, email, password, balance)
#     VALUES ('Binjal', 'binjalpatel16@gmail.com', '123', 70.000)""")



def showbanker():
    print("banker")
    print("1) Register")
    print("2) login")
    print("3) Update all customers")
    print("4) view all customers")
    print("5) delete all customers")
    choice_banker=int(input("Enter Your Choice:"))
    if choice_banker==1:
        register()
    elif choice_banker==2:
        login()
    elif choice_banker==3:
        update_customer()
    elif choice_banker==4:
        viewall()
    elif choice_banker==5:
        delete_customer()
    else:
        print("Wrong choice")

def showcustomer():
    print("customer")
    print("1) Register")
    print("2) login")
    print("3) withdraw amount")
    print("4) deposite amount")
    print("5) view balance")
    choice_customer=int(input("Enter Your Choice:"))
    if choice_customer==1:
        registercustomer()
    elif choice_customer==2:
        logincustomer()
    elif choice_customer==3:
        withdraw_amount()
    elif choice_customer==4:
        deposite()
    elif choice_customer==5:
        viewbalance()
    else:
        print("Wrong choice")


def register():
    print("Registration of Banker")
    name=input("Enter name:")
    email=input("Enter email:")
    password=input("Enter password:")
    balance=input("Enter balance:")
    # adddata={}
    # adddata.update({'name':name,'email':email,'password':password,'balance':balance})
    # maindata.update({name:adddata})
    insert(name,email,password,balance)

def insert(*data):
    print({data[0]},{data[1]},{data[2]},{data[3]})
    # cursor.execute(f"insert into banker(name,email,password,balance) values({data[0]},{data[1]},{data[2]},{data[3]})")
    query = "INSERT INTO banker(name,email,password,balance) values (%s, %s, %s,%s)"
    data1 = (data[0],data[1],data[2],data[3])
    cursor.execute(query, data1)
    mydb.commit()
    print("values Inserted")

def login():
    print("Banker Login")
    uname=input("Enter Username: ")
    pwd=input("Enter Password: ")
    query="select * from banker where email=%s and password=%s"
    cursor.execute(query,(uname,pwd))
    result=cursor.fetchone()
    mydb.commit()
    if result is not None:
        print("Login successful!")
    # Perform other actions or queries here
    else:
        print("Login failed.")


def update_customer():
    print("Update All customers")
    new_id=input("Enter ID: ")
    check_query = "SELECT name,email FROM customer WHERE id = %s"
    cursor.execute(check_query,(new_id,))
   
    result=cursor.fetchone()
    if result is None:
        print("Customer not found.")
        cursor.close()
        cnx.close()
        exit()
    existing_name, existing_email = result
    update_query = "UPDATE customer SET name = %s, email= %s WHERE  id = %s"
    new_name=input("Enter new name:")
    new_email=input("Enter new Email:")
    cursor.execute(update_query, (new_name, new_email, new_id ))
    print("name and email is succesfully updated")
    mydb.commit()
    

def viewall():
    #data view query
    print("View all Customers")
    view_query="select * from customer"
    cursor.execute(view_query)
    rows = cursor.fetchall()
    headings = [desc[0] for desc in cursor.description]
    formatted_headings = ' | '.join(headings)
    print(formatted_headings)

    # Display a line separator
    separator = '-' * (len(formatted_headings) + 3 * len(headings) - 1)
    print(separator)
    #data view 
    for row in rows:
        format_data=' | '.join(str(item) for item in row)
        print(format_data)
    print(separator)

def delete_customer():
    print("delete customers")
    email=input("Enter the email that you want to delete:")
    delete_query="delete from customer where email= %s "
    cursor.execute(delete_query,(email,))
    print("deleted succesfully")
    mydb.commit()


def registercustomer():
    print("Registration of Customer")
    name=input("Enter name:")
    email=input("Enter email:")
    password=input("Enter password:")
    balance=input("Enter balance:")
    # adddata={}
    # adddata.update({'name':name,'email':email,'password':password,'balance':balance})
    # maindata.update({name:adddata})
    insertcustomer(name,email,password,balance)

def insertcustomer(*data):
    print({data[0]},{data[1]},{data[2]},{data[3]})
    # cursor.execute(f"insert into banker(name,email,password,balance) values({data[0]},{data[1]},{data[2]},{data[3]})")
    cursor.execute("use bank_database")
    query = "INSERT INTO customer(name,email,password,balance) values (%s, %s, %s,%s)"
    data1 = (data[0],data[1],data[2],data[3])
    cursor.execute(query, data1)
    mydb.commit()
    print("values Inserted")

def logincustomer():
    print("customer Login")
    uname=input("Enter Username: ")
    pwd=input("Enter Password: ")
    cursor.execute("use bank_database")
    query="select * from customer where email=%s and password=%s"
    cursor.execute(query,(uname,pwd))
    result=cursor.fetchone()
    mydb.commit()
    if result is not None:
        print("Login successful!")
    # Perform other actions or queries here
    else:
        print("Login failed.")

def withdraw_amount():

    print("Withdraw Amount")
    email=input("Enter the Email: ")
    withdrawal_amount=float(input("Enter the Amount: "))
    #retrive the balance 
    query="select * from customer where email= %s"
    cursor.execute(query,(email,))
    result=cursor.fetchone()
    # print(result)
    if result is None:
        print("Customer not found.")
        cursor.close()
        mydb.close()
        exit()

    current_balance =  float(result[4])  # Assuming the balance column is in the third position

    if withdrawal_amount > current_balance:
        print("Insufficient balance.")
        cursor.close()
        mydb.close()
        exit()

    new_balance = float(current_balance) - float(withdrawal_amount)

    update_query = "UPDATE customer SET balance = %s WHERE email = %s"
    cursor.execute(update_query, (new_balance, email,))
    print("balance updated")
    mydb.commit()


def deposite():
    print("Deposite amount")
    email=input("Enter the Email: ")
    deposit_amount=float(input("Enter the Amount: "))
    #retrive the balance 
    query="select * from customer where email= %s"
    cursor.execute(query,(email,))
    result=cursor.fetchone()
    # print(result)
    if result is None:
        print("Customer not found.")
        cursor.close()
        mydb.close()
        exit()
    # balance position 
    current_balance =  float(result[4]) 

    
    if deposit_amount < 0:
        print("Deposit amount cannot be negative.")
        cursor.close()
        mydb.close()
        exit()

    new_balance = float(current_balance) + float(deposit_amount)

    update_query = "UPDATE customer SET balance = %s WHERE email = %s"
    cursor.execute(update_query, (new_balance, email,))
    print("deposite amount updated")
    mydb.commit()
    print()

def viewbalance():
#data view query
    print("View all Customers balance")
    view_query="select name,balance from customer"
    cursor.execute(view_query)
    rows = cursor.fetchall()
    headings = [desc[0] for desc in cursor.description]
    formatted_headings = ' | '.join(headings)
    print(formatted_headings)

# Display a line separator
    separator = '-' * (len(formatted_headings) + 3 * len(headings) - 1)
    print(separator)

#data view 
    for row in rows:
        format_data=' | '.join(str(item) for item in row)
        print(format_data)
    print(separator)


   
