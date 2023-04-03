1. 우선 설치를 해 준다. install.md 참조

2. https://cotak.tistory.com/25?category=452341 이곳을 참고 해서 만들었음.
   이때 ?charset=utf8mb4" 로 했고 그 다음줄

   engine = create_engine(

     SQLALCHEMY_DATABASE_URL

   ) 
   encoding을 빼 줬다. 

그외 오류들

비밀번호에 @를 넣어서 바꾸어 주었다. @는 password와 host를 구분할때 사용해서 비밀번호에 @가 있으면 정보가 잘못 전달 된다. 

sql_app이 (내 부모 폴더) 인식을 못해서 `from . import crud` 를 사용 못하고 `from crud import *`를 사용했다. 