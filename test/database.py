import mysql.connector

class Database():
    # def __init__(self):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Nelldestroyer25",
        database="salon"
    )
    cursor = conn.cursor()