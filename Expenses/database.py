import MySQLdb

def create_connection() -> MySQLdb.Connection:
    return MySQLdb.connect(
        host = "localhost",
        user ="root",
        password ="Mysql@123",
        database = "my_first_db"
        )