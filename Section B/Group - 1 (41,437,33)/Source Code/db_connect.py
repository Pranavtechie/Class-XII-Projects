import mysql.connector as sql

def est_conn():
    conn = sql.connect(host = 'localhost', user = 'root', password = 'student', database = 'shopie')
    cursor = conn.cursor()

    return conn, cursor
