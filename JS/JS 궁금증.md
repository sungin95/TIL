# JS 궁금증

편한 var은 왜 안쓰고, 새롭게 기능이 더 적은 const, let을 사용하는 걸까?

- 같은 이름의 변수를 여러번 생성가능하다.
  - var를 많이 사용하게 되면 이와 같은 문제로 예상치 못한 오류가 발생할 가능성이 크다.
- var는 function 단위의 scope를 가진다
  - 이 부분은 무슨 말인지 모르겠지만 문제인건 확실한 듯하다. 
  - [해당 블로그](https://jodev.kr/entry/JavaScript-var%EB%A5%BC-%EA%B6%8C%EC%9E%A5%ED%95%98%EC%A7%80-%EC%95%8A%EB%8A%94-%EC%9D%B4%EC%9C%A0#:~:text=%EC%9C%84%EC%9D%98%20%EC%BD%94%EB%93%9C%EC%99%80%20%EA%B0%99%EC%9D%B4%20const%EB%A1%9C%20foo%EB%9D%BC%EB%8A%94%20%EB%B3%80%EC%88%98,%EA%B0%80%20%EB%B0%9C%EC%83%9D%ED%95%A0%20%EA%B0%80%EB%8A%A5%EC%84%B1%EC%9D%B4%20%ED%81%AC%EB%8B%A4.)

