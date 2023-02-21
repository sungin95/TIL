# IPC란?

GPT에게 물어보니까

IPC stands for Inter-Process Communication, which refers to the mechanisms and techniques used by different processes to communicate and exchange information with each other. 

IPC는 Inter Process Communication의 약자로, 메커니즘과 기술을 말한다. / 서로간의 다른 프로세스와의 통신과 정보 교환에서 사용되는 

The goal of IPC is to allow processes to synchronize and coordinate their actions to achieve a common goal. 

IPC의 목표는 프로세스에게 ~을 허용하는 것이다. / 동기화와 공통의 목표를 달성하는 행동을 조직화를 

IPC can be implemented in several ways, including shared memory, message passing, pipes, and sockets.

IPC는 몇가지 방법으로 구현 할 수 있다. / 메모리 공유와 메시지 전달, 파이프와 소켓을 포함한 



why use IPC?

IPC is used to facilitate communication and coordination between separate processes, which can run concurrently in a computer system. 

IPC는 ~에 사용된다/ 용이한 통신과 분리된 프로세스 사이를 조정하기 위해/  컴퓨터 시스템 안에서 동시에 운영 될 수 있게

Some common use cases for IPC include:

IPC의 일반적 사용 사레는/ 다음과 같다. 

1. Sharing data: IPC can be used to share data between processes, allowing them to exchange information and coordinate their actions.
   데이터 공유: IPC는 프로세스 간의 데이터 공유를 사용 할 수 있고, 그것들이 정보를 교환하고, 작업을 조정 하는 것을 할 수 있게 한다.
2. Resource sharing: IPC can be used to share resources, such as memory or file descriptors, between processes.
   리소스 공유: IPC는 리소스를 공유 할 수 있다/ 프로세스 간에 메모리 or 파일 설명자?를 
3. Concurrent processing: IPC can be used to divide a large task into smaller sub-tasks, which can be executed concurrently by separate processes to improve performance.
   동시 처리: IPC는 큰 작업을 보다 작은 하위 작업으로 나눌 수 있고, 동시에 실행 할 수 있다/ 성능을 향상 시키는 프로세스를 분리해서 
4. Decoupling processes: IPC can be used to decouple processes from each other, allowing them to evolve and change independently without affecting the others.
   디커플링 프로세스: IPC는 서로 다른 비동기화 ~를 허용하는 프로그램을 사용해서, 그것이 다른 영향 없이 독립적으로 진화하는 것을

Overall, IPC is a crucial technique for building complex, multi-process systems that can perform complex tasks more efficiently and effectively.

전반적으로, IPC는 중대한 기술이다. / 복합적으로 짓기 위해/ ~하는 여러 프로세스 시스템을/ 복합적인 일을 보다 효율적이고 효과적으로 



[출처](https://velog.io/@yanghl98/OS%EC%9A%B4%EC%98%81%EC%B2%B4%EC%A0%9C-IPC%EB%9E%80)

### IPC(Inter Process Communication)란?

#### 정의

> **IPC = 프로세스 간 통신**
> 프로세스들끼리 서로 데이터를 주고받는 행위 또는 그에 대한 방법을 뜻한다.

![img](https://velog.velcdn.com/images%2Fyanghl98%2Fpost%2F05cc6716-d859-43cb-b2f3-6f4c823398d9%2Fimage.png)

위 그림처럼 Process는 완전히 독립된 실행객체이다. 서로 **독립되어 있다**는 것은 다른 프로세스의 영향을 받지 않는다는 장점이 있다. 그러나 독립되어 있는 만큼 별도의 설비가 없이는 서로간에 통신이 어렵다는 문제가 있게 된다.

이를 위해서 **커널 영역**에서 IPC라는 내부 프로세스간 통신을 제공하게 되고, 프로세스는 커널이 제공하는 IPC설비를 이용해서 프로세스간 통신을 할 수 있게 된다.

- 커널(Kernel)

  이란?

  > 운영체제 자체도 소프트웨어이기 때문에 메모리에 올라가야 사용할 수 있다. 하지만 메모리 공간의 제약으로 운영체제 중 항상 필요한 부분만을 메모리에 올려놓고, 그렇지 않은 부분은 필요할 때 메모리에 올려서 사용하게 된다. 이 때 메모리에 상주하는 운영체제의 부분을 커널이라 한다. (보통은 운영체제라고 하면 커널을 말하게 된다.)
  >
  > 즉, 커널은 메모리에 상주하는 부분으로써 **운영체제의 핵심적인 부분**을 뜻한다.



### IPC의 종류

#### 1. 메시지 전달 (Message Passing)

커널이 제공하는 API를 이용해서 커널 공간을 통해 통신한다. **메시지 큐(Mesage Queue)**를 사용하여 송신 프로세스는 큐에 enqueue, 수신 프로세스는 큐에 dequeue 하며 상호간 통신한다. 메시지 큐는 커널 단에서 관리된다.

- **파이프** (쉘에서 사용하는 그 파이프임)

- **소켓 (TCP/IP)** - 로컬에서도 통신이 가능하며 원격에서도 통신이 가능하다. (IP : 127.0.0.1일 경우 로컬에서 패킷을 통해 프로세스끼리 통신하기도 한다.)

  

#### 2. 메모리 공유 (Shared Memory)

프로세스끼리 **특정 공통의 메모리 영역을 공유**하며 상호간 통신하는 방법이다.

**데이터 자체를 공유**하도록 지원하며, 한 프로세스에서 변경한 메모리 공간의 내용을 다른 프로세스에서 접근할 수 있다. 공유 메모리는 커널에서 관리된다.



#### 그림으로 이해

![img](https://velog.velcdn.com/images%2Fyanghl98%2Fpost%2F9d620bb0-54a2-48bd-b30f-d4f0fc4d0303%2Fimage.png)

- 왼쪽 : `Message Passing` 방법, 오른쪽 : `Shared Memory` 방법

  

#### 기타

이러한 IPC 통신에서 프로세스 간 데이터를 동기화하고 보호하기 위해 **세마포어(Semaphore)**와 **뮤텍스(Mutex)**를 사용한다. (공유된 자원에 한번에 하나의 프로세스만 접근시킬 때)

### 출처

https://jwprogramming.tistory.com/54
https://goodmilktea.tistory.com/23

[출처](https://jwprogramming.tistory.com/54)

**1) PIPE (익명 PIPE)**



![img](https://t1.daumcdn.net/cfile/tistory/247CBC4357187A3411)

\- 위 그림은 PIPE의 작동원리를 보여줍니다. 파이프는 두 개의 프로세스를 연결하게 되고, 하나의 프로세스는 데이터를 쓰기만, 다른 하나는 데이터를 읽기만 할 수 있습니다. 한쪽 방향으로만 통신이 가능한 파이프의 특징 때문에 Half-Duplex(반이중) 통신이라고 부르기도 합니다.

PIPE와 같은 반이중 통신의 경우 하나의 통신선로는 읽기나 쓰기 중 하나만 가능하므로 만약 읽기와 쓰기, 즉 송/수신을 모두 하기 원한다면 두개의 파이프를 만들어야만 가능해집니다.



PIPE는 매우 간단하게 사용할 수 있다는 장점이 있습니다. 만약 한쪽 프로세스가 단지 읽기만 하고 다른 쪽 프로세스는 단지 쓰기만 하는, 단순한 데이터 흐름을 가진다면 고민 없이 PIPE를 사용하면 됩니다. 단점은 반이중 통신이라는 점으로 만약 프로세스가 읽기와 쓰기 통신 모두를 해야 한다면 PIPE를 두개 만들어야 하는데, 구현이 꽤나 복잡해 질 수 있습니다. 만약 전이중 통신을 고려해야될 상황이라면 PIPE는 좋은 선택이 아니라고 보여집니다.



**2) Named PIPE(FIFO)**

\- 익명 파이프(Pipe)는 통신을 할 프로세스가 명확하게 알 수 있는 경우 사용합니다. 예를 들어 자식과 부모 프로세스간 통신의 경우에 사용할 수 있으며, Named PIPE는 전혀 모르는 상태의 프로세스들 사이의 통신의 경우 사용합니다. Named PIPE는 PIPE의 단점 중 같은 PPID(같은 부모 프로세스)를 가지는 프로세스들 사이에서만 통신이 가능하지만, Named PIPE는 그 부분을 해결한, PIPE의 확장이라고 할 수 있을 것입니다. **Named PIPE**는 **부모 프로세스와 무관하게 전혀 다른 모든 프로세스들 사이에서 통신이 가능**한데 그 이유는 프로세스 통신을 위해 이름이 있는 파일을 사용하기 때문입니다. Named PIPE의 생성은 mkfifo를 통해 이뤄지는데, mkfifo가 성공하면 명명된 파일이 생성됩니다.

단점으로는, Named PIPE도 PIPE의 또 다른 단점인 읽기/쓰기가 동시에 가능하지 않으며, read-only, write-only만 가능합니다. 하지만 통신선로가 파일로 존재하므로 하나를 읽기 전용으로 열고 다른 하나를 쓰기전용으로 영어서 이러한 read/write문제를 해결 할 수 있습니다. 호스트 영역의 서버 클라이언트 간에 전이중 통신을 위해서는 결국 PIPE와 같이 두개의 FIFO파일이 필요하게 됩니다.



**3)Message Queue**

\- Queue(큐)는 선입선출의 자료구조를 가지는 통신설비로 커널에서 관리합니다. 입출력 방식으로 보자면 위의 Named PIPE와 동일하다고 볼 수 있을 것입니다. Named PIPE와 다른 점이라면 Name PIPE가 데이터의 흐름이라면 메시지 큐는 **메모리 공간**이라는 점입니다. 파이프가 아닌, 어디에서나 물건을 꺼낼 수 있는 컨테이너 벨트라고 보면 될 것입니다.

메시지 큐의 장점은 컨테이너 벨트가 가지는 장점을 그대로 가지게 됩니다. 컨테이너 벨트에 올라올 물건에 라벨을 붙이면 동시에 다양한 물건을 다룰 수 있는 것과 같이, **메시지 큐에 쓸 데이터에 번호를** **붙임**으로써 여러 개의 프로세스가 동시에 데이터를 쉽게 다룰 수 있습니다.



**4)Shared Memory(공유 메모리)**

\- 데이터를 공유하는 방법에는 크게 두 가지가 있습니다. 하나는 통신을 이용해서 데이터를 주고 받는 것이고 다른 하나는 **데이터를 아예 공유, 즉 함께 사용하는** **것**입니다. PIPE, Named PIPE, Message Queue가 통신을 이용한 설비라면, **Shared Memory**는 **공유메모리가 데이터 자체를 공유하도록** **지원**하는 설비입니다.

프로세스는 자신만의 메모리 영역을 가지고 있습니다. 이 메모리 영역은 다른 프로세스가 접근해서 함부로 데이터를 읽거나 쓰지 못하도록 커널에 의해서 보호가 되는데, 만약 다른 다른 프로세스의 메모리 영역을 침범하려고 하면 커널은 침범 프로세스에 SIGSEGV(경고 시그널 - 할당된 메모리의 범위를 벗어나는곳에서 읽거나, 쓰기를 시도할 때 발생) 을 보내게 됩니다.



다수의 프로세스가 동시에 작동하는 Linux 운영체제의 특성상 프로세스의 메모리 영역은 반드시 보호되어져야 합니다. 그렇지만 메모리 영역에 있는 데이터를 다른 프로세스도 사용할 수 있도록 해야할 경우도 필요할 것입니다. PIPE 등을 이용해서 데이터 통신을 이용하여 데이터를 전달하는 방법도 있겠지만, Thread에서 처럼 메모리 영역을 공유한다면 더 편하게 데이터를 함께 사용할 수 있을 것입니다. 

Shared Memory(공유 메모리)는 **프로세스간 메모리 영역을 공유해서 사용할 수 있도록** **허용**합니다. 프로세스가 공유 메모리 할당을 커널에 요청하면 커널은 해당 프로세스에 메모리 공간을 할당해줍니다. 이후 어떤 프로세스건 해당 메모리영역에 접근할 수 있습니다.

공유메모리는 중개자가 없이 곧바로 메모리에 접근할 수 있기 때문에 다른 모든 **IPC****들 중에서 가장 빠르게** **작동**할 수 있습니다.



**5) Memory Map**

\- Memory Map도 Shared Memory(공유메모리)공간과 마찬가지로 메모리를 공유한다는 측면에 있어서는 서로 비슷한 측면이 있습니다. 차이점은 Memory Map의 경우 **열린파일을 메모리에 맵핑시켜서,** **공유**한다는 점일 것입니다. 파일은 시스템의 전역적인(모두 공유할 수 있는) 자원이므로 서로 다른 프로세스들끼리 데이터를 공유하는데 문제가 없을 것임을 예상할 수 있습니다.



**6) Socket**

\- Socket은 프로세스와 시스템의 기초적인 부분이며, 프로세스 들 사이의 통신을 가능하게 합니다. sys/socket.h>라는 헤더를 이용하여 사용할 수 있으며, 같은 도메인에서의 경우에서 연결 될 수 있습니다. 소켓을 사용하기 위해서는 생성해주고, 이름을 지정해주어야 합니다. 또한 domain과 type, Protocol을 지정해 주어야 합니다. 서버 단에서는 bind, listen, accept를 해주어 소켓 연결을 위한 준비를 해주어야 하고 , 클라이언트 단에서는 connect를 통해 서버에 요청하며, 연결이 수립 된 이후에는 Socket을 send함으로써 데이터를 주고 받게 됩니다. 연결이 끝난 후에는 반드시 Socket 을 close()해주어야 하며, Socket과 관련해서는 이후 네트워크 부분에서 자세히 다루도록 하겠습니다.

**7) Semaphore**

\- Semaphore는 Named PIPE, PIPE, Message Queue와 같은 다른 IPC설비들이 대부분 프로세스간 메시지 전송을 목적으로 하는데 반해, Semaphore는 프로세스 간 데이터를 동기화 하고 보호하는데 그 목적을 두게 됩니다. 프로세스간 메시지 전송을 하거나, 혹은 Shared Memory를 통해서 특정 데이타를 공유하게 될 경우 발생하는 문제가 공유된 자원에 여러개의 프로세스가 동시에 접근하면 안되며, 단지 한번에 하나의 프로세스만 접근 가능하도록 만들어줘야 할 것이며, 이 때 사용되는 것이 Semaphore입니다. 자세한 부분은 이전에 포스팅했던 Semaphore와 Mutex 부분에서 다루고 있으므로 생략하도록 하겠습니다.



[출처](https://parkhongbeen.github.io/2020/06/04/%ED%94%84%EB%A1%9C%EC%84%B8%EC%8A%A4%EC%99%80IPC/)

## IPC(InterProcess Communication)

> 프로세스들 간에 데이터 및 정보를 주고받기 위한 메커니즘

### 프로세스간 커뮤니케이션

프로세스는 다른 프로세스 공간에 접근할 수 없습니다.

### 프로세스간 통신의 필요성

성능을 높이기 위해 여러 프로세스를 만들어서 동시에 실행합니다.이 때 프로세서간 상태 확인 및 데이터 송수신이 필요합니다.

### 다양한 IPC기법

File사용, MessegeQueue, SharedMemory, Pipe, Signal, Semaphore, Socket

![image-20200219193905433](https://user-images.githubusercontent.com/53684676/83717693-54f24b80-a66e-11ea-9b00-a06aad9f0bef.png)

### 정리

여러 프로세스를 동시에 실행을 통한 성능 개선, 복잡한 프로그램을 위해 프로세스간 통신이 필요하다. 하지만 프로세스간의 공간이 분리되어 있다. 프로세스간 통신을 위해 특별한 기법은 IPC(InterProcessCommunication)이다. 대부분의 IPC기법은 결국 커널공간을 활용하는 것이다. / 이유는 커널 공간은 공유하기 때문이다.