## ```$ git push```

### 학습목표: 원격저장소를 만들고, 로컬저장소의 커밋을 push한다. 

#### 1. 깃허브 저장소 만들기. 

깃허브에서 새로운 저장소를 만들면 

https://gitbub.com/kdt-live(GitHub Usermane)/test.git(test.git)

이런 식으로 주소가 뜬다. (미리 유저네일을 바꾸도록 한 것은 주소 정보가 바뀌기 떄문이다. )

#### 2. 원격저장소 경로 설정

참고: $는 터미널에서 입력하라는 듯이다. 

$ git remote add origin https://gitbub.com/kdt-live(GitHub Usermane)/test.git(test.git)

​        원격저장소 추가해 Origin으로 

  => 깃아 원격저장소 추가해줘 오리진이라는 이름으로 URL을

$ git remote -v 하면 설정 확인 가능

주의! 붙여넣기 단축키 ctrl + v가 아니라. 우클릭입니다.(이건 vscode에서는 상관없는데 직접 git bush에 들어갈때는 적용이 된다. ) 

#### 3. 현재 버전 push 해 주기

```$ git remote add origin master``` 을 해 주면 깃허브에서 연결을 할 거냐는 메세지를 보내는데. 

파란버튼 누르고 비밀번호를 다시 눌려 인증과정을 거치고 아까 화면을 새로고침하면 정상 연결이 된 것을 확인 할 수 있다. 

#### 자주하는 실수!

1. 커밋이 없는 경우 실행이 되지 않는다. 

2. push를 했을 떄, 이미 가장 최신 버전이라면 이 역시 실행 되지 않는다. 

   요약: ```git add .``` or ```git commit -m "커밋제목"``` 이 잘 되었는지 ```git status```를 통해 잘 확인하자!

### error: remote origin already exists.

위 대로 했음에도 이런 오류가 뜬다면 

해결방법은 간단합니다. 위와 같이 원격 저장소와의 연결이 되어 있다고 하니 기존의 연결을 끊고 새로 올리고 싶은 곳에 소스코드를 올리면 됩니다.

**1.** git remote remove origin 명령어를 입력해서 기존에 연결되어 있는 원격 저장소와의 연결을 끊어줍니다.

**2.** git remote add origin [새롭게 연결할 깃 레파지토리 주소] 명령어를 입력합니다.

**3.** git remote -v 명령어를 입력해서 로컬 저장소를 원격 저장소에 연결시켜줍니다.

**4.** git push origin master 명령어를 입력해서 소스코드를 올리면 됩니다.

### 우반투스 상에 있는 파일 업로드 하기

이 과정은 위랑 비슷하지만 마지막에 

$ git remote add origin master 대신

git push -u origin main 을 사용 하였다. (저 master 명령을 쓰면 fatal: remote origin already exists.라는 에러가 뜬다. )

그러면 확정을 할 것이냐는 물음이 뜨는데. 그냥 예 하면 연결이 된다. 

위 명령어는 GitHub에서 새롭게 만들면 주소창 뜨는곳 아래에서 찾은 명령어이다. 

# Commit

들어 가서 확인 할 수 있지만, 좋은 commit은 제목으로 무엇을 했는지 정확히 알 수 있어야 한다. 

## 종종 있는 실수 

브런치가 꼬이는 경우가 있음. 

내일 본격적으로 함.

예방법:

```$ git pull origin master```
```$ git push origin master```

## git commit 

git commit 으로 하면 창이 뜨는데. 여기서 더 자세히 메시지를 정리 할 수 있다. 

## 버전 관리랑 상관없는 파일(.gitignore)

ex) secret.csv 라는 비밀 문서를 작성하는데 이걸 커밋하면 안돼니까. .

```.gitignore``` 이라는 파일을 만들어 이 파일에 감추고 싶은 파일을 넣으면 해당 파일을 무시 할 수 있다. 

secret.csv 

secret/

*.exe(exe 확장자 전부)

커밋하고 후회하면 늦으니까 미리미리 .gitignore 을 사용해 주자. 

참고 자료: [사이트 바로가기](https://www.toptal.com/developers/gitignore)



## ```$ git pull```

```$ git pull```을 하면 버전을 가져 올 수 있다. 

주로 협업을 할 떄 사용. 

내일







