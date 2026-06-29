import MySQLdb

def create_connection() -> MySQLdb.Connection:
    return MySQLdb.connect(
        host = "localhost",
        user ="root",
        password ="Your_password",
        database = "Your_Database"
        )

def create_tables():
    con : MySQLdb.Connection = create_connection()
    cursor : MySQLdb.cursors.Cursor = con.cursor()

    cursor.execute(''' 
                   create table users (
                      user_id INT PRIMARY KEY AUTO_INCREMENT ,
                      name varchar(12),
                      address varchar(20)
                     )
                      ''')
    
    cursor.execute(''' 
                   create table Category(
                      category_id INT PRIMARY KEY AUTO_INCREMENT,
                      category_name varchar(15)
                   )
                   ''')
    
    cursor.execute('''
                   create table Expenses (
                        expenses_id INT PRIMARY KEY AUTO_INCREMENT,
                        user_id INT,
                        category_id INT,
                        foreign key (user_id) REFERENCES users(user_id) ,
                        foreign key (category_id) REFERENCES Category(category_id) ,
                        amount INT
                   )
                   ''')
    
    con.commit()
    con.close()


