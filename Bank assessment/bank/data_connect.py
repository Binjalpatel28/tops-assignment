import maindata 
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)
cursor = mydb.cursor()
cursor.execute("use bank_database")



