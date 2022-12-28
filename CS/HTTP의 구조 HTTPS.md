오늘의 CS문제

1. HTTP의 구조
2. HTTPS란?



# HTTP의 구조

[출처](https://programmer93.tistory.com/60)

#### **1. HTTP란**

- HyperText Transfer Protocol 의 약자
- 하이퍼텍스트(HTML) 문서를 교환하기 위해 만들어진 통신 규약
- 서버간 네트워크 통신시 어떠한 형식으로 통신할지에 대해 정해둔 규약

#### **2. HTTP 메세지 기본 구조**

기본적인 HTTP의 구조는 아래와 같다.



![img](https://blog.kakaocdn.net/dn/SBdjE/btqRjfzXczu/7JmzAWw6i0BdlWKTn0k9g1/img.png)



**시작 라인**

- Response인지 Request 인지에 따라 **약간 형태가 다르다**.

**헤더**

- **header-field: field-value** 으로 구성되어 있다.
- HTTP 전송에 필요한 모든 부가정보를 가지고 있다.

**메시지 본문**

- 메세지의 본문을 담고 있다.

 


HTTP의 구조를 확인 하고 싶으면 CURL을 통해서 다음 커맨드를 치면

```
curl -v www.google.co.kr?query=http구조
```

다음과 같은 로그가 출력이 된다.



![img](https://blog.kakaocdn.net/dn/u7zTB/btqRlI2ZvD9/8yLcsfnkIJNdjtk9sKwYfK/img.png)



#### **2.1 HTTP Request 구조**

CURL로 요청을 보낸 "www.google.co.kr/?query=http구조" 의 HTTP Request 의 구조이다.



![img](https://blog.kakaocdn.net/dn/x30TZ/btqRrPzkJe5/LEOl80r5wrXA1cr0E62CRK/img.png)



#### **start line**

- [HTTP Method](https://programmer93.tistory.com/38) - 요청시 보내는 HTTP 메소드 형태이다. (GET, POST, PUT, PATCH, DELETE, 기타)
- Request Target - 어디로 보내는지에 대한 URI 이다.
- HTTP Version - HTTP 버젼으로 현재까지는 대부분이 HTTP/1.1이고 HTTP/2, HTTP/3 까지도 있다.



![img](https://blog.kakaocdn.net/dn/ceDXqo/btqRnNpsXqq/EZaWTj2BejpS4AmNx0Qixk/img.png)



#### **header**

 

- Host - 호스트 URL 이다.
- User-Agent - 클라이언트 정보다.
- Accept - 서버에서 해당 타입에 데이터를 보내달라고 요청하는 헤더이다.
- Authorization - JWT 같은 인증 토큰을 서버로 보낼 때 사용하는 헤더이다.
- 기타 등등



![img](https://blog.kakaocdn.net/dn/ckWqjf/btqRjf7T8bf/9HkmlXCiX4kyS2TKoudTj0/img.png)



 

위의 HTTP Method는 GET 방식이라 Body 부분은 따로 존재 하지 않지만 GET이 아닌 다른 메소드의 경우 Body가 존재한다. ( GET 도 Body가 있는 경우가 있는데 GET방식의 Body를 못받는 서버가 있어 권장하는 방법이 아님 )

 

 

 

#### **2.2 HTTP Response 구조**

위에서 요청한 요청의 HTTP Response 의 구조이다.

기본적인 HTTP 의 구조는 동일하지만 담겨오는 정보가 약간 다르다.

 



![img](https://blog.kakaocdn.net/dn/SGfdC/btqRxZWq8iF/n3TA0JZZVj58bei0lfDtbk/img.png)



 

#### **start line**

- HTTP Version - 응답온 메세지의 HTTP 버젼 정보이다.
- [Status Code](https://developer.mozilla.org/ko/docs/Web/HTTP/Status) - 응답 코드이다.
- [Status text](https://developer.mozilla.org/ko/docs/Web/HTTP/Status) - 응답 상태이다.



![img](https://blog.kakaocdn.net/dn/m3GjD/btqRqP8qnAh/oLLYFKNxZoJopNIzqaD5x0/img.png)



#### ***\*header\****

- Date - 응답온 일시이다.
- Content-Type - 응답 데이터의 타입이다.
- Cache-Control - 캐시용 헤더이다.
- 기타 등등



![img](https://blog.kakaocdn.net/dn/BNiRt/btqRqcJv0Iv/vPav8McqfhGSjOp0ngqxFK/img.png)



#### **body**

- 요청에 대한 응답 값



![img](https://blog.kakaocdn.net/dn/biac6B/btqRpuDFbql/4kWFxEtBvc919CiVYPyCFK/img.png)



 

## 내가 다시 정리

기본 구조는 같지만

start line

header

empty line

message body



요청인지 응답인지에 따라 형태가 좀 다르다. 



요청(GET형태라서 message body가 없지 POST형태였으면 이었을 것으로 추측)

![img](https://blog.kakaocdn.net/dn/x30TZ/btqRrPzkJe5/LEOl80r5wrXA1cr0E62CRK/img.png)

응답

![img](https://blog.kakaocdn.net/dn/SGfdC/btqRxZWq8iF/n3TA0JZZVj58bei0lfDtbk/img.png)

### 추가적으로 드는 궁금증

백엔드하는 사람은 요청을 토대로 정보를 전달해 줘야 하기 떄문에 요청의 구조를 이해하는 것이 중요하고

프론트하는 사람들은 응답 받은 값을 통하여 화면을 구성해야 하기 때문에 응답의 구조를 이해하는게 중요할 거 같으면서도

백엔드에서 프론트로 응답을 해 줘야 하기 때문에 응답의 구조를 이해해야 하고

프론트는 서버로 요청을 보내야 하기 때문에 요청의 구조를 이해하는 것이 중요할 거 같은데

무엇이 먼저일까? (당연히 둘 다 이해하는 것이 베스트지만 우선순의를 정해 보자면)



[출처](https://rachel-kwak.github.io/2021/03/08/HTTPS.html)

# HTTPS란?

몇 년 전만 해도 전자 상거래 페이지가 있는 웹사이트에서만 HTTPS를 사용하고 있었다. 그러나 2014년, 구글에서 HTTPS를 사용하는 웹사이트에 대해서 검색 순위 결과에 약간의 가산점을 주겠다고 하며 HTTP를 HTTPS로 바꾸라고 권고했다. 이에 그치지 않고 2019년, 구글은 크롬 68을 릴리즈하며 7월부터 SSL 보안 서버가 적용된 HTTPS 웹페이지는 ‘안전함’으로 표시하고 그렇지 않은 HTTP 사이트에 대해서는 ‘안전하지 않음’ 경고 표시를 적용할 것이라고 발표했다. HTTPS가 어떤 것이길래 구글에서 사용을 강조하는 것일까?



![img](https://post-phinf.pstatic.net/MjAxODA4MjNfMTgw/MDAxNTM1MDAzNzM3ODA2.eNAvF1GYYuE7Pk1bg9crj6GRNCvAAihiyzswr-UC8Isg.OqptAj0NBsBGz2MpA7f2Vg94yS6QZCrKIzQ70wfaWCgg.PNG/screenshot_006.png?type=w1200)



먼저, HTTP에 대해서 알아보자. HTTP란 HyperText Transfer Protocol의 약자로써, 풀어서 설명하면 **하이퍼텍스트(HyperText)를 전송(Transfer)하기 위해 사용되는 통신 규약(Protocol)**이다. 즉, 인터넷에서 HTML과 같은 문서를 사용자 컴퓨터에 설치된 웹 브라우저가 웹 서버에 요청할 때의 규칙이라고 할 수 있다.

HTTP 서버는 기본 포트인 80번 포트에서 서비스 대기 중이며, 클라이언트(웹 브라우저)가 TCP 80 포트를 사용해 연결하면 서버는 요청에 응답하면서 자료를 전송한다. HTTP는 정보를 텍스트로 주고 받기 때문에 네트워크에서 전송 신호를 인터셉트 하는 경우 원하지 않는 데이터 유출이 발생할 수 있다. 이러한 보안 취약점을 해결하기 위한 프로토콜이 **HTTP에 S(Secure Socket)가 추가된 HTTPS**이다.





## HTTPS



![img](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Ft1.daumcdn.net%2Fcfile%2Ftistory%2F9989B1505C72885E29)





![img](http://blog.wishket.com/wp-content/uploads/2020/02/03-3.png)



HTTPS는 기본 골격이나 사용 목적 등은 HTTP와 거의 동일하지만, 데이터를 주고 받는 과정에 ‘보안’ 요소가 추가되었다는 것이 가장 큰 차이점이다. HTTPS를 사용하면 **서버와 클라이언트 사이의 모든 통신 내용이 암호화**된다.

우리가 특정 파일에 암호를 걸 때처럼 어떤 키를 설정해서 잠금을 걸고, 풀 때에도 그것을 입력해서 푸는 것을 생각해보자. 간단하게 생각하면 웹 서버가 키 하나를 정해 페이지를 암호화해서 사용자의 웹 브라우저로 보내고, 웹 브라우저는 그 키를 이용해서 페이지를 복원하면 될 것이다. 그러나 웹 서버는 하나고 사용자는 불특정 다수이기 때문에 간단하지 않다. 그렇다고 키를 사용자들에게 막 줘버리면 아무나 암호화를 풀 수 있게 됨으로써 암호화의 의미가 없게 된다.

HTTPS는 위와 같은 상황에서 페이지를 암호화한 키가 그 페이지를 보는 특정 사용자에게만 알려지도록 한다. HTTPS는 SSL이나 TLS 프로토콜을 통해 세션 데이터를 암호화하며, 기본 TCP/IP 포트는 443이고, SSL 프로토콜 위에서 HTTPS 프로토콜이 동작한다.



> **[참고] TLS**
>
> Transport Layer Security의 줄임말. 과거 SSL에서 발전하며 이름이 변경 된 것이다. 하지만 아직도 SSL이란 명칭이 많이 사용되고 있다.





## 암호화 방식

공개키 암호화 방식과 공개키의 느리다는 단점을 보완한 대칭키 암호화 방식을 함께 사용한다. 공개키 방식으로 대칭키를 전달하고, 서로 공유된 대칭키를 가지고 통신하게 된다.



### 공캐키 방식

- A키로 암호화를 하면 B키로 복호화를 할 수 있다.
- B키로 암호화를 하면 A키로 복호화를 할 수 있다.
- 둘 중 하나를 비공개키(Private Key) 혹은 개인키라 부르며, 이는 자신만 가지고 있고 공개되지 않는다.
- 나머지 하나를 공개키(Public Key)라고 부르며 타인에게 제공한다. 공개키는 유출이 되어도 비공개키를 모르면 복호화 할 수 없기 때문에 안전하다.



![img](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=http%3A%2F%2Fcfile21.uf.tistory.com%2Fimage%2F9943623359FF02B1056ED8)





### 대칭키 방식

- 동일한 키로 암호화, 복호화가 가능하다.
- 대칭키는 매번 랜덤으로 생성되어 누출되어도 다음에 사용할 때는 다른 키가 사용되기 때문에 안전하다.
- 공개키보다 빠르게 통신할 수 있다.



이러한 SSL 방식을 적용하려면 인증서를 발급받아 서버에 적용시켜야 한다. 인증서는 사용자가 접속한 서버가 우리가 의도한 서버가 맞는지를 보장하는 역할을 한다. 인증서를 발급하는 기관을 CA(Certificate Authority)라고 부른다. 공인인증기관의 경우 웹 브라우저는 미리 CA 리스트와 함께 각 CA의 공개키를 알고 있다.



> **[참고] CA(Certificate Authority)란?**
>
> certification authority (CA)는 공개키와 공개 DNS명(ex.`www.example.com`)의 연결을 보장하는 기관이다. 예를 들어 클라이언트가 `www.example.com`의 공개키가 이 공개키인지 어떻게 알 수 있는가? 같은 것이다. 일단 이를 알 방법은 없다. CA는 자신만의 암호화 키로 웹사이트의 공개키를 암호학적으로 사인하는 데 사용함으로써 특정 공개키가 특정 사이트의 공개키라는 것을 보장한다. 이 서명은 계산적으로 위조할 가능성이 없다. 브라우저(그 외 클라이언트)는 잘 알려진 CS가 소유한 공개키를 보관하는 신뢰할 수 있는 anchor 저장소(trust anchor stores)를 유지하고 CS 서명을 암호학적으로 확인하는데 이 공개키를 사용한다.





## 동작 과정

보안적인 부분은 더이상 자세히 다루지 않고, 인증서 발급부터 어떤 식으로 사이트가 안전하게 사용자와 통신을 하는지 전체적으로 알아보자.
\* 아래 그림 및 설명에서 서버 = 사이트, 클라이언트 = 사용자로 나타내었다.



![img](https://t1.daumcdn.net/cfile/tistory/99F0FA445C456BB809)



1. 인터넷 사이트(서버)는 공개키와 개인키를 만들고, 신뢰할 수 있는 인증 기관(CA)에 자신의 정보와 공개키를 관리해달라고 계약하고 (경우에 따라) 돈을 지불한다.
2. 이 때, 계약을 완료한 인증 기관은 기관만의 공개키와 개인키가 있다. 인증 기관은 사이트가 제출된 데이터를 검증하고, 인증 기관의 개인키로 사이트에서 제출한 정보를 암호화해서 인증서를 만들어 제공한다. 사이트는 인증서를 가지게 되었다.
3. 인증 기관은 웹 브라우저에게 자신의 공개키를 제공한다.



![img](https://t1.daumcdn.net/cfile/tistory/993364345C457AED30)



1. 사용자가 사이트에 접속하면 서버는 자신의 인증서를 웹 브라우저(클라이언트)에게 보낸다. 예를 들어, 웹 브라우저가 index.html 파일을 달라고 요청했다면, 서버의 정보를 인증 기관의 개인키로 암호화한 인증서를 받게 되는 것이다.
2. 웹 브라우저는 3.에서 미리 알고 있던 인증기관의 공개키로 인증서를 해독하여 검증한다. 그러면 사이트의 정보와 서버의 공개키를 알 수 있게 된다.
   \* *이 부분은 보안상의 의미는 없다. 단지 해당 서버로부터 온 응답임을 확신할 수 있게 된다.*
3. 이렇게 얻은 서버의 공개키로 대칭키를 암호화해서 다시 사이트에 보낸다.
4. 사이트는 개인키로 암호문을 해독하여 대칭키를 얻게 되고, 이제 대칭키로 데이터를 주고받을 수 있게 된다.



![img](https://t1.daumcdn.net/cfile/tistory/9997354E5C457AF229)





> **[추가] 브라우저는 어떻게 CA의 공개키를 아는가?**
>
> 웹브라우저에는 이미 root CA의 Internet Explorer나 Netscape와 같은 웹 브라우저에는 브라우저가 자동으로 신뢰하는 (즉, Verisign, Thawte와 같은 널리 알려진 루트) CA 인증서 집합이 사전 구성되어 있습니다. (출처 - https://docs.oracle.com/cd/E19159-01/820-4605/abloj/index.html)
>
> 웹 브라우저는 모든 주요 인증 기관의 공개 키와 함께 설치됩니다. 이 공개 키를 사용하여 웹 서버의 인증서가 실제로 신뢰할 수있는 인증 기관에 의해 서명되었는지 확인합니다. (출처 - https://qastack.kr/programming/188266/how-are-ssl-certificates-verified)
>
> 즉, 웹 브라우저는 내부적으로 CA 리스트와 함께 공개키가 포함된 인증서를 가지고 있다.





## HTTPS의 장단점

- HTTPS는 웹사이트의 무결성을 보호해준다. 웹 사이트와 사용자 브라우저 사이의 통신을 침입자가 건드리지 못하도록 한다. (침입자라함은, 악의가 있는 공격자는 물론이고, 합법이지만 통신에 침입하여 페이지에 광고를 삽입하는 경우도 해당한다.)
- 가벼운 웹 서핑이라면 HTTP도 상관없지만, 사용자의 정보를 웹 서버와 주고 받아야하는 경우라면 HTTP는 정보 유출의 위험성을 갖게 된다. HTTPS는 침입자가 웹사이트와 사용자 사이의 통신을 몰래 수신하는 것을 방지함으로써 보안을 강화해준다.
- `getUserMedia()`를 통한 사진 촬영이나 오디오 녹음, 프로그레시브 웹 앱과 같은 강력한 웹 플랫폼 신기능들은 실행하려면 사용자의 명시적인 권한 허락을 필요로 한다. [지오로케이션](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/Using_geolocation) API와 같은 오래된 API들도 실행할 때 권한이 필요하도록 업데이트되고 있는데, HTTPS는 이러한 새 기능과 업데이트된 API에 대한 권한 허락을 가능하게 한다.
- 네이버, 다음은 물론이고 구글 역시 검색 엔진 최적화(SEO: Search Engine Optimization) 관련 내용을 HTTPS 웹사이트에 대해서 적용하고 있다. 즉, 키워드 검색 시 상위 노출되는 기준 중 하나가 보안 요소이다.
- 모든 사이트에서 텍스트를 암호화해서 주고 받으면 과부하가 걸려 속도가 느려질 수 있다. 중요한 사이트는 HTTPS로 관리하고, 그렇지 않은 사이트는 HTTP를 사용한다.
- HTTPS를 지원한다고 해서 무조건 안전한 것은 아니다. 신뢰할 수 있는 CA 기업이 아니라 자체적으로 인증서를 발급할 수도 있고, 신뢰할 수 없는 CA 기업을 통해서 인증서를 발급받을 수도 있기 때문이다.



## 내가 다시 정리

프로젝트를 하면서 종종 들었던 생각이 비밀번호를 입력할 때 저장은 암호화 해서 진행이 되지만 중간 과정에서는 비밀번호가 그대로 노출이 되고 있어서 마음에 걸렸는데. 그 부분을 해결을 한 것이 HTTPS이다. 

HTTPS는 암호화 해서 정보를 전달하는데. 이때 이 암호를 푸는 키가 필요하다. 이 키는 고유키여야 하는데. 사용자는 불특정 다수이기 때문에 어려움이 발생한다. 

> HTTPS는 위와 같은 상황에서 페이지를 암호화한 키가 그 페이지를 보는 특정 사용자에게만 알려지도록 한다. HTTPS는 SSL이나 TLS 프로토콜을 통해 세션 데이터를 암호화하며, 기본 TCP/IP 포트는 443이고, SSL 프로토콜 위에서 HTTPS 프로토콜이 동작한다.
>
> **[참고] TLS**
>
> Transport Layer Security의 줄임말. 과거 SSL에서 발전하며 이름이 변경 된 것이다. 하지만 아직도 SSL이란 명칭이 많이 사용되고 있다.

이때 크게 공캐키 방식과 대칭키 방식이 있는데 

### 공개키 방식

- A키로 암호화를 하면 B키로 복호화를 할 수 있다.
- B키로 암호화를 하면 A키로 복호화를 할 수 있다.
- 둘 중 하나를 비공개키(Private Key) 혹은 개인키라 부르며, 이는 자신만 가지고 있고 공개되지 않는다.
- 나머지 하나를 공개키(Public Key)라고 부르며 타인에게 제공한다. 공개키는 유출이 되어도 비공개키를 모르면 복호화 할 수 없기 때문에 안전하다.

### 대칭키 방식

- 동일한 키로 암호화, 복호화가 가능하다.
- 대칭키는 매번 랜덤으로 생성되어 누출되어도 다음에 사용할 때는 다른 키가 사용되기 때문에 안전하다.
- 공개키보다 빠르게 통신할 수 있다.

공개키 방식은 인증기관이 존재하고 

대칭키 방식은 따로 없다. 

(자세하게는 아직 이해를 못한거 같다. )

