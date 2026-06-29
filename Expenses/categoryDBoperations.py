import MySQLdb
from database import create_connection

def insert_category():
    name = input("Enter Category : ")
    
    try:
        con = create_connection()
        cursor = con.cursor()

        cursor.execute("INSERT INTO Category(category_name) VALUES (%s)",(name,))
        
        con.commit()
        con.close()

        print("Category inserted successfully!")

    except MySQLdb.IntegrityError:
         print("Error: while Inserting details")

def view_category():
     con = create_connection()
     cursor = con.cursor()

     cursor.execute("SELECT * FROM  Category")

     category = cursor.fetchall()

     con.close()

     if category:
        print("\n--- Category List ---")
        for category in category:
         print(category)
     else:
         print("No recode found. ")

    
