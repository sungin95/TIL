# Database

참고: 파이썬 뿐 아니라 sql도 테스트를 보는 곳이 많다. 

- 데이터베이스는 체계회된 데이터의 모임
- 여러 사람이 공유하고 사용할 목적으로 통합 관리되는 정보의 집합
- 논리적이로 연관된 (하나 이상의) 자료의 모음으로 

​		그 내용을 고도로 구조화 함으로써 검색과 갱신의 효율화를 꾀한 것

- 즉, 몇 개의 자료 파일을 조직적으로 통합하여

​		자료 항목의 중복을 없애고 자료를 구조화하여 기억시켜 놓은 자료의 집합체

## 데이터베이스로 얻는 장점들

- 데이터 중복 최소화
- 데이터 무결성 (정확한 정보를 보장)
- 데이터 일관성
- 데이터 독립성(물리적/논리적)
- 데이터 표준화
- 데이터 보안 유지

(공감안감. 공부하고 나면 이해하게 됨)

# RDB

## 관계형 데이터베이스(RDB, Relational Database)

서로 관련된 데이터를 저장하고 접근할 수 있는 데이터베이스 유형

키(Key)와 값(value)들의 간단한 관계(relation)를 표(table) 형태로 정리한 데이터베이스 

| 고유번호 | 이름   | 주소 | 나이 |
| -------- | ------ | ---- | ---- |
| 1        | 홍길동 | 제주 | 20   |
| 2        | 김길종 | 서울 | 30   |
| 3        | 박길동 | 독도 | 40   |

## 스키마

지식을 표상하는 구조

데이터베이스에서 자료의 구조, 표현방법, 관계등 전반적인 명세를 기술한 것

| column  | datatype |
| ------- | -------- |
| id      | INT      |
| name    | TEXT     |
| address | TEXT     |
| age     | INT      |

## 테이블

열(컬럼/필드)과 행(레코드/값)의 모델을 사용해 조직된 데이터 요소들의 집합



기본키(Primary Key): 각 행(레코드)의 고유 값

반드시 설정해야 하며, 데이터베이스 관리 및 관계 설정 시 주요하게 활용 됨

절대 중복이 발생하지 않는 고유한 값(주민등록번호, 학번)



# SQLite

서버 형태가 아닌 파일 형식으로 응용 프로그램에 넣어서 사용하는 비교적 가벼운 데이터베이스

구글 안드로이드 운영체제에 기본적으로 탑재된 데이터베이스이며, 임베디드 소프트웨어에도 많이 활용됨

로컬에서 간단한 DB 구성을 할 수 있으며, 오픈소스 프로젝트이기 때문에 자유롭게 사용가능 

### type

1. NULL
2. INTEGER
   - 크기에 따라 0, 1, 2, 3, 4, 6 또는 8바이트에 저장된 부호 있는 정수 
3. REAL
   - 8바이트 부동 소수점 숫자로 저장된 부동 소수점 값
4. TEXT
5. BLOB
   - 입력된 그대로 정확히 저장된 데이터 (별다른 타입 없이 그대로 저장)
6. NUMERIC



# SQL(구조화된 쿼리(질문화된) 언어)

(Structured Query Language)

- 관계형 데이터베이스 관리시스템의 데이터 관리를 위해 설계된 특수 목적으로 프로그래밍 언어
- 데이터베이스 스키마 생성 및 수정
- 자료의 검색 및 관리
- 데이터베이스 객체 접근 조정 관리

분류

| DDL - 데이터 정의 언어<br />(Data Defntion Language) | 개념                                                         | 예시                                        |
| ---------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------- |
| DML - 데이터 조작 언어                               | 관계형 데이터베이스 구조(테이블, 스키마)를 정의하기 위한 명령어 | CREATE<br />DROP<br />ALTER                 |
| (Data Manipulaton Language)                          | 데이터를 저장, 조회, 수정, 삭제 등을 하기 위한 명령어        | INSERT<br />SELLECT<br />UPDATE<br />DELETE |
| DCL - 데이터 제어 언어<br />(Data Control anguage)   | 데이터베이스 사용자의 권한 제어를 위해 사용하는 명령어       | GRANT<br />REVOKE<br />COMMT<br />ROLLBACK  |

## SQL Keywords - Data Manipulation Language 

INSERT : 새로운 데이터 삽입(추가)

SELECT : 저장되어있는 데이터 조회

UPDATE : 저장되어있는 데이터 갱신

DELETE : 저장되어있는 데이터 삭제

#  Helllo World!(기본 명령어)

```sqlite
sqlite3 tutorial.sqlite3
-- 데이터베이스 생성하기
sqlte> .database
-- csv 파일을 table로 만들기
sqlte> .mode csv
sqlte> .import hellodb.csv examples
sqlte> .tablles
-- SELLECT
SELECT * FROM examples;
sqlte> .headers on
sqlte> .mode column
sqlte> SELECT * FROM examples;
1,"길동","홍",600,"충청도",010-0000-0000
```

(Optional 터미널 view 변경하기)

```python
sqlte> SELECT * FROM examples;
1,"길동","홍",600,"충청도",010-0000-0000

sqlte> .headers on 
sqlte> SELECT * FROM examples;
id,first_name,last_name,age,country,phone
1,"길동","홍",600,"충청도",010-0000-0000

sqlte> .mode column
sqlte> SELECT * FROM examples;
id   first_name   last_name   age   country   phone

1    길동          홍          600    충청도    010-0000-0000
```



SELECT 문은 특정 테이블의 레코드(행) 정보를 반환

필드제약조건



INSERT INTO classmates (name, age) VALUES ('홍길동', 23);

```
$ sqlite3 tutorial.sqlite3
.database
.import hellodb.csv examples
SELECT * FROM examples;
=> 1,길동,홍,600,충청도,010-0000-0000
```



```
환경설정
sql
https://hphk-edu.notion.site/SQLite-62e2a6ee8e4f40fa97b2acbfbd74bd6a
파일 2개 다운로드
해당 파일을 환경변수에 경로 저장
winpty sqlite3 커맨드를 sqlite3로 변경하기
1. code ~/.bashrc
2. alias sqlite3="wiinpty sqlite3"
3. source ~/.bashrc
.quit

.sqlite3  임시환경을 만든다. 
.sqlite3 healthcare.sqlte3 새로운 영구적인 파일을 만든다. 
database가 없으면 여기는 vscode환경이라는 것을 기억하자. 이걸 도와주는 환경이 안깔려 있는 거다. 
.csv형식은 database에서 해당형식으로 옮긴것이다? 아직 무슨 말인지 잘 모르겠다. 
```





```sqlite
-- classmates라는 이름의 테이블 생성
CREATE TABLE classmates (
    id INTEGER PRIMARY KEY, 
    name TEXT
);
CREATE TABLE classmates (
    name TEXT NOT NULL,
    age INT NOT NULL,
    address TEXT NOT NULL
);
CREATE TABLE members(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);
.database
.import hellodb.csv examples
.headers on 
.mode column
.schema healthcare
-- 데이터를 추가
.mode csv

-- 같은 디렉토리에 있는 users.csv 파일을 users 테이블로
.import users.csv users

-- 테이블 목록 조회
.tables

-- 특정 테이블 스키마 조회
.schema classmates

-- 값 추가
INSERT INTO classmates VALUES (1, '조세호');
INSERT INTO classmates (name, age) VALUES ('홍길동', 23);
INSERT INTO classmates (name, age, address) VALUES ('홍길동', 23, '서울');
INSERT INTO classmates VALUES 
('홍길동', 30, '서울'), 
('김철수', 30, '제주'),
('이호영', 26, '인천'),
('박민희', 29, '대구'),
('최혜영', 28, '전주');
INSERT INTO classmates VALUES ('주세환', 40, '대전'); 
INSERT INTO members VALUES 
(10, '홍길동'), 
(11, '김철수'),
(12, '이호영'),
(15, '박민희'),
(18, '최혜영');

-- 테이블 조회
SELECT * FROM classmates;
SELECT rowid, * FROM classmates;
SELECT rowid, name FROM classmates;
SELECT rowid, name FROM classmates LIMIT 2;
SELECT rowid, name FROM classmates LIMIT 1 OFFSET 2;
SELECT * FROM classmates WHERE address='서울';
SELECT name FROM classmates WHERE age >= 30;
SELECT DISTINCT age FROM classmates;
SELECT rowid, * FROM classmates;
SELECT rowid, name FROM classmates LIMIT 100;

-- 삭제 
DELETE FROM classmates WHERE rowid=5;
DELETE FROM members WHERE rowid=5;

-- 수정
UPDATE classmates SET name='홍길동', address='제주도' WHERE rowid=5;

-- 테이블 삭제
DROP TABLE classmates;


SELECT weight*10000/(height*height) AS BMI, weight, height FROM healthcare LIMIT 5;



```



|      |  구문  |                             예시                             |
| :--: | :----: | :----------------------------------------------------------: |
|  C   | INSERT | INSERT INTO 테이블이름 (컬럼1, 컬럼2, ...) VALUES (값1, 값2); |
|  R   | SELECT |             SELECT * FROM 테이블이름 WHERE 조건;             |
|  U   | UPDATE |    UPDATE 테이블이름 SET 컬럼1=값, 컬럼2=값2 WHERE 조건;     |
|  D   | DELETE |              DELETE FROM 테이블이름 WHERE 조건;              |



```sqlite
-- SQLite

-- 테이블 생성
-- 정호,유,40,전라북도,016-7280-2855,370
CREATE TABLE users (
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL,
    country TEXT NOT NULL,
    phone TEXT NOT NULL,
    balance INTEGER NOT NULL
);

-- 데이터를 추가
.mode csv
-- 같은 디렉토리에 있는 users.csv 파일을 users 테이블로
.import users.csv users


-- 쿼리

-- 30세 이상인 사람들
SELECT * FROM users WHERE age >= 30;
-- 30세 이상인 사람들의 이름
SELECT first_name FROM users WHERE age >= 30;
-- 30세 이상인 사람들의 이름 3명만
SELECT first_name FROM users WHERE age >= 30 LIMIT 3;
-- 30세 이상이고 성이 김인 사람
SELECT age, first_name FROM users WHERE age >= 30 AND last_name = '김';

-- 30세 이상인 사람들의 숫자
SELECT COUNT(*) FROM users WHERE age >= 30;
-- 전체 중에 가장 작은 나이
SELECT MIN(age) FROM users;
-- 이씨 중에 가장 작은 나이
SELECT MIN(age) FROM users WHERE last_name = '이';
-- 이씨 중에 가장 작은 나이를 가진 사람의 이름과 계좌잔고
SELECT MIN(age), first_name, balance FROM users WHERE last_name = '이';
-- 30세 이상인 사람들의 평균 나이
SELECT AVG(age) FROM users WHERE age >= 30;
-- 계좌 잔액이 가장 높은 사람
SELECT MAX(balance), first_name FROM users;

-- 지역번호가 02인 사람
SELECT COUNT(*) FROM users WHERE phone LIKE '02-%';
-- 준으로 끝나는 사람
SELECT COUNT(*) FROM users WHERE first_name LIKE '%준';
-- 중간번호가 5114
SELECT COUNT(*) FROM users WHERE phone LIKE '%-5114-%';

-- 나이 오름차순 
SELECT first_name FROM users ORDER BY age ASC LIMIT 10;
-- 나이, 성 순으로 오름차순
SELECT * FROM users ORDER BY age, last_name LIMIT 10;
-- 계좌 잔액 순 내림차순 
SELECT last_name, first_name, balance FROM users ORDER BY balance DESC LIMIT 10;
-- 계좌 잔액 내림차순(높은->낮은 것), 성 오름차순(ㄱ->ㅎ)
SELECT last_name, first_name, balance FROM users ORDER BY balance DESC, last_name ASC LIMIT 10;

SELECT * FROM healthcare WHERE is_drinking = 1 ORDER BY waist ASC LIMIT 5;
```









