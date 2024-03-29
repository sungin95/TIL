 오늘의 cs문제

# GPU(Graphics Processing Unit)

###  GPU란 무엇일까? 1부

GPU는 보통 게임할 때 많이 쓰이는 것으로 알고 계실 텐데요, 그러다 보니 비싼 장비, 혹은 비싼 카드 정도로 알고 계신 분들이 많습니다.

하지만 GPU는 4차 산업혁명과 함께 AI나 가상화폐 채굴 등 여러분의 일상생활을 바꿀 필수 핵심 장비로 탈바꿈 중이랍니다.

과연 GPU는 어떤 구조와 특성을 가지고 있기에 여러 분야에서 쓰일까요?

 

### GPU란?

GPU의 정의부터 알아봅시다!

GPU는 **Graphic Processing Unit**(그래픽 처리 장치)의 약어로, 그래픽 처리, 특히 3D 모델링을 위한 프로세서로 탄생하였습니다.

1990년대 중반까지만해도 3D 그래픽은 주로 CPU로 구현하였으나,

게임 등의 수요가 높아짐에 따라 더 빠르고 실시간 그래픽 처리가 필요했습니다.

1999년 NVIDIA사에서 GeForce 256을 세계 최초의 GPU라고 판매하며 'GPU'라는 명칭이 대중적으로 사용되었습니다. 

1년 후인 2000년에는 AMD사에서 Radeon이라는 GPU를 출시하며 양사의 경쟁이 본격화되었습니다.

2019년 기준 점유율은 각각 NVIDIA(67.9%) vs. AMD(32.1%)로 치열한 경쟁을 이어오고 있습니다.

([biz.chosun.com/site/data/html_dir/2019/10/06/2019100601698.html](https://biz.chosun.com/site/data/html_dir/2019/10/06/2019100601698.html))

 

### CPU vs. GPU

우리가 잘 알고 있는 CPU와 GPU는 무엇이 다른 것일까요? 먼저, CPU의 특징부터 알아보겠습니다.

CPU는 엄청 똑똑한 인간의 뇌와 같습니다.

CPU의 연산을 담당하는 연산장치(ALU)는 구조가 매우 복잡하고, 각종 제어 처리를 담당하고 있습니다.

그래서 명령어가 입력된 순서로 출력하는 직렬 처리 방식 및 복잡한 계산에 대한 빠른 처리가 가능합니다. 

그에 비해 GPU는 연산 장치(ALU)의 구조가 단순하고, 작은 제어/캐시 영역을 가집니다. 그리고 다수의 코어로 이루어져 있습니다.

이러한 구조적인 특징으로 인해, 여러 개의 코어를 동시에 병렬로 작동시켜 부동 소수점 연산 등 특정 단순 계산을 빠르게 할 수 있습니다.

그렇기에 다량의 병렬연산이 필요한 3D 렌더링이나, 딥러닝, 블록체인 등에 GPU가 사용되고 있으며 연산을 가속해주기에 **'가속기'**라는 명칭으로 불리기도 합니다.

 

#### 마무리

이번 글에서는 GPU에 대한 내용과 CPU와의 차이를 알아보았습니다.

아직 CPU와 GPU에 대한 이해가 어려우시다면! 아래 Youtube링크로 들어가시면 조금 더 직관적으로 이해할 수 있으실 거예요^^

다음 글에서는 Cloud에서 주로 쓰이는 GPU의 종류에 대해서 알아보도록 하겠습니다!

[출처](https://tech.ktcloud.com/17)



# 내가 정리

CPU란 엄청 똑똑한 뇌이고, GPU란 똑똑하지 않은 그냥 뇌입니다. 그러면 당연히 CPU가 좋고 GPU가 나쁜것인가? 라고 생각 할 수 있지만, 사람은 언제나 한정적인 자원을 통해 살아가야 하는 존재입니다. CPU는 똑똑하지만 많은 자원을 사용해야 합니다. 그런데 오늘날 하나의 딥은 문제보다는 다수를 여러 문제를 처리해야 하는 상황이 발생했는데. 대표적인 예로 게임 그래픽, 블록체인, 딥러닝 가 있습니다. 이러한 문제를 해결하는 데에는 한명의 천재보다는 평범한 여러명이 더 효율이 좋기 때문에 GPU를 많이 사용합니다. 



[CPU관련자료](https://www.youtube.com/watch?v=Fg00LN30Ezg)



[GPU관련자료](https://www.youtube.com/watch?v=ZdITviTD3VM)