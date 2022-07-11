# 파일 라이프사이클

![status](https://t1.daumcdn.net/cfile/tistory/2447383557690E1003)

## untracked => unmodified => modified => staged

예시)

1. 처음으로 만들면 => untracked(1단계)
2. 보고서 파일 add => Staged(4단계)
3. Staged를 commit하면 => unmodified(2단계)
4. 보고서 수정 modified(3단계)



라고는 하는데. 나는 봐도 잘 모르겠다. 

![내가 이해한 파일 라이프](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTrgRZHaY2t1wQW-EEy4pxYyu43TmQ9gZS_u6bR9ciWkdFrHm5ZrMVuXFv4-E4kXVCrqKs&usqp=CAU)

결국 핵심

1. 파일에서 작업을 한다. 
2. ```$ git add . ```을 통해 임시 저장을 한다. 
3. ```$ git commit -m```을 통해 해당 파일에 하나의 임시 버전으로 저장을 한다. 
4. 추후에 ```$ git push origin master(브런치 네임)```를 통해 서버에 보내준다. (이 명령어는 이전에 깃허브 주소랑 연결 되어 있어야 한다. 참고 [원격저장소 만드는 법](https://github.com/sungin95/TIL/blob/master/0706%20%EC%9B%90%EA%B2%A9%EC%A0%80%EC%9E%A5%EC%86%8C%20%EB%A7%8C%EB%93%9C%EB%8A%94%20%EB%B2%95.md)
