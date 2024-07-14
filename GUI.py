import sys
import tkinter as tk
from pathlib import Path
from tkinter import ttk
import mariadb

# 데이터베이스 생성
def create_database(cur, db_name):
    try:
        sql = 'CREATE DATABASE IF NOT EXISTS ' + db_name + ';'
        cur.execute(sql)
    
    except mariadb.Error as e:
        print(e)
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
        print(e)
        sys.exit(1)

# 데이터베이스 선택
def choice_database(cur, db_name):
    try:
        sql = 'USE ' + db_name + ';'
        cur.execute(sql)

    except mariadb.Error as e:
        print(e)
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
        print(e)
        sys.exit(1)

# 테이블 삭제
def delete_table(cur, table_name):
    try:
        sql = 'DELETE TABLE IF EXISTS ' + table_name +';'
        cur.execute(sql)

    except mariadb.Error as e:
        print(e)
        sys.exit(1)
    
    

# 테이블 값 입력
def insert_value(cur, table_name, attribute ,value):
    try:
        sql = 'INSERT INTO ' + table_name +  '(' + attribute + ') ' + 'VALUES' + '(' + value + ')' +';'
        
        cur.execute(sql)

    except mariadb.Error as e:
        print(e)
        sys.exit(1)

# 테이블 값 삭제
def delete_value(cur, table_name, attribute , condition):
    try:
        sql = 'DELETE FROM ' + table_name +  'WHERE' + condition +';'
        cur.execute(sql)

    except mariadb.Error as e:
        print(e)
        sys.exit(1)

# 데이터 변경
def update_value(cur, table_name, condition ,attribute, value):
    try:
        sql = 'UPDATE INTO ' + table_name + 'SET ' + attribute + ' = ' + value + 'WHERE' + condition + ';'
        cur.execute(sql)

    except mariadb.Error as e:
        print(e)
        sys.exit(1)

# 데이터 조회
def select_value(cur, table_name):
    try:
        sql = 'SELECT * FROM ' + table_name + ';'
        cur.execute(sql)

    except mariadb.Error as e:
        print(e)
        sys.exit(1)
    
    rows = [row for row in cur.fetchall()]
    
    return rows
    

# 테이블 columns값 읽기
def view_columns(cur, table_name):

    cur.execute(('SHOW COLUMNS FROM ' + table_name))
    dbs = [db[0] for db in cur.fetchall()]
    return dbs




# 기능 1번 버튼에 대한 함수
def func_1():

    def func_1_add():
          
        at = view_columns(cur, 'test')
        att = ""
        
        for _ in at:
            att += _ + ', '
        
        att = att[:-2]

        value = entry1.get() + ', ' + '\'' + entry2.get() + '\'' + ', ' + entry3.get() + ', ' + '\'' + entry4.get() + '\'' + ', ' + '\'' + entry5.get() + '\'' + ', ' + '\'' +entry6.get() + '\'' 

        insert_value(cur, 'test', att, value)

    subwindow = tk.Toplevel()

    subwindow.geometry('400x400')
    
    tk.Label(subwindow, text="Test_Number",padx=20, pady=20).grid(row=0, column=0)
    entry1 = tk.Entry(subwindow)
    entry1.grid(row=0, column=1)

    tk.Label(subwindow, text="Test_conductor",padx=20, pady=20).grid(row=1, column=0)
    entry2 = tk.Entry(subwindow)
    entry2.grid(row=1, column=1)

    tk.Label(subwindow, text="Mode_frequency",padx=20, pady=20).grid(row=2, column=0)
    entry3 = tk.Entry(subwindow)
    entry3.grid(row=2, column=1)

    tk.Label(subwindow, text="Model_Number",padx=20, pady=20).grid(row=3, column=0)
    entry4 = tk.Entry(subwindow)
    entry4.grid(row=3, column=1)

    tk.Label(subwindow, text="Test_shape",padx=20, pady=20).grid(row=4, column=0)
    entry5 = tk.Entry(subwindow)
    entry5.grid(row=4, column=1)

    tk.Label(subwindow, text="Sensor_id",padx=20, pady=20).grid(row=5, column=0)
    entry6 = tk.Entry(subwindow)
    entry6.grid(row=5, column=1)
    
    button1 = tk.Button(subwindow, text="추가", command=func_1_add)
    button1.grid(row=6,column=1)




if __name__ == '__main__':
    
    window = tk.Tk()

    dict_db = {}

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

    # root 프레임 설정
    window.geometry('1000x800')

    tree_frame = tk.Frame(window)

    # 프레임 선언
    frame1 = tk.Frame(tree_frame, width=200, height=400, relief='solid')
    frame2 = tk.Frame(tree_frame, width=600, height=400, relief='solid')
    frame3 = tk.Frame(window, width=1000, height= 100, relief='solid')
    frame4 = tk.Frame(window, width=1000, height= 300, relief='solid')

    # 테이블 목록을 보여주는 프레임을 새로 갱신하기 위한 변수 설정
    sub_frame_list = []

    def OndoubleClick(event):
        
        # 더블 클릭된 아이템
        item = tree.selection()[0]

        # 더블클릭한 item이 테이블인 경우
        if iid_table_list[item] in total_table_lsit:
            
            # 테이블 중첩하는 경우 삭제
            if len(sub_frame_list) >= 1:
                sub_frame_list[0].destroy()
                sub_frame_list.pop(0)

            # 사용할 DB 설정
            use_db = db_table_list[iid_table_list[item]]
            choice_database(cur, use_db)

            # 해당 테이블에 열 이름
            col = view_columns(cur, iid_table_list[item])

            tree2 = ttk.Treeview(frame2, columns=tuple(col), show='headings')

            for j in col:
                tree2.heading(j, text=j)

            # 열에 맞는 데이터 목록화
            rows = select_value(cur, iid_table_list[item])
            print(rows)
            for k in rows:
                print(k)
                tree2.insert("", tk.END, values=k)

            # 화면에 commit
            tree2.pack()

            sub_frame_list.append(tree2)
            print(sub_frame_list)
    

    tree = ttk.Treeview(frame1, show='tree')

    # 전체 테이블 목록
    total_table_lsit = []

    # 데이터베이스 - 테이블 매핑
    db_table_list = {}

    # iid값 - 테이블 매핑 (iid값에 알맞은 데이터 추출을 위해)
    iid_table_list = {}

    # 데이터베이스 리스트
    db_list = view_database(cur)

    # iid값 기본 설정 
    iid = 0

    # 데이터베이스 리스트 가시화
    for _ in db_list:
        item = tree.insert("", tk.END, text = _, iid=iid)
        iid += 1
        choice_database(cur, _)
        table_lsit = view_tables(cur)
        for i in table_lsit:
            db_table_list[i] = _
            subitem = tree.insert(item, tk.END, text = i, iid=iid) 
            iid_table_list[str(iid)] = i
            total_table_lsit.append(i)
            iid += 1

    # 더블클릭 이벤트 리스너
    tree.bind("<Double-1>", OndoubleClick)

    tree.pack()

    b1 = tk.Button(frame3, text='기능1', command=func_1)
    b2 = tk.Button(frame3, text='기능2')
    b3 = tk.Button(frame3, text='기능3')
    b4 = tk.Button(frame3, text='기능4')
    b5 = tk.Button(frame3, text='기능5')

    b1.grid(row=0, column=0, padx= 20)
    b2.grid(row=0, column=1, padx= 20)
    b3.grid(row=0, column=2, padx= 20)
    b4.grid(row=0, column=3, padx= 20)
    b5.grid(row=0, column=4, padx= 20)


    frame1.grid(row=0, column=0)
    frame2.grid(row=0,column=1)
    tree_frame.grid(row=0, column=0)
    frame3.grid(row=1, column=0)
    frame4.grid(row=2, column=0)

    window.mainloop()

    conn.commit()
    cur.close()
    conn.close()
