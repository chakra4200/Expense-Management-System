import MySQLdb
from database import create_connection

def insert_user():
    name = input("Enter the name: ")
    address = input("Enter Address: ")

    try:
        con = create_connection()
        cursor = con.cursor()

        cursor.execute("INSERT INTO users(name,address) VALUES (%s,%s)",(name,address))
        
        con.commit()
        con.close()

        print("User inserted successfully!")

    except MySQLdb.IntegrityError:
         print("Error: while Inserting details")

def view_users():
     con = create_connection()
     cursor = con.cursor()

     cursor.execute("SELECT * FROM users")

     user = cursor.fetchall()

     con.close()

     if user:
        print("\n--- Users List ---")
        for user in user:
         print(user)
     else:
         print("No users recode found. ")

def search_user():
    con = create_connection()
    cursor = con.cursor()

    name = input("Enter the name: ")

    cursor.execute("SELECT * FROM users WHERE name = %s",(name,))
    user = cursor.fetchall()

    if user:
        for user in user:
         print(user)
    else:
         print("No users recode found. ")
    
    con.close()







    


