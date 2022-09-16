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







# 코딩 스타일 가이드

[에어비엔비 JS Guide](https://github.com/airbnb/javascript)

에어비엔비가 개인적으로 가장 보기 쉽게 정리가 되어 있었습니다. 

# 변수와 식별자

- 선언 (Declaration) 
  - 변수를 생성하는 행위 또는 시점 
- 할당 (Assignment) 
  - 선언된 변수에 값을 저장하는 행위 또는 시점 
- 초기화 (Initialization) 
  - 선언된 변수에 처음으로 값을 저장하는 행위 또는 시점
- 함수 스코프* (function scope) 
  - 함수의 중괄호 내부를 가리킴 
  - 함수 스코프를 가지는 변수는 함수 바깥에서 접근 불가능



|        |  let   | const  |  var   |
| :----: | :----: | :----: | :----: |
| 재할당 |  가능  | 불가능 |  가능  |
| 재선언 | 불가능 | 불가능 | 불가능 |



![var](JS수업중 정리.assets/var-16632895971332.JPG)

var 호이스팅 이라는 문제를 남김

호이스팅

- 호이스팅 (hoisting) 
  - 변수를 선언 이전에 참조할 수 있는 현상 
  - 변수 선언 이전의 위치에서 접근 시 undefined를 반환 
- 자바스크립트는 모든 선언을 호이스팅한다. 
- 즉, var, let, const 모두 호이스팅이 발생하지만, var는 선언과 초기화가 동시에 발생 하여 일시적 사각지대가 존재하지 않는다. 

``` js
console.log(username) // undefined
var username = '홍길동'

console.log(email)
let email = 'gildong@gmail.com'

console.log(age)
const age = 50
```



# 데이터 타입

![캡처](JS수업중 정리.assets/캡처.JPG)

## 원시 타입 (Primitive type)

- 객체 (object)가 아닌 기본 타입 
- 변수에 해당 타입의 값이 담김 
- 다른 변수에 복사할 때 실제 값이 복사됨

## 참조 타입 (Reference type)

- 객체 (object) 타입의 자료형 
- 변수에 해당 객체의 참조 값이 담김 
- 다른 변수에 복사할 때 참조 값이 복사됨

## 자동 형변환

![123](JS수업중 정리.assets/123.JPG)

# 연산자

일치 비교 연산자 (===)

## 논리 연산자

- 세 가지 논리 연산자로 구성 

  - and 연산은 ‘&&’ 연산자를 이용 

  - or 연산은 ‘||’ 연산자를 이용 

  - not 연산은 ‘!’ 연산자를 이용 

- 단축 평가 지원 
  - ex) false && true => false 
  - ex) true || false => true

## 삼항연사자

```js
console.log(true ? 1 : 2) // 1
console.log(false ? 1 : 2) // 2
const result = Math.PI > 4 ? 'Yes' : 'No'
console.log(result) // No
```

[에어비엔비 15.6](https://github.com/airbnb/javascript#comparison--nested-ternaries)



# 조건문

## switch statement

```html
<!DOCTYPE html>
<html>
  <body>
    <h2>JavaScript switch</h2>
    <script>
      const nation = "Korea";

      switch (nation) {
        case "Korea": {
          console.log("안녕하세요!");
        }
        case "France": {
          console.log("Bonjour");
        }
        case "Korea": {
          console.log("안녕하세요!");
        }
        default: {
          console.log("Hello!");
        }
      }
    </script>
  </body>
</html>
<!--
안녕하세요!
Bonjour
안녕하세요!
Hello!
case는 if문 처럼 걸러주지 않는다. 
case는 제일 위에 한개에만 적용이 된다. 
-->
<!--올바른 예-->
<!DOCTYPE html>
<html>
  <body>
    <h2>JavaScript switch</h2>

    <p id="demo"></p>

    <script>
      const nation = "Korea";

      switch (nation) {
        case "Korea": {
          console.log("안녕하세요!");
          break;
        }
        case "France": {
          console.log("Bonjour");
          break;
        }
        case "Korea": {
          console.log("안녕하세요!");
          break;
        }
        default: {
          console.log("Hello!");
          break;
        }
      }
    </script>
  </body>
</html>
<!--안녕하세요!-->
```



# 반복문

- while

```js
let i = 0

while (i < 6) {
    console.log(i) // 0, 1, 2, 3, 4, 5
    i += 1
}
```

- for

```js
for (initialization; condition; expression) {
    // do something
}
```

- ​	세미콜론(;)으로 구분되는 세 부분 으로 구성 
- initialization 
  - 최초 반복문 진입 시 1회만 실행되는 부분 
- condition 
  - 매 반복 시행 전 평가되는 부분 
- expression 
  - 매 반복 시행 이후 평가되는 부분 
- 블록 스코프 생성

```js
for (let i = 0; i < 6; i++) {
    console.log(i) //0, 1, 2, 3, 4, 5
}
```

- for...in 
  - 주로 객체(object)의 속성들을 순회할 때 사용 
  - 배열도 순회 가능하지만 인덱스 순으로 순회한다는 보장이 없으므로 권장하지 않음 
  - 실행할 코드는 중괄호 안에 작성 
  - 블록 스코프 생성
  - 객체 출력하면 인덱스 출력???

```js
for (variable in object) {
    // do something
}
// object(객체) => key-value로 이루어진 자료구조 (객체 챕터에서 학습 예정)
const capitals = {
    korea: 'seoul',
    france: 'paris',
    USA: 'washington D.C.'
}
for (let capital in capitals) {
    console.log(capital) // Korea, france, USA
}
```

- for...of 
  - 반복 가능한(iterable)* 객체를 순회하며 값을 꺼낼 때 사용 
  - 반복 가능한(iterable) 객체*의 종류: Array, Map, Set, String 등
  - 실행할 코드는 중괄호 안에 작성 
  - 블록 스코프 생성
  - 객체 출력하면 오류???

```js
for (variable of iterables) {
    // do something
}
const fruits = ['딸기', '바나나', '메론']

for (let fruit of fruits) {
    fruit = fruit + '!'
    console.log(fruit) //딸기!, 바나나!, 메론!
}
```









# 함수 (콜백함수)

## 함수의 정의

- 3가지 부분으로 구성 
  - 함수의 이름 (name) 
  - 매개변수 (args) 
  - 함수 body (중괄호 내부)

```js
// 함수 선언식
function name(args) {
    // do something
}
// 함수 표현식
const name = function (args) {
// do something
}
```

## 매개변수와 인자의 개수 불일치 허용

```jS
// 인자 적거나 많거나 오류 안남
const noArgs = function () {
return 0
}
noArgs(1, 2, 3) // 0
const twoArgs = function (arg1, arg2) {
return [arg1, arg2]
}
twoArgs(1, 2, 3) // [1, 2]

// 매개변수보다 인자의 개수가 적을 경우
const threeArgs = function (arg1, arg2, arg3) {
return [arg1, arg2, arg3]
}
threeArgs() // [undefined, undefined, undefined]
threeArgs(1) // [1, undefined, undefined]
threeArgs(1, 2) // [1, 2, undefined]


// ...으로 여러개 받을 수 있음
const restOpr = function (arg1, arg2, ...restArgs) {
return [arg1, arg2, restArgs]
}
restArgs(1, 2, 3, 4, 5) // [1, 2, [3, 4, 5]]
restArgs(1, 2) // [1, 2, []]

// spread operator(…)를 사용하면 배열 인자를 전개하여 전달 가능
const spreadOpr = function (arg1, arg2, arg3) {
return arg1 + arg2 + arg3
}
const numbers = [1, 2, 3]
spreadOpr(...numbers) // 6
```



## 함수 타입

선언식 함수와 표현식 함수 모두 타입은 function으로 동일

```js
// 함수 표현식
const add = function (args) { }

// 함수 선언식
function sub(args) { }

console.log(typeof add) // function
console.log(typeof sub) // function
```



## 함수 호이스팅

호이스팅(hoisting) – 함수 선언식

- 함수 선언식으로 선언한 함수는 var로 정의한 변수처럼 hoisting 발생 
- 함수 호출 이후에 선언 해도 동작

```js
add(2,7) // 9

function add (num1, num2) {
    return num1 + num2
}
```

## 호이스팅(hoisting) - 함수 표현식

- 반면 함수 표현식으로 선언한 함수는 함수 정의 전에 호출 시 에러 발생 
- 함수 표현식으로 정의된 함수는 변수로 평가되어 변수의 scope 규칙을 따름

```js
sub(7,2) //Uncaught referenceError: Connot access 'sub' before initialization

const sub = function (num1, num2) {
    return num1 - num2
}
```

## (참고) 호이스팅(hoisting) – 함수 표현식

- 함수 표현식을 var 키워드로 작성한 경우, 변수가 선언 전 undefined 로 초기화 되어 다른 에러가 발생



# Arrow Function

- 함수를 비교적 간결하게 정의할 수 있는 문법 
- function 키워드 생략 가능 
- 함수의 매개변수가 단 하나 뿐이라면, ‘( )’ 도 생략 가능 
- 함수 몸통이 표현식 하나라면 ‘{ }’과 return도 생략 가능 
- 기존 function 키워드 사용 방식과의 차이점은 후반부 this 키워드를 학습하고 다시 설명

동작하는 방식이 조금 다름

this. 라는 키워드 사용할 때 주의

지금 사용하는 문법에는 크게 문제가 없다. 

![432](JS수업중 정리.assets/432.JPG)

```js
const str = 'a santa at nasa’
str.includes('santa') // true
str.includes('asan') // false

const str = 'a cup’
str.split() // ['a cup’]
str.split('') // ['a', ' ', 'c', 'u', 'p']
str.split(' ') // ['a', 'cup']

const str = 'a b c d'
str.replace(' ', '-') // 'a-b c d'
str.replaceAll(' ', '-') // 'a-b-c-d'

const str = ' hello '
str.trim() // 'hello'
str.trimStart() // 'hello '
str.trimEnd() // ' hello'
```

string.trim()

(정리 요망)

array.join( 파이썬 문자열, 자바스크립트 리스트)



# 배열

- 키와 속성들을 담고 있는 참조 타입의 객체(object) 

- 순서를 보장하는 특징이 있음 
- 주로 대괄호를 이용하여 생성하고, 0을 포함한 양의 정수 인덱스로 특정 값에 접근 가능 
- 배열의 길이는 array.length 형태로 접근 가능

![14](JS수업중 정리.assets/14.JPG)

```js
const numbers = [1, 2, 3, 4, 5]
numbers.reverse()
console.log(numbers) // [5, 4, 3, 2, 1]

const numbers = [1, 2, 3, 4, 5]
numbers.push(100)
console.log(numbers) // [1, 2, 3, 4, 5, 100]

const numbers = [1, 2, 3, 4, 5]
numbers.push()
console.log(numbers) // [1, 2, 3, 4, 5]

const numbers = [1, 2, 3, 4, 5]
numbers.unshift(100)
console.log(numbers) // [100, 1, 2, 3, 4, 5]

const numbers = [1, 2, 3, 4, 5]
numbers.shift()
console.log(numbers) // [1, 2, 3, 4, 5]

const numbers = [1, 2, 3, 4, 5]
console.log(numbers.includes(1)) // true

console.log(numbers.includes(100)) // false

const numbers = [1, 2, 3, 4, 5]
let result

result = numbers.indexOf(3) // 2
console.log(result)

result = numbers.indexOf(100) // -1
console.log(result)

const numbers = [1, 2, 3, 4, 5]
let result

result = numbers.join() // 1,2,3,4,5
console.log(result)

result = numbers.join('') // 12345
console.log(result)

result = numbers.join(' ') // 1 2 3 4 5 
console.log(result)

result = numbers.join('-') // 1-2-3-4-5 
console.log(result)
```



```js
const array = [1, 2, 3]
const newArray = [0, ...array, 4]
console.log(newArray) // [0, 1, 2, 3, 4]
```

## 배열 주요 메서드

## (forEach, map, filter, reduce, find, some, every)

![123124](JS수업중 정리.assets/123124.JPG)

```js
//forEach(요소, 인덱스, 배열)
array.forEach((element, index, array) => {
    // do something
})
const fruits = ['딸기', '수박', '사과', '체리']
fruits.forEach((fruit, index) => {
console.log(fruit, index)
// 딸기 0
// 수박 1
// 사과 2
// 체리 3
})

//map
array.map((element, index, array) => {
    // do something
})
const numbers = [1, 2, 3, 4, 5]

const doubleNums = numbers.map((num) => {
    return num * 2
})
console.log(doubleNums) // [2, 4, 6, 8, 10]

// filter
array.filter((element, index, array) => {
    // do something
})
const numbers = [1, 2, 3, 4, 5]

const oddNums = numbers.filter((num, index) => {
    return num % 2
})
console.log(oddNums) // [1, 3, 5]

// reduce
array.reduce((acc, element, index, array) => {
    // do something
}, initialValue)
const numbers = [1, 2, 3]

const result = numbers.reduce((acc, num) => {
    return acc + num
}, 0)
console.log(result) // 6

// find
array.find((element, index, array)) {
    // do something
}
const avengers = [
    { name: 'Tony Stark', age: 45 },
    { name: 'Steve Rogers', age: 3 },
    { name: 'Thor', age: 40 },
]
const result = avengers.find((avenger) => {
    return avenger.name === 'Tony Stark'
})
console.log(result) // {name: "Tony Stark", age: 45}

// some
/*
• 배열의 요소 중 하나라도 주어진 판별 함수를
통과하면 참을 반환
• 모든 요소가 통과하지 못하면 거짓 반환
• (참고) 빈 배열은 항상 거짓 반환
*/
array.some((element, index, array) => {
    // do something
})
const numbers = [1, 3, 5, 7, 9]
const hasEvenNumber = numbers.some((num) => {
    return num % 2 === 0
})
console.log(hasEvenNumber) // false
const hasEvenNumber = numbers.some((num) => {
    return num % 2
})
console.log(hasEvenNumber) // true

// every
/*
• 배열의 모든 요소가 주어진 판별 함수를
통과하면 참을 반환
• 하나의 요소라도 통과하지 못하면 거짓 반환
• (참고) 빈 배열은 항상 참 반환
*/
array.every((element, index, array) => {
    // do something
})
const numbers = [1, 3, 5, 7, 9]
const hasEvenNumber = numbers.every((num) => {
    return num % 2 === 0
})
console.log(hasEvenNumber) // false
const hasEvenNumber = numbers.every((num) => {
    return num % 2
})
console.log(hasEvenNumber) // true
```

# 객체

- 객체는 속성(property)의 집합이며, 중괄호 내부에 key와 value의 쌍으로 표현 
- key는 문자열 타입*만 가능 
  - (참고) key 이름에 띄어쓰기 등의 구분자가 있으면 따옴표로 묶어서 표현 
- value는 모든 타입(함수포함) 가능 
- 객체 요소 접근은 점 또는 대괄호로 가능 
  - (참고) key 이름에 띄어쓰기 같은 구분자가 있으면 대괄호 접근만 가능

```js
const me = {
name: 'jack',
phoneNumber: '01012345678',
'samsung products': {
buds: 'Galaxy Buds pro',
galaxy: 'Galaxy s20’,
},
}
console.log(me.name)
console.log(me.phoneNumber)
console.log(me['samsung products'])
console.log(me['samsung products'].buds)
```

- 메서드는 객체의 속성이 참조하는 함수 
- 객체.메서드명() 으로 호출 가능 
- 메서드 내부에서는 this 키워드가 객체를 의미함

```js
const me = {
    firstName: 'John',
    lastName: 'Doe’
    ,
    getFullName: function () {
    return this.firstName + this.lastName
    }
}
```

# JSON

- key-value쌍의 형태로 데이터를 표기하는 언어 독립적 표준 포맷 
- 자바스크립트의 객체와 유사하게 생겼으나 실제로는 문자열 타입 
  - 따라서 JS의 객체로써 조작하기 위해서는 구문 분석(parsing)이 필수 
- 자바스크립트에서는 JSON을 조작하기 위한 두 가지 내장 메서드를 제공 
  - JSON.parse() 
    - JSON => 자바스크립트 객체 
  - JSON.stringify() 
    - 자바스크립트 객체 => JSON

[mdn JSON](https://developer.mozilla.org/ko/docs/Learn/JavaScript/Objects/JSON)

JSON은 문자열 형태로 존재합니다 — 네트워크를 통해 전송할 때 아주 유용하죠. 데이터에 억세스하기 위해서는 네이티브 JSON 객체로 변환될 필요가 있습니다.

