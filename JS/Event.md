# Event

브라우저 조작을 위한 JS, 그 핵심 이벤트

## 개념

- 네트워크 활동이나 사용자와의 상호작용 같은 사건의 발생을 알리기 위한 객체
- 이벤트 발생
  - 마우스를 클릭하거나 키보드를 누르는 등 사용자 행동으로 발생할 수도 있음
  - 특정 메서드를 호출(Element.click())하여 프로그래밍적으로도 만들어 낼 수 있음



역할: ~하면 ~한다. 

행동을 어떻게 정의할까?

클릭하면, 경고창을 띄운다. 

특정 이벤트가 발생하면, 할 일(함수)을 등록한다. 

```js
target.addEventListener(type, listener(함수)[, options])
```

대상에 특정 이벤트가 발생하면, 할 일을 등록하자



# 실습 문법 정리

```js
// btn1
const btn1 = document.querySelector('#btn1')
// btn1이 클릭되면 함수실행
btn1.addEventListener('click', function() {
    // h1 태그를 잡아서
    const h1 = document.querySelector('h1')
    // 클래스 blue를 토글하자. 
    h1.classList.toggle('blue')
})

// input
const input = document.querySelector('input')
input.addEventListener('input', function(e) {
    console.log(e.target.value)
})// 만들어서 붙이기
console.log('hello, js!')
// h1 요소(element)를 만들고
const title = document.createElement('h1')
// 텍스트를 추가하고
title.innerText = 'JS 기초' 
// 선택자로 body태그를 가져와서
const body = document.querySelector('body')
// body태그에 자식 요소로 추가
body.appendChild(title)

// 요소를 선택하기
console.log(document.querySelector('#title'))
// <h1 id="title">JS 기초</h1>
console.log(document.querySelectorAll('.text'))
// NodeList(2) [p.text, p.text]
console.log(document.querySelector('.text'))
// <p class="text">querySelector</p>

// 토글, 타겟
// btn1
const btn1 = document.querySelector('#btn1')
// btn1이 클릭되면 함수실행
btn1.addEventListener('click', function() {
    // h1 태그를 잡아서
    const h1 = document.querySelector('h1')
    // 클래스 blue를 토글하자. 
    h1.classList.toggle('blue')
})

// input
const input = document.querySelector('input')
input.addEventListener('input', function(e) {
    console.log(e.target.value)
})
```



# 이벤트의 종류

대표적인 이벤트를 소개한다.

자세한 사항은 [Event referenceVisit Website](https://developer.mozilla.org/ko/docs/Web/Events)을 참조 바란다.



## UI Event

| Event    | Description                                                  |
| -------- | ------------------------------------------------------------ |
| **load** | 웹페이지나 스크립트의 로드가 완료되었을 때                   |
| unload   | 웹페이지가 언로드될 때(주로 새로운 페이지를 요청한 경우)     |
| error    | 브라우저가 자바스크립트 오류를 만났거나 요청한 자원이 존재하지 않는 경우 |
| resize   | 브라우저 창의 크기를 조절했을 때                             |
| scroll   | 사용자가 페이지를 위아래로 스크롤할 때                       |
| select   | 텍스트를 선택했을 때                                         |

 

## Keyboard Event

| Event     | Description                                                  |
| --------- | ------------------------------------------------------------ |
| keydown   | 키를 누르고 있을 때                                          |
| **keyup** | 누르고 있던 키를 뗄 때                                       |
| keypress  | 키를 누르고 뗏을 때                                          |
| keyCode   | 키 코드값. **[https://blog.lael.be/post/75Visit Website](https://blog.lael.be/post/75)** |

 

## Mouse Event

| Event       | Description                                                  |
| ----------- | ------------------------------------------------------------ |
| **click**   | 마우스 버튼을 클릭했을 때                                    |
| dbclick     | 마우스 버튼을 더블 클릭했을 때                               |
| mousedown   | 마우스 버튼을 누르고 있을 때                                 |
| mouseup     | 누르고 있던 마우스 버튼을 뗄 때                              |
| mousemove   | 마우스를 움직일 때 (터치스크린에서 동작하지 않는다)          |
| mouseover   | 마우스를 요소 위로 움직였을 때 (터치스크린에서 동작하지 않는다) |
| mouseout    | 마우스를 요소 밖으로 움직였을 때 (터치스크린에서 동작하지 않는다) |
| mouserenter | 해당 요소에 마우스 커서를 올려다놓았을때                     |
| mouseleave  | 해당 요소에 마우스 커서를 빼낼때                             |

 

## Focus Event

| Event              | Description               |
| ------------------ | ------------------------- |
| **focus**/focusin  | 요소가 포커스를 얻었을 때 |
| **blur**/foucusout | 요소가 포커스를 잃었을 때 |

 

## Form Event

| Event      | Description                                                 |
| ---------- | ----------------------------------------------------------- |
| **input**  | input 또는 textarea 요소의 값이 변경되었을 때               |
|            | contenteditable 어트리뷰트를 가진 요소의 값이 변경되었을 때 |
| **change** | select box, checkbox, radio button의 상태가 변경되었을 때   |
| submit     | form을 submit할 때 (버튼 또는 키)                           |
| reset      | reset 버튼을 클릭할 때 (최근에는 사용 안함)                 |

 

## Clipboard Event

| Event | Description            |
| ----- | ---------------------- |
| cut   | 콘텐츠를 잘라내기할 때 |
| copy  | 콘텐츠를 복사할 때     |
| paste | 콘텐츠를 붙여넣기할 때 |

# 이벤트 막기

stopPropagation

```js
function logEvent(event) {
	event.stopPropagation();
}
```

주의: 버블링은 유용합니다. 버블링을 꼭 멈춰야 하는 명백한 상황이 아니라면 버블링을 막지 마세요. 아키텍처를 잘 고려해 진짜 막아야 하는 상황에서만 버블링을 막으세요.

`event.stopPropagation()`은 추후에 문제가 될 수 있는 상황을 만들어낼 수 있습니다.

1. 중첩 메뉴를 만들었다 가정합시다. 각 서브메뉴(submenu)에 해당하는 요소에서 클릭 이벤트를 처리하도록 하고, 상위 메뉴의 클릭 이벤트 핸들러는 동작하지 않도록 `stopPropagation`을 적용합니다.
2. 사람들이 페이지에서 어디를 클릭했는지 등의 행동 패턴을 분석하기 위해, window내에서 발생하는 클릭 이벤트 전부를 감지하기로 결정합니다. 분석 시스템을 도입하기로 합니다. 그런데 이런 분석 시스템의 코드는 클릭 이벤트를 감지하기 위해 `document.addEventListener('click'…)`을 사용합니다.
3. `stopPropagation`로 버블링을 막아놓은 영역에선 분석 시스템의 코드가 동작하지 않기 때문에, 분석이 제대로 되지 않습니다. 안타깝게도 `stopPropagation`을 사용한 영역은 '죽은 영역(dead zone)'이 되어버립니다.

이벤트 버블링을 막아야 하는 경우는 거의 없습니다. 버블링을 막아야 해결되는 문제라면 커스텀 이벤트 등을 사용해 문제를 해결할 수 있습니다. 커스텀 이벤트 사용 방법은 추후에 다루겠습니다. 핸들러의 `event` 객체에 데이터를 저장해 다른 핸들러에서 읽을 수 있게 하면, 아래쪽에서 무슨 일이 일어나는지를 부모 요소의 핸들러에게 전달할 수 있으므로, 이 방법으로도 이벤트 버블링을 통제할 수 있습니다.





