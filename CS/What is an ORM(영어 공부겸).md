# What is an ORM – The Meaning of Object Relational Mapping Database Tools



![What is an ORM – The Meaning of Object Relational Mapping Database Tools](https://www.freecodecamp.org/news/content/images/size/w2000/2022/09/markus-winkler-gLdJnQFcIXE-unsplash.jpg)

Object Relational Mapping (ORM) is a technique used in creating a "bridge" between object-oriented programs and, in most cases, [relational databases](https://www.freecodecamp.org/news/what-is-a-relational-database-rdbms-definition/).

객체 관계 연결(ORM) 은/ 사용되는 기술 입니다. / 다르를 만드는데/ 객체지향프로그램 사이에서 / 그리고 대부분의 관계 데이터 베이스에서

Put another way, you can see the ORM as the layer that connects [object oriented programming](https://www.freecodecamp.org/news/four-pillars-of-object-oriented-programming/) (OOP) to relational databases.

바꿔 말하면/ 너는 ORM을 ~로 볼 수 있다./ ~하는 층으로/ 객체 지향 프로그램(OOP)에서 관계데이터 베이스로 연결하는

When interacting with a database using OOP languages, you'll have to perform different operations like creating, reading, updating, and deleting (CRUD) data from a database. By design, you use SQL for performing these operations in relational databases.

데이터 베이스와 소통 할 때/ 객체 지향 프로그램 언어를 사용하는/ 너는 다른 작업을 수행해야 할 것이다 / 만들고 읽고 업데이트하고, 삭제하는 것처럼(CRUD)/데이터 베이스로 부터 데이터를. / 설계상/ 너는 SQL을 사용해서/~하는 수행을 위해/ 그것들을 데이터 베이스 안에서 작업하는

While using SQL for this purpose isn't necessarily a bad idea, the ORM and ORM tools help simplify the interaction between relational databases and different OOP languages.

SQL을 사용하는 동안/ 목적을 위해/ 필수적이지 않은 나쁜 아이디어는/ ORM과 ORM도구는 단순화를 돕는다. / 관계형 데이터베이스 와 다른 객체지향프로그램 언어 사이에 상호작용을

## What is an ORM Tool?

ORM툴은 무엇인가?

An ORM tool is software designed to help OOP developers interact with relational databases. So instead of creating your own ORM software from scratch, you can make use of these tools.

ORM툴은 ~를 돕기 위해 설계된 도구인데/ 객체지향프로그램이 개발자와 관계형 데이터 베이스 간에 상호작용을/ 그래서 만드는 대신에/ 너의 자체 객체 관계 연결 소프트웨어를 / 스크래취 로부터(?)/너는 그 도구를 사용할 수 있어.

Here's an example of SQL code that retrieves information about a particular user from a database:

여기 SQL코드 ~하는 예시가 있어. / 정보를 가져오는/ 특정 유저에 관한/ 데이터베이스로 부터 

```sql
"SELECT id, name, email, country, phone_number FROM users WHERE id = 20"
```

아이디 20번의 유저의 id, name, email, country, phone_number를 가져오는 예시

The code above returns information about a user — `name`, `email`, `country`, and `phone_number` — from a table called `users`. Using the `WHERE` clause, we specified that the information should be from a user with an `id` of 20.

위의 코드는/ ~관한 정보를 돌려준다./유저의 name, email, country and phone_number를/ 콜한 users 테이블로 부터/ WHERE라는 조항을 사용하여/ 

On the other hand, an ORM tool can do the same query as above with simpler methods. That is:

```
users.GetById(20)
```

So the code above does the same as the SQL query. Note that every ORM tool is built differently so the methods are never the same, but the general purpose is similar.

ORM tools can generate methods like the one in the last example.

Most OOP languages have a variety of ORM tools that you can choose from. Here are some of the most popular for Java, Python, PHP, and .NET development:

### Popular ORM Tools for Java

#### 1. Hibernate

[Hibernate](https://hibernate.org/orm/) enables developers to write data persistent classes following OOP concepts like inheritance, polymorphism, association, composition. Hibernate is highly performant and is also scalable.

#### 2. Apache OpenJPA

[Apache OpenJPA](https://openjpa.apache.org/) is also a Java persistence tool. It can be used as a stand-alone **POJO** (plain old Java object) persistence layer.

#### 3. EclipseLink

[EclipseLink](https://www.eclipse.org/eclipselink/) is an open source Java persistence solution for relational, XML, and database web services.

#### 4. jOOQ

[jOOQ](https://www.jooq.org/) generates Java code from data stored in a database. You can also use this tool to build type safe SQL queries.

#### 5. Oracle TopLink

You can use [Oracle TopLink](https://docs.oracle.com/cd/E17904_01/web.1111/b32441/undtl.htm#JITDG91126) to build high-performance applications that store persistent data. The data can be transformed into either relational data or XML elements.

### Popular ORM Tools for Python

#### 1. Django

[Django](https://docs.djangoproject.com/en/4.1/topics/db/queries/) is a great tool for building web applications rapidly.

#### 2. web2py

[web2py](http://www.web2py.com/init/default/index) is an open source full-stack Python framework for building fast, scalable, secure, and data-driven web applications.

#### 3. SQLObject

[SQLObject](http://www.sqlobject.org/) is an object relational manager that provides an object interface to your database.

#### 4. SQLAlchemy

[SQLAlchemy](https://www.sqlalchemy.org/) provides persistence patterns designed for efficient and high-performing database access.

### Popular ORM Tools for PHP

#### 1. Laravel

[Laravel](https://laravel.com/docs/9.x/eloquent) comes with an object relational manager called Eloquent which makes interaction with databases easier.

#### 2. CakePHP

[CakePHP](https://book.cakephp.org/4/en/orm.html) provides two object types: repositories which give you access to a collection of data and entities which represents individual records of data.

#### 3. Qcodo

[Qcodo](https://github.com/qcodo/qcodo) provides different commands that can be run in the terminal to interact with databases.

#### 4. RedBeanPHP

[RedBeanPHP](https://redbeanphp.com/index.php) is a zero config object relational mapper.

### Popular ORM Tools for .NET

#### 1. Entity Framework

[Entity Framework](https://learn.microsoft.com/en-us/ef/) is a multi-database object-database mapper. It supports SQL, SQLite, MySQL, PostgreSQL, and Azure Cosmos DB.

#### 2. NHibernate

[NHibernate](https://nhibernate.info/) is an open source object relational mapper with tons of plugins and tools to make development easier and faster.

#### 3. Dapper

[Dapper](https://www.learndapper.com/) is a micro-ORM. It is mainly used to map queries to objects. This tool doesn't do most of the things an ORM tool would do like SQL generation, caching results, lazy loading, and so on.

#### 4. Base One Foundation Component Library (BFC)

[BFC](http://www.boic.com/b1mspecsheet.htm) is a framework for creating networked database applications with Visual Studio and DBMS software from Microsoft, Oracle, IBM, Sybase, and MySQL

You can see more ORM tools [here](https://en.wikipedia.org/wiki/List_of_object–relational_mapping_software).

Now let's discuss some of the advantages and disadvantages of using ORM tools.

## Advantages of Using ORM Tools

Here are some of the advantages of using an ORM tool:

- It speeds up development time for teams.
- Decreases the cost of development.
- Handles the logic required to interact with databases.
- Improves security. ORM tools are built to eliminate the possibility of SQL injection attacks.
- You write less code when using ORM tools than with SQL.

## Disadvantages of Using ORM Tools

- Learning how to use ORM tools can be time consuming.
- They are likely not going to perform better when very complex queries are involved.
- ORMs are generally slower than using SQL.

## Summary

In this article, we talked about Object Relational Mapping. This is a technique used to connect object oriented programs to relational databases.

We listed some of the popular ORM tools for different programming languages.

We concluded with some of the advantages and disadvantages of using ORM tools. languages.

Happy coding!





# 한글로 조사



Goal

> - 영속성(Persistence)이란
> - ORM(Object Relational Mapping)이란
> - ORM의 장단점
> - The Object-Relational Impedance Mismatch
> - Association(연관성)
>   - One-To-One Relationship
>   - One-To-Many Relationship

## 영속성(Persistence)
- 데이터를 생성한 프로그램이 종료되더라도 사라지지 않는 데이터의 특성을 말한다.

- 영속성을 갖지 않는 데이터는 단지 메모리에서만 존재하기 때문에 프로그램을 종료하면 모두 잃어버리게 된다.

- Object Persistence(영구적인 객체)

  - 메모리 상의 데이터를 파일 시스템, 관계형 테이터베이스 혹은 객체 데이터베이스 등을 활용하여 영구적으로 저장하여 영속성 부여한다.
  - ![img](https://gmlwjd9405.github.io/images/database/orm-persistence.png)

  - 데이터를 데이터베이스에 저장하는 3가지 방법
    - JDBC (java에서 사용)
    - Spring JDBC (Ex. JdbcTemplate)
    - Persistence Framework (Ex. Hibernate, Mybatis 등)

- Persistence Layer

  - 프로그램의 아키텍처에서, 데이터에 영속성을 부여해주는 계층을 말한다.
  - JDBC를 이용하여 직접 구현할 수 있지만 Persistence framework를 이용한 개발이 많이 이루어진다.

- Persistence Framework

  - JDBC 프로그래밍의 복잡함이나 번거로움 없이 간단한 작업만으로 데이터베이스와 연동되는 시스템을 빠르게 개발할 수 있으며 안정적인 구동을 보장한다.
  - Persistence Framework는 SQL Mapper와 ORM으로 나눌 수 있다.
    - Ex) JPA, Hibernate, Mybatis 등

### ORM이란

Object Relational Mapping, 객체-관계 매핑

- 객체와 관계형 데이터베이스의 데이터를 자동으로 매핑(연결)해주는 것을 말한다.
  - 객체 지향 프로그래밍은 클래스를 사용하고, 관계형 데이터베이스는 테이블을 사용한다.
  - 객체 모델과 관계형 모델 간에 불일치가 존재한다.
  - ORM을 통해 객체 간의 관계를 바탕으로 SQL을 자동으로 생성하여 불일치를 해결한다.
- 데이터베이스 데이터 <—매핑—> Object 필드
  - 객체를 통해 간접적으로 데이터베이스 데이터를 다룬다.
- Persistant API라고도 할 수 있다.
  - Ex) JPA, Hibernate 등

### ORM의 장단점
#### 장점
- 객체 지향적인 코드로 인해 더 직관적이고 비즈니스 로직에 더 집중할 수 있게 도와준다.
  - ORM을 이용하면 SQL Query가 아닌 직관적인 코드(메서드)로 데이터를 조작할 수 있어 개발자가 객체 모델로 프로그래밍하는 데 집중할 수 있도록 도와준다.
  - 선언문, 할당, 종료 같은 부수적인 코드가 없거나 급격히 줄어든다.
  - 각종 객체에 대한 코드를 별도로 작성하기 때문에 코드의 가독성을 올려준다.
  - SQL의 절차적이고 순차적인 접근이 아닌 객체 지향적인 접근으로 인해 생산성이 증가한다.
- 재사용 및 유지보수의 편리성이 증가한다.
  - ORM은 독립적으로 작성되어있고, 해당 객체들을 재활용 할 수 있다.
  - 때문에 모델에서 가공된 데이터를 컨트롤러에 의해 뷰와 합쳐지는 형태로 디자인 패턴을 견고하게 다지는데 유리하다.
  - 매핑정보가 명확하여, ERD를 보는 것에 대한 의존도를 낮출 수 있다.
- DBMS에 대한 종속성이 줄어든다.
  - 객체 간의 관계를 바탕으로 SQL을 자동으로 생성하기 때문에 RDBMS의 데이터 구조와 Java의 객체지향 모델 사이의 간격을 좁힐 수 있다.
  - 대부분 ORM 솔루션은 DB에 종속적이지 않다.
  - 종속적이지 않다는것은 구현 방법 뿐만아니라 많은 솔루션에서 자료형 타입까지 유효하다.
  - 프로그래머는 Object에 집중함으로 극단적으로 DBMS를 교체하는 거대한 작업에도 비교적 적은 리스크와 시간이 소요된다.
  - 또한 자바에서 가공할경우 equals, hashCode의 오버라이드 같은 자바의 기능을 이용할 수 있고, 간결하고 빠른 가공이 가능하다.

#### 단점
- 완벽한 ORM 으로만 서비스를 구현하기가 어렵다.
  - 사용하기는 편하지만 설계는 매우 신중하게 해야한다.
  - 프로젝트의 복잡성이 커질경우 난이도 또한 올라갈 수 있다.
  - 잘못 구현된 경우에 속도 저하 및 심각할 경우 일관성이 무너지는 문제점이 생길 수 있다.
  - 일부 자주 사용되는 대형 쿼리는 속도를 위해 SP를 쓰는등 별도의 튜닝이 필요한 경우가 있다.
  - DBMS의 고유 기능을 이용하기 어렵다. (하지만 이건 단점으로만 볼 수 없다 : 특정 DBMS의 고유기능을 이용하면 이식성이 저하된다.)
- 프로시저가 많은 시스템에선 ORM의 객체 지향적인 장점을 활용하기 어렵다.
  - 이미 프로시저가 많은 시스템에선 다시 객체로 바꿔야하며, 그 과정에서 생산성 저하나 리스크가 많이 발생할 수 있다.
  - The Object-Relational Impedance Mismatch

The Object-Relational Impedance Mismatch

Granularity(세분성)

- 경우에 따라 데이터베이스에 있는 해당 테이블 수보다 더 많은 클래스를 가진 객체 모델을 가질 수 있다.
- 예를 들어, “사용자 세부 사항”에 대해 생각해보자.
  - 코드 재사용과 유지보수를 위해 “Person”과 “Address”라는 두 개의 클래스로 나눌 수 있다.
  - 그러나 데이터베이스에는 person이라는 하나의 테이블에 “사용자 세부 사항”을 저장할 수 있다.
  - 이렇게 Object 2개와 Table 1개로 두 개의 갯수가 다를 수 있다.
- Coarse Granularity(굵은/거친): PersonDetails Class
- Fine Granularity(가는/세밀한): Persion Class, Address Class

Inheritance(상속)

- RDBMS는 객체지향 프로그래밍 언어의 자연적 패러다임인 상속과 유사한 것을 정의하지 않는다.
- 즉, 상속의 개념이 없다.

Identity(일치)

- RDBMS는 ‘sameness’라는 하나의 개념을 정확히 정의하는데, 바로 ‘기본키(primary key)’이다.
- 그러나 자바에서는 객체 식별(a==b)과 객체 동일성(a.equales(b))을 모두 정의한다.
- RDBMS에서는 PK가 같으면 서로 동일한 record로 정의하지만, Java에서는 주솟값이 같거나 내용이 같은 경우를 구분하여 정의한다.

Associations(연관성)

- 객체지향 언어는 객체 참조(reference)를 사용하는 연관성을 나타내는 반면, RDBMS는 연관성을 ‘외래키(foreign key)’로 나타낸다.
- 아래 참고

Navigation(탐색/순회)

- Java 및 RDBMS에서 객체에 액세스하는 방법은 근본적으로 다르다.
- Java에서는 하나의 연결에서 다른 연결로 이동하면서 탐색/순회한다. (그래프 형태)
  - 예를 들어, aUser.getBillingDetails().getAccountNumber()
  - 이는 RDBMS에서 데이터를 검색하는 효율적인 방법이 아니다.
- RDBMS에서는 일반적으로 SQL 쿼리 수를 최소화하고 JOIN을 통해 여러 엔터티를 로드하고 원하는 대상 엔터티를 선택(select)한다.

### Association(연관성)

- Java에서의 객체 참조(Object References)

  - 방향성이 있다. (Directional)

  - ```java
     public class Employee { 
       private int id; 
       private String first_name; 
       …
       private Department department; // Employee -> Department
       …
      }
    ```

  -  Java에서 양방향 관계가 필요한 경우 연관을 두 번 정의해야 한다.

    - 즉, 서로 Reference를 가지고 있어야 한다.

- RDBMS의 외래키(Foreign Key)

  - FK와 테이블 Join은 관계형 데이터베이스 연결을 자연스럽게 만든다.

방향성이 없다. (Direction-Less)
  INSERT INTO 
  EMPLOYEE(id, first_name, … ,department_id) // FK
  VALUES …
One-To-One Relationship
예를 들어, 각 학생은 고유한 주소를 가지고 있다고 하자.
RDBMS (방향성이 없다.)
각 Student의 record는 서로 다른 Address record를 가리키고 이것은 일대일 매핑을 보여준다.
Java Object (방향성이 있다.)
public class Student {
 private long studentId;
 private String studentName;
 private Address studentAddress; // Student -> Address
 …
}
public class Address {
 private long addressId;
 private String street;
 private String city;
 private String state;
 private String zipcode;
 …
}
One-To-Many Relationship
예를 들어, 각 학생은 여러 개의 핸드폰을 가질 수 있다고 하자.
RDBMS (방향성이 없다.)
각 Student의 record는 여러 개의 Phone record를 가리킬 수 있다. (일대다 매핑)
이 관계를 하나의 다른 Table(Relational Model)로 만들 수 있다.
One-To-Many를 구성하는 방법: 1) Join Table, 2) Join Column
Java Object (방향성이 있다.)
public class Student {
 private long studentId;
 private String studentName;
 private Set<Phone> studentPhoneNumbers; // Student -> Some Phones
 …
}
public class Phone {
 private long phoneId;
 private String phoneType;
 private String phoneNumber;
 …
}
관련된 Post
JDBC, JPA/Hibernate, Mybatis의 차이에 대해 알고 싶으시면 JDBC, JPA/Hibernate, Mybatis의 차이를 참고하시기 바랍니다.
Spring Hibernate에 대해 알고 싶으시면 Spring Hibernate 이해하기를 참고하시기 바랍니다.
References
ORM의 장단점
https://gmlwjd9405.github.io/2019/02/01/orm.html



[출처](https://gmlwjd9405.github.io/2019/02/01/orm.html)



# ORM이란?

- ORM(Object-relational mapping)을 단순하게 표현하면 객체와 관계와의 설정이라 할 수 있다. ORM에서 말하는 [객체](http://www.incodom.kr/객체)([Object](http://www.incodom.kr/Object))의 의미는 우리가 흔히 알고 있는 OOP(Object_Oriented Programming)의 그 객체를 의미한다는 것을 쉽게 유추할 수 있을 것이다. 그렇다면 과연 관계라는 것이 의미하는 것은 무엇일까? 지극히 기초적인 이야기지만 개발자가 흔히 사용하고 있는 관계형 데이터베이스를 의미한다.
- 그렇다면 도대체 무엇이 문제여서 객체와 [관계형 데이터베이스](http://www.incodom.kr/관계형_데이터베이스) 간의 매핑을 지원해주는 Framework나 Tool들이 나오는 것일까? ORM framework나 도구가 없던 시절에도 이미 우리는 OOP를 하면서 객체와 관계형 데이터베이스를 모두 잘 사용하고 있었음에도 불구하고, 굳이 이런 새로운 개념들이 나오게 되는 이유는 "Back to basics(기본에 충실하자)" 을 지키기 위해서라고 볼 수 있다. 즉, 보다 OOP다운 프로그래밍을 하자는데부터 출발한 것이다.
- 그럼 과연 무엇이 문제였던 것일까? 우리가 어떤 어플리케이션을 만든다고 하면 관련된 정보들을 객체에 담아 보관하게 된다. 프로그래밍 실습 예제의 단골 손님격인 주소록을 만든다고 가정했을 때 주소록의 주체가 될 사람이라는 객체에는 주민등록번호, 이름, 키, 몸무게 등이 저장될 것이고 주소나 전화번호 같은 추가로 저장될 객체들이 연결 될 것이다. 이렇게 생성한 사람 객체를 영구적으로 저장하기 위해 파일이나 데이터베이스에 입력한다는 것은 객체와 그와 연결된 객체들을 데이터베이스의 테이블에 저장 한다는 것을 의미한게 된다. 즉, 테이블(Table)에 객체가 가지고 있던 정보를 입력하고, 이 테이블들을 "join"과 같은 SQL 질의어를 통해 관계 설정을 해 주게 된다. 여기서 문제는 이 테이블과 객체간의 이질성이 발생 하게 된다는 것이다.

# 사용예시

- 보통 ORM Framwork들은 이러한 이질성을 해결하기 위해서 객체와 테이블간의 관계를 설정하여 자동으로 처리하게 되는데 예시를 통해 확인하면 다음과 같다.public class Person{ private String name; private String height; private String weight; private String ssn; //implement getter & setter methods }
- iBatis의 경우에는 다음과 같이 mapping file내에서 해당 query의 결과를 받을 객체를 지정해 줄 수 있다<select id="getPerson" resultClass="net.agilejava.person.domain.Person"> SELECT name, height, weight, ssn FROM USER WHERE name = #name#; </select>
- 즉, getPerson 이라고 정의된 질의어 결과는 net.agilejava.person.domain의 Person객체에 자동으로 mapping 되는 것이다. Hibernate의 경우에는 mapping 파일에서 다음과 같이 표현을 해준다.<hibernate-mapping> <class name="net.agilejava.person.domain.Person" table="person"> <id name="name" column="name"/> <property name="height" column="height"/> <property name="weight" column="weight"/> <property name="ssn" column="ssn"/> <class> </hibernate-mapping>
- 위 두개의 Framework의 예시를 보면 알 수 있듯이 setter 메소드가 있으면 객체에 결과를 set하는 작업을 따로 해줄 필요 없이 자동으로 해당 값이 할당되게 된다. 물론 여기에 1:m 이나 m:1등의 관계들이 형성되면 추가적인 작업이 필요하긴 하지만 일단 눈에 보이는 간단한 부분은 처리가 되는 것을 볼 수 있다. 물론 반대의 경우에도 객체를 던져주면 ORM Framework에서 알아서 get을 수행해 해당하는 column에 넣어주게 된다.
- 어떻게 보면 더 복잡해 보일 수도 있는 [ORM](http://www.incodom.kr/ORM)이지만 막상 사용해 보면 그 편리함에 몸을 떨게 된다. 단순하게 get/set만 해주는게 목적이 아니라 객체지향적인 시스템을 위해서 관계형 데이터베이스의 설계부터 변화를 주고, 설계된 [데이터베이스](http://www.incodom.kr/데이터베이스)와 [객체](http://www.incodom.kr/객체)와의 관계에 대한 설정 등을 포함하여 보다 객체지향적인 시스템의 완성을 위한 도구라고 말할 수 있겠다. 물론, ORM 이라는 것이 흔히 말하는 silver bullet은 절대 아니다. 많은 사람들이 ORM에 대해 우려하고 있는 부분은 객체지향적으로 설계되지 않은 데이터베이스에서의 사용에 따른 폐해라고 생각한다. 이미 데이터베이스 중심적인 사고를 통해 만들어 놓은 데이터베이스에 ORM을 도입 해도 분명 이점이 있긴 하겠지만, 그에 비해 개발자들의 학습곡선이라던지, 기존에 존재하는 코드나 시스템들과의 연계 또는 유지보수 적인 측면, 그리고 성능 등에서 생각해보면 부정적으로 볼 수 밖에 없다. 즉, 전체 적인 시스템의 분석, 설계 단계에서부터 객체와 데이터베이스를 따로 생각하는 것이 아니라 하나의 덩어리로 인지하고 양쪽 모두를 고려한 설계를 해나갈 수 있을 때, ORM은 보다 좋은 모습을 보여주고 각광을 받을 수 있을 것이다.

# 장점

- 객체 지향적인 코드로 인해 더 직관적이고 비즈니스 로직에 더 집중할 수 있게 도와준다.
  - 선언문, 할당, 종료 같은 부수적인 코드가 없거나 급격히 줄어든다.
  - 각종 객체에 대한 코드를 별도로 작성하기 때문에 코드의 가독성을 올려준다.
  - SQL의 절차적이고 순차적인 접근이 아닌 객체 지향적인 접근으로 인해 생산성이 증가한다.
- 재사용 및 유지보수의 편리성이 증가한다.
  - ORM은 독립적으로 작성되어있고, 해당 객체들을 재활용 할 수 있다.
  - 때문에 모델에서 가공된 데이터를 컨트롤러에 의해 뷰와 합쳐지는 형태로 디자인 패턴을 견고하게 다지는데 유리하다.
  - 매핑정보가 명확하여, ERD를 보는 것에 대한 의존도를 낮출 수 있다.
- DBMS에 대한 종속성이 줄어든다.
  - 대부분 ORM 솔루션은 DB에 종속적이지 않다.
  - 종속적이지 않다는것은 구현 방법 뿐만아니라 많은 솔루션에서 자료형 타입까지 유효하다.
  - 프로그래머는 Object에 집중함으로 극단적으로 DBMS를 교체하는 거대한 작업에도 비교적 적은 리스크와 시간이 소요된다.
  - 또한 자바에서 가공할경우 equals, hashCode의 오버라이드 같은 자바의 기능을 이용할 수 있고, 간결하고 빠른 가공이 가능하다.

# 단점

- 완벽한 ORM 으로만 서비스를 구현하기가 어렵다.
  - 사용하기는 편하지만 설계는 매우 신중하게 해야한다.
  - 프로젝트의 복잡성이 커질경우 난이도 또한 올라갈 수 있다.
  - 잘못 구현된 경우에 속도 저하 및 심각할 경우 일관성이 무너지는 문제점이 생길 수 있다.
  - 일부 자주 사용되는 대형 쿼리는 속도를 위해 SP를 쓰는등 별도의 튜닝이 필요한 경우가 있다.
  - DBMS의 고유 기능을 이용하기 어렵다. (하지만 이건 단점으로만 볼 수 없다 : 특정 DBMS의 고유기능을 이용하면 이식성이 저하된다.)
- 프로시저가 많은 시스템에선 ORM의 객체 지향적인 장점을 활용하기 어렵다.
  - 이미 프로시저가 많은 시스템에선 다시 객체로 바꿔야하며, 그 과정에서 생산성 저하나 리스크가 많이 발생할 수 있다.

 

[출처](https://hello-bryan.tistory.com/318)



# 내가 정리

ORM이란 결국 데이터 베이스와 객체지향 프로그램(장고, 파이썬등)을 연결해 주는 것이다. 

우리가 항상 만들던 클래스가 ORM이라고 생각한다. 

[참고](https://popawaw.tistory.com/239)

SQLite, MySql, postgres 등과 관련 된 내용인듯하다. 

[장고 ORM](https://codesik.github.io/Django-ORM-Model/)

[장고 ORM활용](https://codesik.github.io/Django-ORM-Operation/)

우리가 항상 쓰던 models은 장고에서 자체 제공해 주는 ORM이다. 



그러면 MySql을 쓴다면 models.Model은 사용 안한다는 거겠지?

