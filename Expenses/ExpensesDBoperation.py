from database import create_connection

def add_expenses():
   con = create_connection()
   cursor = con.cursor()

   print(" Available Users ")
   cursor.execute("SELECT * FROM users")

   for row in cursor.fetchall():
       print(row)

   print(" Available Category ")
   cursor.execute("SELECT * FROM Category")

   for row in cursor.fetchall():
       print(row)

   user_id:int = int(input("Enter User id: "))
   Category_id:int = int(input("Enter Category id: "))
   amount:int = int(input("Enter Amount: "))

   cursor.execute("INSERT INTO Expenses (user_id,category_id,amount) VALUES(%s,%s,%s)" ,(user_id,Category_id,amount))

   con.commit()
   con.close()

def search_expenses_by_user_and_category():
    con = create_connection()
    cursor = con.cursor()

    userName = input("Enter User Name: ")
    categoryName = input("Enter Category Name: ")
    
    quary ='''SELECT 
    u.name,
    c.Category_name,
    e.amount
    from Expenses as e
    INNER join users u
    ON e.user_id = u.user_id
    INNER join Category c
    ON e.Category_id = c.Category_id
    WHERE u.name = %s AND c.category_name = %s'''

    cursor.execute(quary,(userName,categoryName))
    expenses = cursor.fetchall()

    if expenses:
        for expenses in expenses:
         print(expenses)
    else:
         print("No recode found. ")
    
    con.close()










   



