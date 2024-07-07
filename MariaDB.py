import mariadb
import tkinter as tk
import sys

# 데이터베이스 생성
def create_database(cur, db_name):
    try:
        sql = 'CREATE DATABASE IF NOT EXISTS ' + db_name + ';'
        cur.execute(sql)
    
    except mariadb.Error as e:
        sys.exit(1)

# 데이터베이스 목록 확인 
def view_database(cur):

    cur.execute('SHOW databases;')
    dbs = [db[0] for db in cur.fetchall()]
    return dbs

# 데이터베이스 삭제
def delete_database(cur, db_name):
    try:
        sql = 'DROP DATABASE ' + db_name + ';'
        cur.execute(sql)

    except mariadb.OperationalError as e:
        sys.exit(1)

# 데이터베이스 선택
def choice_database(cur, db_name):
    try:
        sql = 'USE ' + db_name + ';'
        cur.execute(sql)

    except mariadb.Error as e:
        sys.exit(1)

# 테이블 목록 확인 
def view_tables(cur):

    cur.execute('SHOW TABLES;')
    tbs = [db[0] for db in cur.fetchall()]
    return tbs

# 테이블 생성
def create_table(cur, table_name, attribute):
    try:
        sql = 'CREATE TABLE IF NOT EXISTS ' + table_name +  '(' + attribute + ')' + ';'
        cur.execute(sql)

    except mariadb.Error as e:
        sys.exit(1)

# 테이블 삭제
def delete_table(cur, table_name):
    try:
        sql = 'DELETE TABLE IF EXISTS ' + table_name +';'
        cur.execute(sql)

    except mariadb.Error as e:
        sys.exit(1)

# 테이블 값 입력
def insert_value(cur, table_name, attribute ,value):
    try:
        sql = 'INSERT INTO ' + table_name +  '(' + attribute + ')' + 'VALUES' + '(' + value + ')' +';'
        cur.execute(sql)

    except mariadb.Error as e:
        sys.exit(1)

def update_value(cur, table_name, condition ,attribute, value):
    try:
        sql = 'UPDATE INTO ' + table_name + 'SET ' + attribute + ' = ' + value + 'WHERE' + condition + ';'
        cur.execute(sql)

    except mariadb.Error as e:
        sys.exit(1)

# 테이블 columns값 읽기
def view_columns(cur, table_name):

    cur.execute(('SHOW COLUMNS FROM ' + table_name))
    dbs = [db[0] for db in cur.fetchall()]
    return dbs


if __name__ == '__main__':
    
    # Mariadb server와 연결
    try:
        conn = mariadb.connect(
            host='192.168.0.8',
            user = 'root',
            password = 'rldjrgo123*',
            port = 3306)
        
    except mariadb.Error as e:
        sys.exit(1)

    # 명령어 실행 권한 획득
    cur = conn.cursor()

    # (1) mariadb_test라는 데이터베이스명을 가진 데이터베이스 생성
    create_database(cur, 'MariaDB_Test')
    print(view_database(cur))

    # (2) mariadb_test라는 데이터베이스명을 가진 데이터베이스 삭제
    delete_database(cur, 'MariaDB_Test')
    print(view_database(cur))

    # (1) 실행 
    create_database(cur, 'MariaDB_Test')

    # (3) mariadb_test 데이터베이스 사용
    choice_database(cur, 'MariaDB_Test')

    # (4) 요소 선정 후, Mariadb_test 데이터베이스 안, Test라는 이름의 테이블로 생성 
    attribute = 'Test_Number INT NOT NULL PRIMARY KEY, Test_conductor varchar(20), Mode_frequency FLOAT, Model_Number varchar(20), Test_shape varchar(20), Sensor_id varchar(20)'
    create_table(cur, 'Test', attribute)
    print(view_tables(cur))
    print(view_columns(cur, 'test'))

    # (4) Table : Shape
    attribute = 'Shape_Number varchar(20) NOT NULL PRIMARY KEY, Model varchar(20), Shape_feature varchar(30)'
    create_table(cur, 'Shape', attribute)

    # (4) Table : Aircraft
    attribute = 'Model varchar(20) NOT NULL PRIMARY KEY, Nickname varchar(20), Model_Number varchar(20)'
    create_table(cur, 'Aircraft', attribute)

    # (4) Table : Mode
    attribute = 'Test_Number INT NOT NULL PRIMARY KEY, Mode_1_frequency flaot, Mode_2_frequency flaot, Mode_3_frequency flaot'
    create_table(cur, 'Mode', attribute)
    
    # (4) Table : Sensor
    attribute = 'Sensor_id varchar(20) NOT NULL PRIMARY KEY, Sensor_type varchar(20), Sensor_dir varchar(10)'
    create_table(cur, 'Sensor', attribute)

    window = tk.Tk()
    window.mainloop()