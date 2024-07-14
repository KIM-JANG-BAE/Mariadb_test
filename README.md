# Mariadb_test

![ERD](https://github.com/KIM-JANG-BAE/Mariadb_test/assets/100831121/0d34e4ed-c43f-45e8-be5c-d4cd17228e9f)

### CREATE, DROP, SHOW
* CREATE : 데이터베이스 생성
* DROP : 데이터베이스 삭제
* SHOW : 데이터베이스 목록 보기



예시)

1. CREATE DATABASE [IF NOT EXISTS] 'DataBase_Name';
- [IF NOT EXISTS] : 데이터베이스가 존재하지 않는다면
- 'DataBase_Name' : 생성할 데이터베이스 이름


2. DROP DATABASE [IF EXISTS] 'DataBase_Name';
- [IF EXISTS] : 데이터베이스가 존재한다면
- 'DataBase_Name' : 삭제할 데이터베이스 이름


3. SHOW DATABASES;

<br>

1. CREATE TABLE [IF NOT EXISTS] 'Table_Name';
- [IF NOT EXISTS] : 테이블이 존재하지 않는다면
- 'Table_Name' : 생성할 테이블 이름


2. DROP TABLE [IF EXISTS] 'DataBase_Name';
- [IF EXISTS] : 테이블이 존재한다면
- 'Table_Name' : 삭제할 테이블 이름

<br>

### INSERT, SELECT, DELETE, UPDATE

* INSERT : 테이블에 데이터 삽입
* SELECT : 테이블 데이터 조회
* DELETE : 테이블 데이터 삭제
* UPDATE : 테이블 데이터 변경


예시)

1. INSERT INTO 'Table_Name'(col1, col2, col3) VALUES (val1, val2, val3);
- 'Table_Name' : 테이블 이름
- (col1, col2, col3) : 데이터를 삽입할 테이블의 피처
- (val1, val2, val3) : 각 피처에 알맞은 데이터

2. DELETE FROM 'Table_Name' WHERE condition;
- 'Table_Name' : 테이블 이름
- condition : 조건문  ex) Name = '김장배'

3. UPDATE 'Table_Name' SET col = value WHERE condition;
- 'Table_Name' : 테이블 이름
- col : 변경할 피처
- value : 변경될 값
- condition : 조건문 ex) ID = 100000

4. SELECT * FROM 'Table_Name' WHERE condition;
- \* : 모든 요소
- 'Table_Name' : 테이블 이름
- condition : 조건문

#GUI

![image](https://github.com/user-attachments/assets/8e4939a3-06bd-480c-a6db-d52f6b798d4a)

![image](https://github.com/user-attachments/assets/a8f2bd9c-62d8-4fb6-9db6-a0e593f395aa)





