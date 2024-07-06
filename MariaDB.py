import mariadb
import tkinter as tk
import sys

def create_database(cur, db_name):
    try:
        sql = 'CREATE DATABASE IF NOT EXISTS ' + db_name + ';'
        cur.execute(sql)
    
    except mariadb.Error as e:
        sys.exit(1)
    
def view_database(cur):

    cur.execute('SHOW databases;')
    dbs = [db[0] for db in cur.fetchall()]
    return dbs

def delete_database(cur, db_name):
    try:
        sql = 'DROP DATABASE ' + db_name + ';'
        cur.execute(sql)

    except mariadb.OperationalError as e:
        sys.exit(1)

def choice_database(cur, db_name):
    try:
        sql = 'USE ' + db_name + ';'
        cur.execute(sql)

    except mariadb.Error as e:
        sys.exit(1)

def create_table(cur, table_name, attribute):
    try:
        sql = 'CREATE TABLE IF NOT EXISTS ' + table_name +  '(' + attribute + ')' + ';'
        cur.execute(sql)

    except mariadb.Error as e:
        sys.exit(1)



if __name__ == '__main__':
    
    try:
        conn = mariadb.connect(
            host='192.168.0.8',
            user = 'root',
            password = 'rldjrgo123*',
            port = 3306)
    except mariadb.Error as e:
        sys.exit(1)

    cur = conn.cursor()

    window = tk.Tk()
    window.mainloop()







