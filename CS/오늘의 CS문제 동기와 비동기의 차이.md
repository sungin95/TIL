오늘의 CS문제: 동기와 비동기의 차이

# 동기와 비동기의 차이

## 정의

우선 동기와 비동기의 정의를 보자면 아래와 같이 정의 할 수 있을거 같습니다. 



> ## 💡동기(synchronous)

- 동기는 데이터의 요청과 결과가 한 자리에서 동시에 일어나는것을 말합니다.

**요청을 하면 시간이 얼마나 걸리던지 요청한 자리에서 결과가 주어져야 합니다.**

*사용자가 데이터를 서버에게 요청한다면 그 서버가 데이터 요청에 따른 응답을 사용자에게 다시 리턴해주기 전까지 사용자는 다른 활동을 할 수 없으며 기다려야만합니다.*



> ## 🕯 비동기(Asynchronous)

- 비동기는 동시에 일어나지 않는다는 의미입니다.

  **요청한 결과는 동시에 일어나지 않을거라는 약속입니다.**

*서버에게 데이터를 요청한 후 요청에 따른 응답을 계속 기다리지 않아도되며 다른 외부 활동을 수행하여도되고 서버에게 다른 요청사항을 보내도 상관없습니다*

[출처](https://velog.io/@slobber/%EB%8F%99%EA%B8%B0%EC%99%80-%EB%B9%84%EB%8F%99%EA%B8%B0%EC%9D%98-%EC%B0%A8%EC%9D%B4)



위 정의는 잘 정리는 되어 있다고는 생각을 하지만, 결국 이 공부의 목적은 사용에 있다고 생각을 하는데. 위 정의를 통해 그래서 언제 동기를 쓰고 비동기를 쓰지?라는 질문에 답을 하지 못할 거 같습니다. 그래서 사용할 때 고려해야 될 부분들의 저의 경험을 위주로 정리를 해 보았습니다. 



## 사용하는 상황

### 동기

페이지를 이동하는 상황에서 주로 사용 하였습니다. 

동기를 사용하게 되면 기본적으로 전체 화면이 새로 고침이 되고 서버의 응답이 이루어질 때까지 계속 대기해야만합니다. 이로인해 작업중이라면 하는 일이 약간은 끊기는 느낌을 받게 됩니다. 그래서 현재 페이지에서 작업중이 상황에서 버튼을 동기로 만드는 일은 피하는게 좋았던거 같습니다. 반대로 페이지를 이동하는 상황에서는 동기로 구현하는 것이 가장 좋다고 생각합니다. 



### 비동기

현재 페이지에서 여전히 작업을 하고 있을때

비동기의 핵심은 페이지의 부분을 새롭게 하는 기능이라고 생각을 합니다. 이 기능 덕분에 현재 화면 or 스크롤을 상태등을 유지하면서 서버로부터 새로운 자료를 요청 할 수 있고 유저는 현재 하는 작업을 더욱 몰입 할 수 있게 됩니다. 

다만, 구현은 많이 까다롭습니다. js에서 서버로 요청을 보내서 js가 응답을 받고 응답받은 값을 통해서 js의 명령어를 통하여 HTML을 변화를 시켜야 하기 때문이죠. 



