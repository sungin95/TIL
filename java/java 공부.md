# Part 1

## Ch1.강의 소개

### 학습 목표

1. 객체지향 프로그래밍에 대한 이해
2. HTTP 프로토콜 및 HTTP 웹 서버 동작 원리 이해
3. MVC 구조 및 DI 내부 동작 원리 이해



### Chapter

1. 개발 환경 구축
2. 객체지향 패러다임
3. 웹 애플리케이션 이해
4. 서블릿 프로그래밍
5. JDBC 프로그래밍
6. MVC 프레임워크 만들기
7. DI 프레임워크 만들기
8. Spring Boot 코드 분석

## 

### 개발환경 구축

#### JDK 설치

jdk 구성

JRE와 Java Development Tools 로 구성



## Ch02.개발 환경 구성하기

0. 웹 프로젝트 환경 구성

- intellij vs maven vs gradle

  - maven보다 gradle가 늦게 나왔고 성능이 더 좋음
  - 그러나 maven이 커뮤니티는 더 풍부

- gradle DSL kotlin Groovy

- 파일 이름 바꾸기 `shift + f6`

- 설정추가

  - 임베디드 톰캣
  - 서블릿
  - 로그
  - 변경사항은 오른쪽에 리플레쉬 코끼리 클리하면 된다. (오타가 있으면 표시 없이 추가가 안되니 주의!)

- 서버 만들어서 실행하기 

  - f2누르면 문제있는 코드로 이동. 

    - import class 를 해 준다. 

  - 부족한 설정 추가. 

    - webapps 폴더 추가 

    - settions(carl+alt+S)에서 gradle(build execution,, deployment - build tools - gradle)

      여기서 설정을 inteliJ IDEA로 바꾸어 준다. 

    - 프로젝트 관련 설정 변경하기 shift+Ctrl+Alt+S(file의 project structure)

      

      여기까지가 특정 장소에 컴파일한 파일을 올리고

      톰캣이 이 컴파일한 파일을 사용 할 수 있도록 하는 환경 설정이다. 

      이것은 공식문서에서 확인 할 수 있다. 

      https://tomcat.apache.org/tomcat-8.5-doc/appdev/deployment.html

- 도커

  - 도커허브
  - 도커 컴포즈
    - 다중 컨테이너를 정의 실행하기 위한 도구

- 도커 활용 개발환경 구축하기

  - 도커 설치(설치 후 docker -v 로 확인)
  - 원하는 이미지 다운로드 
    - docker pull mysql:latest
    - docker run --name mysql-sample-container -e MYSQL_ROOT_PASSWORD=test -d -p 3306:3306 mysql:latest 
  - docker ps -a 로 확인
  -  mysql -u root -p
    - 비밀번호는 미리 입력한 test 이다. 

도커로 mysql을 연동해 버리네?

## Ch03.객체지향 패러다임

### 테스트코드 실습

- JUnit5 사용
  - 공식 문서 참고
    - https://junit.org/junit5/docs/current/user-guide/#writing-tests
    - https://www.petrikainulainen.net/programming/testing/junit-5-tutorial-writing-parameterized-tests/
- AssertJ
  - 테스트 코드 가독성을 높여주는 자바 라이브러리
- 테스트 코드를 작성하는 이유
  - 문서화 역할
  - 코드에 결함을 발견하기 위함
  - 리팩토링 시 안정성 확보
  - 데스트 하기 쉬운 코드를 작성하다 보면 더 낮은 결합도를 가진 설계를 얻을 수 있음.

- TDD
  - Test Driven Development(테스트 주도 개발)
  - 프로덕션 코드보다 테스트 코드를 먼저 자성하는 개발 방법
  - TFD(Test First Development) + 리팩토링(여기가 중요!!!)
  - 기능 동작을 검증(메소드 단위)

- BDD
  - Behavior Driven Development(행위 주도 개발)
  - 시나리오 기반으로 테스트 코드를 작성하는 개발 방법
  - 하나의 시나리오는 Given, When, Then 구조를 가짐


비밀번호 유효성 검증기를 만들면서 실습을 진행할 예정. 

- 요구사항
  - 비밀번호는 최소 8자 이상 12자 이하여야 한다. 
  - 비밀번호 8자 미만 또는 12자 초과인 경우 IIIegalArgumentException 예외를 발생시킨다. 
  - 경계조건에 대해 테스트 코드를 작성해야 한다. 



​	

## ch04.웹 애플리케이션 이해

- Step1 - 사용자 요청을 메인 Thread가 처리하도록 한다. 
- Step2 - 사용자 요청이 들어올 때마다 Thread를 새로 생성해서 사용자 요청을 처리하도록 한다. 
- Step3 - Thread Pool을 적용해 안정적인 서비스가 가능하도록 한다. 


HTTP

- 1.1, 2 는 TCP 기반 위에서 동작
- 3은 UDP 기반 위에서 동작

HTTP 요청/응답 메시지 구조



클리이언트  => 요청, request Line, Header, Blank Line, Body => 서버

​                     <= 응답, Status line,Header, Blank Line, Body <= 

HTTP 특징

- 클라이언트-서버 모델
- 무상태 프로토콜(Stateless)
  - 서버가 클라이언트 상태를 유지하지 않음
  - 해결책: Keep-Alive속성 사용

- 비 연결성(Connectionless)
  - 서버가 클라이언트 요청에 대해 응답을 미치면 맺었던 연결을 끊어 버림
  - 해결책: 쿠키(클라이언트에 정보 저장), 세션(서버에 정보 저장), JWT



=> 이러한 특징을 갖는 이유는 HTTP는 기본적으로 불특정 다수와 통신이 가능하도록 설계된 프로토콜입니다. 그래서 더 많은 사람들과 통신을 하기 위한 특성을 지녔습니다. 



Httpequest

- RequestLine (GET /calculate?operand1=11&operator=*&operand2=55 HTTP/1.1)
  - HttpMethod
  - path
  - queryString
- Header
- Body



Step1은 처리 가능하게 만드는것

Step2는 사용자 요청이 들어올 때마다 새로 Thread생성.





### CGI  프로그램과 서블릿

CGI(CommonGateway Interface)

-  웹 서버와 애플리케이션 사이에 데이터를 주고받는 규약
- CGI 규칙에 따라서 만들어진 프로그램을 CGI 프로그램이라고 함.
- CGI프로그램 종류로는 컴파일 방식(C,C++,Java 등)과 인터프리터 방식(PHP, Python 등)이 있음.

![20230720_140836](java 공부.assets/20230720_140836.png)

웹서버와 Servlet파일 사이의 관계를 알아야 한다. 



#### Servlet

- 자바에서 웹 애플리케이션을 만드는 기술
- 자바에서 동적인 웹 페이지를 구현하기 위한 표준

#### ServletContainer

- 서블릿의 생성부터 소멸까지의 라이프사이클을 관리하는 역할
- 서블릿 컨테이너는 웹 서버와 소켓을 만들고 통신하는 과정을 대신 처리해준다. 개발자는 비즈니스 로직에만 집중하면 된다. 
- 서블릿 객체를 싱글톤으로 관리(인스턴스 하나만 생성하여 공유하는 방식)
  - 상태를 유지(stateful)하게 설계하면 안됨
  - Thread safety 하지 않음



#### WAS vs 서블릿 컨테이너

- WAS는 서블릿 컨테이너를 포함하는 개념
- WAS는 매 요청마다 스레드 풀에서 기존 스레드를 사용함
- WAS의 주요 튜닝 포인트는 max thread 수
- 대표적인 WAS로는 톰캣이 있다. 

![20230720_145436](java 공부.assets/20230720_145436.png)



RaceCondition 이란

여러 프로세스 혹은 스레드가 동시에 하나의 자원에 접근하는 경우를 말한다. 

### 계산기 서블릿 만들기



![20230720_152734](java 공부.assets/20230720_152734.png)

#### Servlet 인터페이스

- 서블릿 컨테이너가 서블릿 인터페이스에 있는 메소드들을 호출함
- 서블릿 생명주기와 관련된 메소드
  - init(), service(), destory()
- 서블릿 기타 메소드
  - getServletConfig()
  - getServletInfo()

서블릿을 몰라도 spring을 할 수 있는데 왜 학습해야 할까?

![20230720_154658](java 공부.assets/20230720_154658.png)

큰 그림을 이해하기 위해서는 서블릿에 대해 일정부분 학습이 필요하다. 







+일때 작동하지 않는다. 이유는 예약어 이기 때문에.

#### URL 인코딩(퍼센트 인코딩)

- URL로 사용할 수 없는 문자(예약어, Non-ASCII문자(한글)등)를 사용할 수 있도록 인코딩하는 것
- 인코딩 된 문자는 triplet(세 개가 한 세트)로 인코딩 되며 각각을 % 다음에 두 개의 16진수로 표현함
- 예약 문자
  - https://ko.wikipedia.org/wiki/%ED%8D%BC%EC%84%BC%ED%8A%B8_%EC%9D%B8%EC%BD%94%EB%94%A9
  - https://www.convertstring.com/ko/EncodeDecode/UrlEncode   (문자 변환)



## ch05.JDBC 프로그래밍

### JDBC

- 자바 애플리케이션에서 DB 프로그래밍을 할 수 있도록 도와주는 표준 인터페이스
- JDBC 인터페이스들을 구현한 구현체들은 각 데이터베이스 벤더 사들이 제공

=> python의 ORM을 말하는거 같다. 



### DBCP(Database connection pool)

- 미리 일정량의 DB 커넥션을 생성해서 풀에 저장해 두고 있다가 HTTP 요청에 따라 필요할 때 풀에서 커넥션을 가져다 사용하는 기법
- 참고로 스프링 부트 2.0 부터는 디폴트 커넥션 풀로 HikariCP 사용

=> 실습에 hikariCP사용

커넥션 풀 사용 시 유의 사항

- 커넥션의 사용 주체는 WAS 스레드이므로 커넥션 개수는 WAS 스레드 수와 함께 고려해야 함
- 커넥션 수를 크게 설정하면 메모리 소모가 큰 대신 동시 접속자 수가 많아지더라도 사용자 대기 시간이 상대적으로 줄어들게 되고, 반대로 커넥션 개수를 작게 설정하면 메모리 소모는 적은 대신 그만큼 대기시간이 길어질 수 있음. 따라서 적정량의 커넥션 객체를 생성해 두어야 함. 

DataSource

- 커넥션 획득하기 위한 표준 인터페이스
- HikariCP의 DataSource 사용



## ch06. MVC 프레임워크 만들기 

### 리플렉션 API 개념 소개 및 실습

#### Reflection

- 힙 영역에 로드돼 있는 클래스 타입의 객체를 통해 필드/메소드/생성자를 접근 제어자와 상관 없이 사용할 수 있도록 지원하는 API
- 컴파일 시점이 아닌 런타임 시점에 동적으로 특정 클래스의 정보를 추출해낼 수 있는 프로그래밍 기법
- 주로 프레임워크 또는 라이브러리 개발 시 사용됨.
- https://www.baeldung.com/reflections-library

#### Reflection 사용하는 프레임워크/라이브러리 소개

- Spring 프레임워크 (ex. DI)
- Test 프레임워크 (ex. JUnit)
- JSON Serialization/Deserialization 라이브러리 (ex. Jackson)
- 등등

#### 실습

- @Controller 애노테이션이 설정돼 있는 모든 클래스를 찾아서 출력한다. 
- 실습코드
  - https://github.com/serverwizard/jdbc-practice/tree/master/mvc-practice

### 프론트 컨드롤러 개념 소개 및 실습

- 모든 요청을 단일 handler(처리기)에서 처리하도록 하는 패턴
- 스프링 웹 MVC 프레임워크의 DispatcherServlet(프론트 컨트롤러 역할)이 프론트 컨트롤러 패턴으로 구현돼 있음. 
- ![20230726_164321](java 공부.assets/20230726_164321.png)

### Forward vs Redirect

#### Forward

- 서블릿에서 클라이언트(웹 브라우저)를 거치지 않고 바로 다른 서블릿 (또는 JSP)에게 요청하는 방식

- Forward 방식은 서버 내부에서 일어나는 요청이기 때문에 Http ServletRequest, HttpServletResponse객체가 새롭게 생성되지 않음(공유됨)

- RequestDispatcher dispatcher = request.getRequestDispatcher("포워드 할 서블릿 또는 JSP")

  dispatcher.forward(request, response)

#### Redirect

- 서블릿이 클라이언트(웹 브라우저)를 다시 거쳐 다른 서블릿(또는 JSP)에게 요청하는 방식
- Redirect 방식은 클라이언트로부터 새로운 요청이기 때문에 새로운 HttpServletRequest, HttpServletResponse 객체가 생성됨
- HttpServletResponse객체의 sendRedirect() 이용

![20230726_170905](java 공부.assets/20230726_170905.png)



logback 설정 학습 권장

#### 스프링 웹 MVC 프레임워크

- ![20230727_123312](java 공부.assets/20230727_123312.png)

- https://docs.spring.io/spring-framework/docs/3.2.x/spring-framework-reference/html/mvc.html

#### 애노테이션 기반 MVC 프레임워크

- DispatcherServlet
- AnnotationHandlerMapping
- HandlerAdapter
- ViewResolver

## ch07. DI 프레임워크 만들기

### DI 개념 소개 및 장점

DI (Dependency Injection)

- 의존성 주입
  - 한 객체가 다른 객체를 사용할 때 의존성이 있다고 함.
  - 런타임 시 의존 관계를 맺는 대상은 외부에서 결정하고 주입해 주는 것
  - 스프링 프레임워크는 DI 기능을 지원해주는 프레임워크

DI 장점

- 의존성 주입을 인터페이스 기반으로 설계하면, 코드가 유연해짐
  - 느슨한 결합도
- 변경에 유연해짐
  - 결합도가 낮은 객체끼지는 부품을 쉽게 갈아끼울 수 있음.
