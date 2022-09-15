새로운 언어를 배울때: 변수 데이터타입 조건 반복 함수 특징

# 자바스크립트

정의: 브라우저를 조작 할 수 있는 유일한 언어. 

## node.js

runtime환경 제공

js는 브라우저 위에서만 작동

node.js가 그 한계를 해결.



# JS기초 문법

```js
document.querySelector('.text') // 하나
document.querySelectorAll('.text') // 모두

append 여러개?
appendChild 1개

const a = document.createElement('a')
a.innerText = '실라버스'


const title = document.querySelector('.title')
title.innerText = '실라버스'
title.appendChiled(h1)
title.remove() // 삭제

a.setAttribute('href', 'https://syllaverse.com') // 딕셔너리 비슷한 느낌?
console.log(a.getAttribute('href'))

// class가 여러개 라면?
h1.classList(다양한 기능이 있다. )
h1.classList.replace('red', 'blue')

// 이벤트 토글
const btn1 = document.querySelector('#btn1')
btn1.addEventListener('click', function() {
    const h1 = document.querySelector('h1')
    h1.classList.toggle('blue')
}) // 자동으로 반대로 바뀌었다가 하네
/*
토클 
껏다 켯다 하는거
modal에 사용
클릭하면 class생성, 끄면 class 삭제
*/
```

## 주의

보안적이슈

사이트 공격 경로가 될 수 있음. 

innerHTML을 사용 안한다. 



# 문서정리

[JS와 API](https://developer.mozilla.org/ko/docs/Learn/JavaScript/First_steps/What_is_JavaScript#%EA%B7%B8%EB%9E%98%EC%84%9C_%EC%96%B4%EB%96%A4_%EC%9D%BC%EC%9D%84_%ED%95%A0_%EC%88%98_%EC%9E%88%EB%82%98%EC%9A%94)

변수를 저장하고 활용가능

이벤트 코드 사용 가능.

API

브라우저 API 

- DOM
- Geolocation API
- Canvas & WebGL API
- HTMLMediaElement & WebRTC

서드파티 API (브라우저에 탑재되지 않은 API로, 웹의 어딘가에서 직접 코드와 정보를 찾아야 합니다.)

- Twitter API
- Google 지도 API & OpenStreetMap API



인터프리터(바로 실행) vs 컴파일러(변환 과정 후 실행)

JIT 컴파일(just-in-time)이라는 기술로 향상을 시키지만 이 기술은 런타임 도중에 일어나므로 컴파일러 과정이라고 보지 않는다. 







