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


!= NOT <>
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



# 01_hello.sql

```sqlite
-- SQLite
-- classmates라는 이름의 테이블 생성
CREATE TABLE classmates (
    id INTEGER PRIMARY KEY, 
    name TEXT
);

-- 테이블 목록 조회
.tables

-- 특정 테이블 스키마 조회
.schema classmates

-- 값 추가
INSERT INTO classmates VALUES (1, '조세호');

-- 테이블 조회
SELECT * FROM classmates;

INSERT INTO classmates VALUES (2, '이동희');

-- 테이블 삭제
DROP TABLE classmates;
```

# 02_classmates.sql

```sqlite
-- classmates
-- name : TEXT
-- age : INT
-- address : TEXT 

CREATE TABLE classmates (
    name TEXT,
    age INT,
    address TEXT
);

-- CREATE TABLE students(
-- id INTEGER PRIMARY KEY,
-- name TEXT NOT NULL,
-- age INTEGER DEFAULT 1 CHECK (0 < age)
-- );

-- CREATE
-- INSERT INTO classmates VALUES ('홍길동', 23);
-- Parse error: table classmates has 3 columns but 2 values were supplied
INSERT INTO classmates (name, age) VALUES ('홍길동', 23);
SELECT * FROM classmates;
INSERT INTO classmates (name, age, address) VALUES ('홍길동', 23, '서울');
INSERT INTO classmates VALUES ('김철수', 40, '서울');

SELECT rowid, * FROM classmates;
-- rowid는 SQLite에서 자동으로 제공하고 있는 PK. 값이 1씩 증가하는 모습을 보임.
-- rowid  name  age  address
-- -----  ----  ---  -------
-- 1      홍길동   23
-- 2      홍길동   23   서울
-- 3      김철수   40   서울

DROP TABLE classmates;
```

# 03_classmates.sql

```sqlite
CREATE TABLE classmates (
    name TEXT NOT NULL,
    age INT NOT NULL,
    address TEXT NOT NULL
);

INSERT INTO classmates VALUES 
('홍길동', 30, '서울'), 
('김철수', 30, '제주'),
('이호영', 26, '인천'),
('박민희', 29, '대구'),
('최혜영', 28, '전주');

SELECT * FROM classmates;
-- name  age  address
-- ----  ---  -------
-- 홍길동   30   서울
-- 김철수   30   제주
-- 이호영   26   인천
-- 박민희   29   대구
-- 최혜영   28   전주

SELECT rowid, name FROM classmates;
rowid  name
-----  ----
1      홍길동
2      김철수
3      이호영
4      박민희
5      최혜영

SELECT rowid, name FROM classmates LIMIT 2;
-- rowid  name
-- -----  ----
-- 1      홍길동
-- 2      김철수

SELECT rowid, name FROM classmates LIMIT 1 OFFSET 2;
-- rowid  name
-- -----  ----
-- 3      이호영

SELECT * FROM classmates WHERE address='서울';
-- name  age  address
-- ----  ---  -------
-- 홍길동   30   서울

SELECT name FROM classmates WHERE age >= 30;
-- name
-- ----
-- 홍길동
-- 김철수

SELECT DISTINCT age FROM classmates;
-- age
-- ---
-- 30
-- 26
-- 29
-- 28

SELECT DISTINCT address FROM classmates;
-- address
-- -------
-- 서울
-- 제주
-- 인천
-- 대구
-- 전주

-- 삭제 
DELETE FROM classmates WHERE rowid=5;
rowid  name  age  address
-----  ----  ---  -------
1      홍길동   30   서울
2      김철수   30   제주
3      이호영   26   인천
4      박민희   29   대구

INSERT INTO classmates VALUES ('주세환', 40, '대전'); 
SELECT rowid, * FROM classmates;
-- rowid  name  age  address
-- -----  ----  ---  -------
-- 1      홍길동   30   서울
-- 2      김철수   30   제주
-- 3      이호영   26   인천
-- 4      박민희   29   대구
-- 5      주세환   40   대전

-- 수정
UPDATE classmates SET name='홍길동', address='제주도' WHERE rowid=5;
SELECT rowid, * FROM classmates;
rowid  name  age  address
-----  ----  ---  -------
1      홍길동   30   서울
2      김철수   30   제주
3      이호영   26   인천
4      박민희   29   대구
5      홍길동   40   제주도

SELECT rowid, name FROM classmates LIMIT 100;
```

# 04_autoincrement.sql

```sqlite
CREATE TABLE members(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

INSERT INTO members VALUES 
(1, '홍길동'), 
(2, '김철수'),
(3, '이호영'),
(4, '박민희'),
(5, '최혜영');

DELETE FROM members WHERE rowid=5;
INSERT INTO members (name) VALUES ('주세환'); 
SELECT * FROM members;
-- id  name
-- --  ----
-- 1   홍길동
-- 2   김철수
-- 3   이호영
-- 4   박민희
-- 6   주세환  
```

# 05.users.sql

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
```

# 06_function.sql

```sqlite
SELECT * FROM users LIMIT 1;

-- pipe sign 엔터 위에 있어요 보통
-- 문자열 합치기 ||
-- (성+이름) 출력, 5명만
SELECT 
    last_name || first_name 이름,
    age,
    country,
    phone,
    balance
FROM users
LIMIT 5;

-- 이름   age  country  phone          balance
-- ---  ---  -------  -------------  -------
-- 유정호  40   전라북도     016-7280-2855  370
-- 이경희  36   경상남도     011-9854-5133  5900
-- 구정자  37   전라남도     011-4177-8170  3100
-- 장미경  40   충청남도     011-9079-4419  250000
-- 차영환  30   충청북도     011-2921-4284  220

-- 문자열 길이 LENGTH
SELECT 
    LENGTH(first_name),
    first_name
FROM users
LIMIT 5;
-- LENGTH(first_name)  first_name
-- ------------------  ----------
-- 2                   정호
-- 2                   경희
-- 2                   정자
-- 2                   미경
-- 2                   영환

-- 문자열 변경 REPLACE
-- 016-7280-2855 => 01672802855
SELECT 
    first_name,
    phone,
    REPLACE(phone, '-', '')
FROM users
LIMIT 5;

-- 숫자 활용
SELECT MOD(5, 2)
FROM users
LIMIT 1;

-- 올림, 내림, 반올림
SELECT CEIL(3.14), FLOOR(3.14), ROUND(3.14)
FROM users
LIMIT 1;

-- 9의 제곱근
SELECT SQRT(9)
FROM users
LIMIT 1;

-- 9^2
SELECT POWER(9, 2)
FROM users
LIMIT 1;
```

# 07_group.sql

```sqlite
-- GROUP BY

-- 성별 갯수
SELECT last_name, COUNT(*)
FROM users
GROUP BY last_name;

-- GROUP BY에서 활용하는 컬럼을 제외하고는
-- 집계함수를 쓰세요.
SELECT last_name, AVG(age), COUNT(*)
FROM users
GROUP BY last_name;

-- 참고...
SELECT last_name, age
FROM users
WHERE last_name = '곽';
-- last_name  age
-- ---------  ---
-- 곽          25
-- 곽          30
-- 곽          28
-- 곽          15

-- GROUP BY는 결과가 정렬되지 않아요. 기존 순서와 바뀜
-- 원칙적으로 내가 정렬해서 보고 싶으면 ORDER BY!

SELECT *
FROM users
LIMIT 5;
-- first_name  last_name  age  country  phone          balance       
-- ----------  ---------  ---  -------  -------------  -------       
-- 정호          유          40   전라북도     016-7280-2855  370    
-- 경희          이          36   경상남도     011-9854-5133  5900   
-- 정자          구          37   전라남도     011-4177-8170  3100   
-- 미경          장          40   충청남도     011-9079-4419  250000 
-- 영환          차          30   충청북도     011-2921-4284  220  

SELECT last_name, COUNT(*)
FROM users
GROUP BY last_name
LIMIT 5;

-- last_name  COUNT(*)
-- ---------  --------
-- 강          23
-- 고          10
-- 곽          4
-- 구          2
-- 권          17

-- GROUP BY WHERE를 쓰고 싶다.
-- 100번 이상 등장한 성만 출력하고 싶음. 
SELECT last_name, COUNT(last_name)
FROM users
WHERE COUNT(last_name) > 100
GROUP BY last_name;
-- 오류 발생!
-- Parse error: misuse of aggregate: COUNT()
--   LECT last_name, COUNT(last_name) FROM users WHERE COUNT(last_name) > 100 GROUP

-- 조건에 따른 GROUP 하시려면
-- HAVING을 쓴다!
SELECT last_name, COUNT(last_name)
FROM users
GROUP BY last_name
HAVING COUNT(last_name) > 100;
```

# 08_case.sql

```sqlite
-- 단순 조회
SELECT id, gender
FROM healthcare
LIMIT 5;

-- id  gender
-- --  ------
-- 1   1
-- 2   2
-- 3   2
-- 4   1
-- 5   2

-- 성별 1(남자), 2(여자)
SELECT 
    id,
    CASE 
        WHEN gender = 1 THEN '남자'
        WHEN gender = 2 THEN '여자'
        -- ELSE 
    END AS 성별
FROM healthcare 
LIMIT 5;
-- id  성별
-- --  -----
-- 1   남자
-- 2   여자
-- 3   여자
-- 4   남자
-- 5   여자

-- 흡연(smoking)
SELECT DISTINCT smoking
FROM healthcare;

SELECT 
    id, 
    smoking, 
    CASE 
        WHEN smoking = 1 THEN '비흡연자'
        WHEN smoking = 2 THEN '흡연자'
        WHEN smoking = 3 THEN '헤비스모커'
        ELSE '무응답'
    END
FROM healthcare
LIMIT 50;

-- 나이에 따라서 구분
-- 청소년(~18), 청년(~40), 중장년(~90)
SELECT 
    first_name,
    last_name,
    age,
    CASE 
        WHEN age <= 18 THEN '청소년'
        WHEN age <= 40 THEN '청년'
        WHEN age <= 90 THEN '중장년'
        ELSE '노년' 
    END
FROM users
LIMIT 10;
```

# 09_subquery.sql

```sqlite
-- 가장 나이가 작은 사람의 수
-- 1
SELECT age, COUNT(*)
FROM users
GROUP BY age
ORDER BY age
LIMIT 1;
-- age  COUNT(*)
-- ---  --------
-- 15   39

-- 확인해보기
SELECT MIN(age) 
FROM users;
-- MIN(age)
-- --------
-- 15

SELECT COUNT(*)
FROM users 
WHERE age = 15;
-- COUNT(*)
-- --------
-- 39

SELECT COUNT(*)
FROM users 
WHERE age = (SELECT MIN(age) FROM users);
-- COUNT(*)
-- --------
-- 39

-- 평균 계좌 잔고가 높은 사람은 수?

SELECT AVG(balance) FROM users;

SELECT COUNT(*)
FROM users
WHERE balance > (SELECT AVG(balance) FROM users);
-- COUNT(*)
-- --------
-- 222

-- 유은정과 같은 지역에 사는 사람의 수?
SELECT 
    country
FROM users
WHERE last_name = '유' AND first_name = '은정';

SELECT 
    COUNT(*)
FROM users
WHERE country = (SELECT country FROM users
WHERE last_name = '유' AND first_name = '은정');

-- 당연히
SELECT COUNT(*), AVG(balance), AVG(age)
FROM users;

-- 예를 들면
-- table이 게시글 테이블, 댓글 테이블
SELECT 
    (SELECT COUNT(*) FROM users) AS 총인원,
    (SELECT AVG(balance) FROM users) AS 평균연봉;
-- 총인원   평균연봉
-- ----  ---------
-- 1000  151456.89

-- 이은정
SELECT 
    country
FROM users
WHERE last_name = '이' AND first_name = '은정';
-- country
-- -------
-- 전라북도
-- 경상북도

SELECT 
    COUNT(*)
FROM users
WHERE country = (SELECT country FROM users
WHERE last_name = '이' AND first_name = '은정');
-- COUNT(*)
-- --------
-- 115

SELECT country, COUNT(*)
FROM users
GROUP BY country;
-- country  COUNT(*)
-- -------  --------
-- 강원도      101
-- 경기도      114
-- 경상남도     106
-- 경상북도     103
-- 전라남도     123
-- 전라북도     115
-- 제주특별자치도  118
-- 충청남도     105
-- 충청북도     115

SELECT 
    COUNT(*)
FROM users
WHERE country IN (SELECT country FROM users
WHERE last_name = '이' AND first_name = '은정');
-- COUNT(*)
-- --------
-- 218

-- 특정 성씨별로 가장 적은 나이 사람 모두
SELECT 
    last_name,
    MIN(age)
FROM users
GROUP BY last_name;

SELECT
    last_name,
    first_name,
    age
FROM users
WHERE (last_name, age) IN (
    SELECT 
        last_name,
        MIN(age)
    FROM users
    GROUP BY last_name)
ORDER BY last_name;
```

# 10_last.sql

```sqlite
-- AC/DC의 모든 앨범
-- AC/DC (artists)
-- 앨범(albums)

-- 앨범 검색하려고 했는데..
-- 아티스는 id로 저장되어있네요.
-- AC/DC는 아는데 ID를 모르네요?

-- ID 조회
SELECT ArtistId 
FROM artists
WHERE Name = 'Nirvana';

-- 서브쿼리
SELECT * 
FROM albums
WHERE ArtistId = (SELECT ArtistId 
FROM artists
WHERE Name = 'Nirvana');

SELECT * FROM users JOIN role ON users.role_id = role.id;

SELECT * FROM users JOIN artists ON users.ArtistId = artists.id
SELECT * FROM albums WHERE ArtistId = (SELECT ArtistId FROM artists WHERE Name = 'Nirvana');

WHERE ArtistId = (SELECT ArtistId 
FROM artists
WHERE Name = 'Nirvana');
```



FQA)

그럼 조인과 서브쿼리랑 차이점이라고 한다면 

조인은 id가 같은 모두를 찾아서 보여준다. 

서브 쿼리는 특정조건에 맞는(WHERE을 사용시) 쿼리만 찾아 보여 준다 이 정도로 이해 하면 될까요?

예시)

SELECT * FROM users JOIN artists ON users.ArtistId = artists.id
SELECT * FROM albums WHERE ArtistId = (SELECT ArtistId FROM artists WHERE Name = 'Nirvana');

re: 정의 서브는 쿼리안에 쿼리

조인은 두 테이블을 합친다

조인이 성능적으로 더 좋다. 

웹페이지에 조인 vs 서브쿼리

모든것이 대체 될 수 있는 개념이 아니다. 

# JOIN 

- INNER JOIN
- OUTER JOIN
- LEFT JOIN(겹치지 않으면 혹은 NULL이면 모든 값이 NULL이렇게 나옴)
- FULL OUTER JOIN (왼쪽, 오른쪽 하고 겹치는것은 공백?한다. )
- CROSS JOIN (모든 가능한 수 조인)

WHERE과도 합칠 수 있다. 

```sqlite
SELECT * FROM users LEFT OUTER JOIN role ON users.role_id = role.id WHERE id != NULL;
SELECT * FROM albums FULL OUTER JOIN artists ON albums.role_id = artists.id;
장르 정보
트렉에 앨범 아이디 아이디 대신 이름의 형태. 
```

# 11_CREATE.sq

```sqlite
CREATE TABLE users (
    id INT PRIMARY KEY,
    name TEXT,
    role_id INT
);

INSERT INTO users VALUES 
    (1, '관리자', 1),
    (2, '김철수', 2),
    (3, '이영희', 2);

CREATE TABLE role (
    id INT PRIMARY KEY, 
    title TEXT
);

INSERT INTO role VALUES 
    (1, 'admin'),
    (2, 'staff'),
    (3, 'student');

CREATE TABLE articles (
    id INT PRIMARY KEY, 
    title TEXT,
    content TEXT,
    user_id INT
);

INSERT INTO articles VALUES 
    (1, '1번글', '111', 1),
    (2, '2번글', '222', 2),
    (3, '3번글', '333', 1),
    (4, '4번글', '444', NULL);

-- 확인
.mode column
SELECT * FROM users;
SELECT * FROM role;
SELECT * FROM articles;
```

# 12_join.sql

```sqlite
-- INNER JOIN
-- A와 B테이블에서 값이 일치하는 것들만 
SELECT *
FROM users INNER JOIN role
    ON users.role_id = role.id;
-- id  name  role_id  id  title
-- --  ----  -------  --  -----
-- 1   관리자   1        1   admin
-- 2   김철수   2        2   staff
-- 3   이영희   2        2   staff

SELECT 
    users.name, 
    role.title
FROM users INNER JOIN role
    ON users.role_id = role.id;
-- name  title
-- ----  -----
-- 관리자   admin
-- 김철수   staff
-- 이영희   staff

-- 스태프(2)만 출력
SELECT *
FROM users INNER JOIN role
    ON users.role_id = role.id
WHERE role.id = 2;
-- id  name  role_id  id  title
-- --  ----  -------  --  -----
-- 2   김철수   2        2   staff
-- 3   이영희   2        2   staff

-- 이름을 내림차순으로 출력하세요.
SELECT *
FROM users INNER JOIN role
    ON users.role_id = role.id
ORDER BY users.name DESC;
-- id  name  role_id  id  title
-- --  ----  -------  --  -----
-- 3   이영희   2        2   staff
-- 2   김철수   2        2   staff
-- 1   관리자   1        1   admin

-- LEFT OUTER JOIN
SELECT * 
FROM articles LEFT OUTER JOIN users
    ON articles.user_id = users.id;

-- id  title  content  user_id  id  name  role_id
-- --  -----  -------  -------  --  ----  -------
-- 1   1번글    111      1        1   관리자   1
-- 2   2번글    222      2        2   김철수   2
-- 3   3번글    333      1        1   관리자   1
-- 4   4번글    444

SELECT * 
FROM articles LEFT OUTER JOIN users
    ON articles.user_id = users.id
WHERE articles.user_id IS NOT NULL;
-- id  title  content  user_id  id  name  role_id
-- --  -----  -------  -------  --  ----  -------
-- 1   1번글    111      1        1   관리자   1
-- 2   2번글    222      2        2   김철수   2
-- 3   3번글    333      1        1   관리자   1

SELECT * 
FROM articles FULL OUTER JOIN users
    ON articles.user_id = users.id;

-- CROSS JOIN
SELECT * 
FROM users CROSS JOIN role;
-- id  name  role_id  id  title
-- --  ----  -------  --  -------
-- 1   관리자   1        1   admin
-- 1   관리자   1        2   staff
-- 1   관리자   1        3   student
-- 2   김철수   2        1   admin
-- 2   김철수   2        2   staff
-- 2   김철수   2        3   student
-- 3   이영희   2        1   admin
-- 3   이영희   2        2   staff
-- 3   이영희   2        3   student

-- 3개의 테이블 조인
SELECT * 
FROM articles
    JOIN users
        ON articles.user_id = users.id
    JOIN role
        ON users.role_id = role.id;
-- id  title  content  user_id  id  name  role_id  id  title
-- --  -----  -------  -------  --  ----  -------  --  -----
-- 1   1번글    111      1        1   관리자   1        1   admin
-- 2   2번글    222      2        2   김철수   2        2   staff
-- 3   3번글    333      1        1   관리자   1        1   admin
```

















