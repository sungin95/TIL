# TCP/IP

[이해하면 인생이 바뀌는 TCP 송/수신 원리](https://www.youtube.com/watch?v=K9L9YZhEjC0&t=39s)

데이터 통신의 전반적인 원리를 설명해준 명강의!!!

### TCP / IP란?



![TCP IP](https://blog.kakaocdn.net/dn/byluys/btqNkPqmM78/TYlmUkLNpV2jSReWTA5HUk/img.png)



TCP/IP(Transmission Control Protocol/Internet Protocol)는 데이터가 의도된 목적지에 닿을 수 있도록 보장해주는 통신 규약입니다. TCP / IP는 이름에서 알 수 있듯 TCP / IP에는 두가지 프로토콜로 이루어져 있으며 인터넷으로 디바이스를 연결하는 네트워크 프로토콜의 집합이며 개별적인 네트워크 프로토콜로 사용될 수도 있습니다. TCP / IP는 인터넷의 기본 통신 언어입니다. 기본적으로 TCP / IP를 사용하면 한 컴퓨터가 데이터 패킷을 컴파일하고 올바른 위치로 전송하여 인터넷을 통해 다른 컴퓨터와 통신 할 수 있습니다. 

> **프로토콜이란?**
> 컴퓨터와 네트워크 기기가 상호간에 통신하기 위해서는 서로 같은 방법으로 통신하지 않으면 안됩니다. 어떻게 상대를 찾고, 어떻게 상대에게 이야기를 시작하고, 어떤 언어로 이야기하며 어떻게 이야기를 종료할까와 같은 규칙을 결정할 필요가 있습니다. 위와 같이 서로다른 하드웨어와 운영체제 등이 서로 통신을 하기위해 모든 요소에 규칙이 필요합니다. 이런 규칙을 프로토콜이라고 부릅니다. 

 

### TCP란?

최상위 계층인 TCP는 많은 양의 데이터를 가져 와서 패킷으로 컴파일 한 다음 동료 TCP 계층에서 수신하도록 전송하여 패킷을 유용한 정보 / 데이터로 바꾸는 역할을 합니다. TCP는 전달받은 패킷을 재조립하고, 패킷에 손상이 있거나 손실된 패킷이 있다면 재전송을 요청하는 패킷을 전송하여 재전송 받습니다.

※ 패킷 : 데이터를 일정한 크기로 자른 단위로 인터넷에서 정보를 전달하는 단위

 

### IP란?

IP는 Internet Protocol의 줄임말로, 인터넷에서 컴퓨터의 위치를 찾아서 데이터를 전송하기 위해 지켜야 할 규약입니다. 전 세계 수억대의 컴퓨터가 인터넷을 하기 위해서는 서로의 정체를 알 수 있도록 특별한 주소를 부여했는데 이 주소를 IP주소라고 합니다.IP는 4개의 숫자로 구성되며 숫자의 크기에 따라 IPv4(32비트, 각 숫자는 1바이트), IPv6(128비트, 각 숫자는 4바이트)로 나뉩니다. 일반적으로는 IPv4는 10진수로 표현하며 각 자리는 .으로 구분하고, IPv6는 각 자리를 4자리 16진수로 표현하며 각 자리는 :로 구분합니다. 맨 아래 계층인 IP는 올바른 목적지를 찾는 패킷 GPS 역할을합니다. 지도의 관점에서 IP를 생각하면 IP 계층은 고속도로에서 운전하는 자동차와 마찬가지로 각 패킷은 게이트웨이 컴퓨터 (도로 표지판)를 통과하여 패킷을 올바른 목적지로 전달하는 역할을합니다. 



 

##  TCP / IP 의 4계층 



![TCP IP 4계층](https://blog.kakaocdn.net/dn/d64HML/btqNiWKw4nX/JW5zNwWZ4KP53MAhwWuOIK/img.png)



TCP/IP가 많이 사용되면서 흔히 사용되던 OSI 7계층을 더욱 추상화 한 TCP/IP 4계층이 등장했습니다. TCP / IP에는 위와 같이 4개의 층이 있습니다.

 

1. 네트워크엑세스 계층(물리계층, 데이터링크계층)
2. 인터넷계층(네트워크계층),
3. 전송계층(전송계층)
4. 응용계층(세션계층, 표현계층, 응용계층)

 

### 네트워크 액세스 계층(Network Access Layer)

1. OSI 7계층의 물리계층과 데이터 링크 계층에 해당
2. TCP/IP 패킷을 네트워크 매체로 전달하는 것과 네트워크 매체에서 TCP/IP 패킷을 받아들이는 과정을 담당
3. 에러 검출 기능(Detecting errors), 패킷의 프레임화(Fraimg packets)
4. 네트워크 접근 방법, 프레임 포맷, 매체에 대해 독립적으로 동작하도록 설계.
5. 물리적인 주소로 MAC을 사용
6. LAN, 패킷망, 등에 사용됨

 

### 2계층 인터넷 계층(Internet Layer)

1. OSI 7계층의 네트워크 계층에 해당
2. 어드레싱(addressing), 패키징(packaging), 라우팅(routing) 기능을 제공
3. 네트워크상 최종 목적지까지 정확하게 연결되도록 연결성을 제공하게 됨.
4. 프로토콜 종류 – IP, ARP, RARP

 

### 3계층 전송 계층(Transport Layer)

1. OSI 7계층의 전송 계층에 해당
2. 애플리케이션 계층의 세션과 데이터그램(datagram) 통신서비스 제공
3. 통신 노드 간의 연결을 제어하고, 신뢰성 있는 데이터 전송을 담당한다.
4. 프로토콜 종류 – TCP, UDP

[[Network\] TCP / UDP의 개념과 특징, 차이점](https://coding-factory.tistory.com/614)

 

### 4계층 응용 계층(Application Layer)

1. OSI 7계층의 세션 계층, 표현 계층, 응용 계층에 해당한다.
2. 프로그램(브라우저)가 직접 인터액트하는 레이어. 데이터를 처음으로 받는곳
3. 다른 계층의 서비스에 접근할 수 있게 하는 애플리케이션을 제공
4. 애플리케이션들이 데이터를 교환하기 위해 사용하는 프로토콜을 정의
5. HTTP, SMTP등의 프로토콜을 가진다.
6. TCP/UDP 기반의 응용 프로그램을 구현할 때 사용한다.
7. 프로토콜 종류 – FTP, HTTP, SSH



[출처](https://coding-factory.tistory.com/613)



## 전송 계층에서 사용되는 프로토콜 (TCP / UDP)

 



![네트워크 모델](https://blog.kakaocdn.net/dn/ebbB00/btqNgswn5Ce/bbnxlGNJV48aWcN8jT7mZk/img.png)



TCP와 UDP는 OSI 표준모델과 TCP/IP 모델의 **전송계층**에서 사용되는 프로토콜입니다. 전송계층은 송신자와 수신자를 연결하는 통신 서비스를 제공하고 IP에 의해 전달되는 패킷의 오류를 검사하며 재전송 요구 제어등을 담당하는 계층입니다. 쉽게 말해 데이터의 전달을 담당한다고 생각하시면 됩니다. TCP와 UDP는 포트 번호를 이용하여 주소를 지정하는것과 데이터 오류검사를 위한 체크섬 존재하는 두가지 공통점을 가지고 있지만 정확성(TCP)을 추구할지 신속성(UDP)을 추구할지를 구분하여 나뉩니다.

 

데이터를 중요하게 생각하여 확실히 주고받고 싶을 때는 ‘TCP(Transmission Control Protocol)’를 사용합니다. TCP는 통신할 컴퓨터끼리 ‘보냈습니다’, ‘도착했습니다’라고 서로 확인 메시지를 보내면서 데이터를 주고받음으로써 통신의 신뢰성을 높입니다. 웹이나 메일, 파일 공유 등과 같이 데이터를 누락시키고 싶지 않은 서비스는 TCP를 사용하고 있습니다.

 

그에 반해 데이터의 신뢰성은 제쳐두고 어쨌든 빨리 보내고 싶을 때는 ‘UDP(User Datagram Protocol)’를 사용합니다. UDP는 데이터를 보내면 그것으로 끝이므로 신뢰성은 없지만 확인 응답과 같은 절차를 생략할 수 있으므로 통신의 신속성을 높입니다. VoIP(Voice over IP)와 같은 시간 동기가 필요한 특히 속도를 필요로 하는 서비스들이 UDP를 사용하고 있습니다. 

 

> **포트 번호로 서비스를 식별한다.
> **
> TCP와 UDP는 ‘포트 번호’라는 숫자를 이용하여 컴퓨터 안의 어떤 서비스(애플리케이션)에게 데이터를 전달하면 좋은지를 식별합니다. 포트 번호는 ‘0~65535’(16비트 분)까지의 숫자로 되어 있으며, 범위에 따라 용도가 정해져 있습니다. ‘0~1023’은 ‘잘 알려진 포트(well-known port)’라고 해서 웹 서버나 메일 서버 등과 같이 일반적인 서버 소프트웨어가 클라이언트의 서비스 요청을 대기할 때 사용합니다. ‘1024~49151’은 ‘등록된 포트(registered port)’로, 제조업체의 독자적인 서버 소프트웨어가 클라이언트의 서비스 요청을 대기할 때 사용합니다. ‘49152~65535’는 ‘동적 포트(dynamic port)’로, 서버가 클라이언트를 식별하기 위해 사용합니다.

[[기타\] TCP / IP란 무엇인가?](https://coding-factory.tistory.com/613)

 

##  TCP의 개념과 특징 



![TCP](https://blog.kakaocdn.net/dn/IVBAk/btqNlmuFIm3/je46XorKIeFVz93PbkxODk/img.png)



TCP(Trasmission Control Protocol)는 연결 지향적 프로토콜입니다. 연결 지향 프로토콜이란 클라이언트와 서버가 연결된 상태에서 데이터를 주고받는 프로토콜을 의미합니다. 클라이언트가 연결 요청(SYN 데이터 전송)을 하고, 서버가 연결을 수락하면 통신 선로가 고정되고, 모든 데이터는 고정된 통신 선로를 통해서 순차적으로 전달됩니다. 그렇기 때문에 TCP는 데이터를 정확하고 안정적으로 전달할 수 있습니다. TCP는 호스트간 신뢰성 있는 데이터 전달과 흐름제어를 합니다. TCP 프로토콜은 신뢰성 있는 데이터의 전송을 위해 확인작업을 거치는데 TCP는 패킷을 성공적으로 전송하면(ACK) 라는 신호를 날리고 만약에 ACK 신호가 제 시간에 도착하지 않으면 Timeout이 발생하여 패킷 손실이 발생한 패킷을 다시 전송해줍니다. TCP는 이렇게 데이터를 송신할때마다 확인 응답을 주고받는 절차가 있으므로 통신의 신뢰성이 올라갑니다. 주로 lient와 Server 또는 P2P Socket 통신 등, 네트워크를 사용한 통신을 할 때 TCP 통신을 많이 사용합니다.

 

### TCP의 단점

- 데이터로 보내기 전에 반드시 연결이 형성되어야함.
- 1 : 1 통신만 가능함.
- 고정된 통신 선로가 최단선(네트워크 길이)이 아닐경우 상대적으로 UDP보다 데이터 전송속도가 느림.

 

### TCP의 특징

1. 연결형 (connnection-oriented) 서비스로 연결이 성공해야 통신이 가능하다.
2. 데이터의 경계를 구분하지 않는다. (바이트 스트림 서비스)
3. 데이터의 전송 순서를 보장한다. (데이터의 순서 유지를 위해 각 바이트마다 번호를 부여)
4. 신뢰성있는 데이터를 전송한다. (Sequence Number, Ack Number를 통한 신뢰성 보장)
5. 데이터 흐름 제어(수신자 버퍼 오버플로우 방지) 및 혼잡 제어(패킷 수가 과도하게 증가하는 현상 방지)
6. 연결의 설정(3-way handshaking)과 해제(4-way handshaking)
7. 전이중(Full-Duplex), 점대점(Point to Point) 서비스
8. UDP보다 전송속도가 느리다.

 

### 3 way handshake 방식 (SYN, ACK)



![3way handshake](https://blog.kakaocdn.net/dn/c7IA52/btqNfrrcasU/B0UyfjyjKh1Ga6yQB3v2y0/img.jpg)



TCP 통신을 위한 네트워크 연결은 3 way handshake 이라는 방식으로 연결됩니다. 3 way handshake 방식은 서로의 통신을 위한 관문(port)을 확인하고 연결하기 위하여 3번의 요청/응답 후에 연결이 되는 것을 말합니다.(이 과정에서 가장 많은 시간이 소요되어 UDP방식보다 속도가 느려지는 주요 원인으로 지목됩니다.)

 

#### 연결 과정

1. Client에서 Server에 연결 요청을 하기위해 SYN 데이터를 보낸다.
2. Server에서 해당 포트는 LISTEN 상태에서 SYN 데이터를 받고 SYN_RCV로 상태가 변경된다.
3. 그리고 요청을 정상적으로 받았다는 대답(ACK)와 Client도 포트를 열어달라는 SYN 을 같이 보낸다.
4. Client에서는 SYN+ACK 를 받고 ESTABLISHED로 상태를 변경하고 서버에 ACK 를 전송한다.
5. ACK를 받은 서버는 상태가 ESTABLSHED로 변경된다. 

**위와 같이 3번의 통신이 정상적으로 이루어지면, 서로의 포트가 ESTABLISHED 되면서 연결이 됩니다.**

 

> **TCP state (netstat 명령어를 통해 확인가능)
>
> ****LISTEN :** 서버의 데몬이 떠서 접속 요청을 기다리는 상태
> **SYN-SENT :** 로컬의 클라이언트 어플리케이션이 원격 호스트에 연결을 요청한 상태
> **SYN_RECEIVED :** 서버가 원격 클라이언트로부터 접속 요구를 받아 클라이언트에게 응답을 하였지만 아직 클라이언트에게 확인 메시지는 받지 않은 상태
> **ESTABLISHED :** 3 way-handshaking 이 완료된 후 서로 연결된 상태
> **FIN-WAIT1, CLOSE-WAIT, FIN-WAIT2 :** 서버에서 연결을 종료하기 위해 클라이언트에게 종결을 요청하고 회신을 받아 종료하는 과정의 상태
> **TIME-WAIT :** 연결은 종료되었지만 분실되었을지 모를 느린 세그먼트를 위해 당분간 소켓을 열어두고 있는 상태
> **CLOSING :** 흔하지 않지만 주로 확인 메시지가 전송도중 분실된 상태 
> **CLOSED :** 완전히 종료

 

### TCP 헤더 정보



![TCP Header](https://blog.kakaocdn.net/dn/cIt86U/btqNiVx6GmY/nPEo5ZZsFq71gFGqAxtvxK/img.png)



| **필드**                      | **크기** | **내용**                                                     |
| ----------------------------- | -------- | ------------------------------------------------------------ |
| 송수신자의 포트 번호          | 16       | TCP로 연결되는 가상 회선 양단의 송수신 프로세스에 할당되는 포트 주소 |
| 시퀀스 번호 (Sequence Number) | 32       | 송신자가 지정하는 순서 번호, 전송되는 바이트 수를 기준으로 증가 SYN = 1 : 초기 시퀀스 번호가 된다. ACK 번호는 이 값에 1을 더한값 SYN = 0 : 현재 세션의 이 세그먼트 데이터의 최초 바이트 값의 누적 시퀀스 번호 |
| 응답 번호 (ACK Number)        | 32       | 수신 프로세스가 제대로 수신한 바이트 수를 응답하기 위해 사용 |
| 데이터 오프셋 (Data Offset)   | 4        | TCP 세그먼트의 시작 위치를 기준으로 데이터의 시작 위치를 표현(TCP 헤더의 크기) |
| 예약 필드(Reserved)           | 6        | 사용을 하지 않지만 나중을 위한 예약 필드이며 0으로 채워져야한다. |
| 제어 비트(Flag Bit)           | 6        | SYN, ACK, FIN 등의 제어 번호                                 |
| 윈도우 크기(Window)           | 16       | 수신 윈도우의 버퍼 크기를 지정할 때 사용. 0이면 송신 프로세스의 전송 중지 |
| 체크섬(Checksum)              | 16       | TCP 세그먼트에 포함되는 프로토콜 헤더와 데이터에 대한 오류 검출 용도 |
| 긴급 위치(Urgent Pointer)     | 16       | 긴급 데이터를 처리하기 위함, URG 플래그 비트가 지정된 경우에만 유효 |

 

### TCP 제어비트 (Flag Bit) 정보

| 종류 | 내용                                                         |
| ---- | ------------------------------------------------------------ |
| ACK  | 응답 번호 필드가 유효한지 설정할때 사용하며 상대방으로부터 패킷을 받았다는 걸 알려주는 패킷. 클라이언트가 보낸 최초의 SYN 패킷 이후에 전송되는 모든 패킷은 이 플래그가 설정되어야 한다. |
| SYN  | 연결 설정 요구. 동기화 시퀀스 번호. 양쪽이 보낸 최초의 패킷에만 이 플래그가 설정되어 있어야 한다.TCP 에서 세션을 성립할 때 가장먼저 보내는 패킷, 시퀀스 번호를 임의적으로 설정하여 세션을 연결하는 데에 사용되며 초기에 시퀀스 번호를 보내게 된다. |
| PSH  | 수신 애플리케이션에 버퍼링된 데이터를 상위 계층에 즉시 전달할 때 사용 |
| RST  | 연결의 리셋이나 유효하지 않은 세그먼트에 대한 응답용으로 사용 |
| URG  | 긴급 위치를 필드가 유효한지 설정 (긴급한 데이터는 다른 데이터에 비해 우선순위가 높음) |
| FIN  | 세션 연결을 종료시킬 때 사용되며 더 이상 전송할 데이터가 없을 때 연결 종료 의사 표시 |

 

##  UDP의 개념과 특징 



![UDP](https://blog.kakaocdn.net/dn/db4ChG/btqNkfv2W6U/RPlPzrfgr0YbZUa7XLcrw1/img.png)



UDP(User Datagram Protocol)는 전송계층의 비연결 지향적 프로토콜입니다. 비연결 지향적이란 데이터를 주고받을 때 연결 절차를 거치지 않고 발신자가 일방적으로 데이터를 발신하는 방식을 의미합니다. 연결 과정이 없기 때문에 TCP보다는 빠른 전송을 할 수 있지만 데이터 전달의 신뢰성은 떨어집니다. UDP는 발신자가 데이터 패킷을 순차적으로 보내더라도 이 패킷들은 서로 다른 통신 선로를 통해 전달 될 수 있습니다. 먼저 보낸 패킷이 느린 선로를 통해 전송될 경우 나중에 보낸 패킷보다 늦게 도착할 수 있으며 최악의 경우 잘못된 선로로 전송되어 유실될 수도 있습니다. 이럴 경우 TCP와는 다르게 UDP는 중간에 패킷이 유실이나 변조가 되어도 재전송을 하지 않습니다. 

 

### UDP의 단점

- 데이터의 신뢰성이 없다.
- 의미있는 서버를 구축하기위해서는 일일이 패킷을 관리해주어야 한다.

 

### UDP의 특징

1. 비연결형 서비스로 연결 없이 통신이 가능하며 데이터그램 방식을 제공한다.
2. 데이터 경계를 구분한다. (데이터그램(datagram) 서비스)
3. 정보를 주고 받을때 정보를 보내거나 받는다는 신호절차를 거치지 않는다.
4. 신뢰성 없는 데이터를 전송한다. (데이터 재전송과 데이터 순서 유지를 위한 작업을 하지 않는다.
5. 패킷관리가 필요하다.
6. 패킷 오버헤드가 적어 네트워크 부하가 감소되는 장점.
7. 상대적으로 TCP보다 전송속도가 빠르다.

 

### UDP의 헤더정보

| **필드**           | **크기** | **내용**                                 |
| ------------------ | -------- | ---------------------------------------- |
| 송신자의 포트 번호 | 16       | 데이터를 보내는 어플리케이션의 포트 번호 |
| 수신자의 포트 번호 | 16       | 데이터를 받을 어플리케이션의 포트 번호   |
| 데이터의 길이      | 16       | UDP 헤더와 데이터의 총 길이              |
| 체크섬(Checksum)   | 16       | 데이터 오류 검사에 사용                  |

 

 

##  TCP / UDP 간략비교 

### 공통점

| **TCP와 UDP의 공통점**              |
| ----------------------------------- |
| 포트 번호를 이용하여 주소를 지정    |
| 데이터 오류 검사를 위한 체크섬 존재 |

 

### 차이점

|                    | **TCP**            | **UDP**                        |
| ------------------ | ------------------ | ------------------------------ |
| **연결방식**       | 연결형서비스       | 비 연결형 서비스               |
| **패킷 교환 방식** | 가상 회선 방식     | 데이터그램 방식                |
| **전송 순서**      | 전송 순서 보장     | 전송 순서가 바뀔 수 있음       |
| **수신 여부 확인** | 수신 여부를 확인함 | 수신 여부를 확인하지 않음      |
| **통신 방식**      | 1:1 통신만 가능    | 1:1 / 1:N / N:N 통신 모두 가능 |
| **신뢰성**         | 높음               | 낮음                           |
| **속도**           | 느림               | 빠름                           |

 

[출처](https://coding-factory.tistory.com/614)



# 내가 정리

결국 TCP/IP의 핵심은 잘 보내졌는지 체크한다는 것이다. 이 기능 덕분에 데이터의 소실 없이 원하는 목적지까지 잘 보낼 수 있다. 다만, 이것을 확인하는 과정에서 속도지연문제가 발생한다. 