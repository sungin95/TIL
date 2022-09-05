# 배운것중 잘 몰랐던거

## html

|           | 단순 표현 | 강조 의미        |
| --------- | --------- | ---------------- |
| 굵은 글씨 | b         | strong 강한 글씨 |
| 이탤릭    | i         | em               |

```html
<img class="fit-picture"
     src="/media/cc0-images/grapefruit-slice-332-332.jpg"
     alt="Grapefruit slice atop a pile of other slices"> 대체특징(이미지가 안보일때 보임)+ 시각장애인을 위한 소리
```

팁:

computed: 계산이 완료되면 

styles, element.style: 임시로 바꿀 수 있음

## CSS

우선순위 id, class, 태그

id는 1번만 쓰자(권장)

# 드림코딩

```html
<header>
    <nav></nav>
</header>
<main>
    <article>
        <section></section>
    </article>
    <aside></aside>
</main>
<footer></footer>
<oi>
    순서가 중요
	<ul>
        순서없음 
        <dl>
            정의 설명 목록
        </dl>
    </ul>	
</oi>
<button>
    특정한 액션을 위해
</button>
<a>
    어디론가 이동할 때
</a>
<table>
    (행 + 열) 데이터
</table>
<css>Flex, Grid 사용</css>
```



# table

\<thead>,\<tbody>,\<tfoot>요소를 활용



# input

![name](html.assets/name.JPG)

input 속성

autofocus

label 

for을 사용해서 라벨만 클릭해도 자동으로 입력된다. (id와 연계)

radio(타입) 이름당 하나 선택 가능 value는 보내지는 값



# Bootstrap





## CDN

Content Delivery Network

쓰는 소스코드는 같지만 가장 가까운 서버로 간다. 

데이터 센터랑은 다르다. 

서버에 문제가 생기면 작동을 안한다. 



![spacing](html.assets/spacing.JPG)







오늘 유틸리티만 보자







# 블로그 내용 정리(순한맛)

https://tecoble.techcourse.co.kr/post/2021-10-24-browser-rendering/

주소창에 google.com 입력했을 때

HTML파일은 어떻게 브라우저에 그려지는지.

브라우저는 무엇인가?: Chrome, Safari, Firefox, Internet Explorer 등을 말한다.

MDN에서는 브라우저가 우선 웹 페이지를 찾고, 하이퍼링크를 통해 다른 페이지로 이동. 중요하다고 생각되는 곳 보여준다. 

(여기서 중요하다? 무슨 말인지 잘 모르겠네. )

이때 자료를 서버로 부터 받아 오고(이미지, 비디오 등등) 받아온 자원을 렌더링 과정을 통해 보여준다. 



## 브라우저 렌더링 동작 과정



1. HTML 파일과 CSS 파일을 파싱해서 각각 Tree를 만든다. (Parsing) 
2. 두 Tree를 결합하여 Rendering Tree를 만든다. (Style) 
3. Rendering Tree에서 각 노드의 위치와 크기를 계산한다. (Layout)
4. 계산된 값을 이용해 각 노드를 화면상의 실제 픽셀로 변환하고, 레이어를 만든다. (Paint)
5. 레이어를 합성하여 실제 화면에 나타낸다. (Composite)

### Parsing

브라우저가 렌더링을 위해서는 가장 먼저 온 HTML파일 해석을 하고 DOM(Document Object Model) Tree 구성.

이때 css자료가 포함되어 있으면 CSSOM(CSS Object Model) Tree 구성.

### Style

이 과정은 DOM과 CSSOM을 합쳐 Render Tree를 구성. Render Tree는 실제 화면에 그려질 Tree

(Tree가 구성 요소 쯤 되는 것 같다. 아니면 데이터 구조?)

### Layout

Render Tree 정확한 위치 계산

### Paint

계산된 값을 이용해 Render Tree 실제 픽셀로 변환.

이때 하나의 레이어가 아니라 여러개의 레이어로 관리 

### Composite

여러 레이어를 합성하여 실제 화면에 표시.

# 블로그 내용 정리(매운맛)

https://d2.naver.com/helloworld/59361

## 브라우저의 주요 기능

사용자가 선택한 자원을 서버에 요청, 브라우저에 표시하는 것.



# Q&A

\<iframe>: 인라인 프레임 요소

```html
<iframe id="inlineFrameExample"
    title="Inline Frame Example"
    width="300"
    height="200"
    src="https://www.openstreetmap.org/export/embed.html?bbox=-0.004017949104309083%2C51.47612752641776%2C0.00030577182769775396%2C51.478569861898606&layer=mapnik">
</iframe>
```

여기에서 src에 있는 주소창을  https://map.naver.com/v5/?c=14165093.6424532,4530823.3727283,16,0,0,2,dh 네이버 지도에서 검색한 걸로 바꾸어 보았는데. 바꾸니까 안보이더라고요? 같은 지도 src라고 생각했는데. 왜 안되는지 의아해서 질문드렸습니다.

[네이버 지도](https://map.naver.com/v5/?c=14165093.6424532,4530823.3727283,16,0,0,2,dh)



RE

네이버 측에서 보안상의 이유로 해당 url이 iframe으로 띄워지는 것을 막았기 때문입니다. 위의 코드를 크롬창에서 띄우고 F12를 눌러보면 아래와 같은 경고창을 볼 수 있습니다. 여기서 'X-Frame-Options'가 deny(거부)되었다고 나옵니다. X-Frame-Options에 관해서는 mdn문서를 참고해 주세요! https://developer.mozilla.org/ko/docs/Web/HTTP/Headers/X-Frame-Options

참고로, 저희가 나중에 배울 Django에서는 기본적으로 iframe접근을 막습니다. 접근을 막는 설정을 해제할 수도 있고요!



## X-Frame-Options

The **`X-Frame-Options`** [HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP) 응답 헤더는 해당 페이지를 [`frame`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/frame) 또는[`iframe`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/iframe), [`object`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/object) 에서 렌더링할 수 있는지 여부를 나타내는데 사용됩니다. 사이트 내 콘텐츠들이 다른 사이트에 포함되지 않도록 하여 [clickjacking](https://en.wikipedia.org/wiki/Clickjacking) 공격을 막기 위해 이 헤더를 사용합니다.

### 여기서

#### frame이란?

`<frame>`은 다른 HTML 문서가 표시될 수 있는 특정 영역을 정의하는 element이다. frame은 [`frameset`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/frameset)내에서 사용되어야 한다.

<frame> element의 사용은 screen reader 사용자들의 접근성 부족과같은 기능문제같은 특정 단점 때문에 권장되지 않는다
<frame> element 대신에 [`iframe`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/iframe) 가 아마 더 적합할것이다.

##### 속성(=Attributes)

다른 모든 HTML elments와 마찬가지로, <frame> element는 전역속성([global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes))이 적용된다.

- [**`src`**](https://developer.mozilla.org/ko/docs/Web/HTML/Element/frame#attr-src)

  이 속성은 frame으로 표시될 문서를 기입합니다.

- [**`name`**](https://developer.mozilla.org/ko/docs/Web/HTML/Element/frame#attr-name)

  이 속성은 프레임을 명명하는데 사용됩니다. 명명되지않은 모든 링크들은 그들이 속해있는 그 프레임 안에서 열릴것입니다

- 

- [**`noresize`**](https://developer.mozilla.org/ko/docs/Web/HTML/Element/frame#attr-noresize)

  이 속성은 사용자가 프레임크기를 조정할수 없게합니다.

- [**`scrolling`**](https://developer.mozilla.org/ko/docs/Web/HTML/Element/frame#attr-scrolling)

   이 속성은 스크롤바의 유무를 결정합니다. 이 속성을 사용하지않으면 특정상황에서 자동으로 브라우져에 스크롤바가 생깁니다. 두가지를 선택할 수 있습니다. "yes"면 항상 스크롤바를 보여주고 "no"면 항상 스크롤바를 보여주지 않습니다.

- [**`marginheight`**](https://developer.mozilla.org/ko/docs/Web/HTML/Element/frame#attr-marginheight)

  이 속성은 프레임 사이의 여백 높이를 정의할때 사용됩니다.

- [**`marginwidth`**](https://developer.mozilla.org/ko/docs/Web/HTML/Element/frame#attr-marginwidth)

  이 속성은 프레임 사이의 여백 넓이를 정의할때 사용됩니다.

- [**`frameborder`**](https://developer.mozilla.org/ko/docs/Web/HTML/Element/frame#attr-frameborder)

  이 속성을 사용하면 프레임에 대한 경계선을 넣을 수 있습니다.

##### 예시

```html
<frameset cols="50%,50%">
  <frame src="https://developer.mozilla.org/en/HTML/Element/iframe" />
  <frame src="https://developer.mozilla.org/en/HTML/Element/frame" />
</frameset>
```



#### iframe이란?

**HTML `<iframe>` 요소**는 중첩 [브라우징 맥락](https://developer.mozilla.org/ko/docs/Glossary/Browsing_context)을 나타내는 요소로, 현재 문서 안에 다른 HTML 페이지를 삽입합니다.

삽입된 브라우징 맥락은 각자 자신만의 [세션 기록](https://developer.mozilla.org/ko/docs/Web/API/History)과 [문서](https://developer.mozilla.org/ko/docs/Web/API/Document)를 가집니다. 다른 브라우징 맥락을 포함하고 있는 맥락은 "부모 브라우징 맥락"이라고 부릅니다. 부모를 가지지 않는, 즉 최상위 브라우징 맥락은 대개 브라우저 창으로서, [`Window`](https://developer.mozilla.org/ko/docs/Web/API/Window) 객체로 나타냅니다.

세션기록(History)

**`History`** 인터페이스는 브라우저의 세션 기록, 즉 현재 페이지를 불러온 탭 또는 프레임의 방문 기록을 조작할 수 있는 방법을 제공합니다.

속성

*`History` 인터페이스는 어떤 속성도 상속하지 않습니다.*

- [`History.length`](https://developer.mozilla.org/ko/docs/Web/API/History/length) Read only

  현재 페이지를 포함해, 세션 기록의 길이를 나타내는 정수를 반환합니다.

- [`History.scrollRestoration`](https://developer.mozilla.org/ko/docs/Web/API/History/scrollRestoration)

  기록 탐색 시 스크롤 위치 복원 여부를 명시할 수 있습니다. 가능한 값은 `auto`와 `manual`입니다.

- [`History.state`](https://developer.mozilla.org/ko/docs/Web/API/History/state) Read only

  기록 스택 최상단의 스테이트를 나타내는 값을 반환합니다. `popstate` 이벤트를 기다리지 않고 현재 기록의 스테이트를 볼 수 있는 방법입니다.

메서드

*`History` 인터페이스는 어떤 메서드도 상속하지 않습니다.*

- [`History.back()`](https://developer.mozilla.org/ko/docs/Web/API/History/back)

  세션 기록의 바로 뒤 페이지로 이동하는 비동기 메서드입니다. 브라우저의 뒤로 가기 버튼을 눌렀을 때, 그리고 `history.go(-1)`을 사용했을 때와 같습니다.> **참고:** 세션 기록의 제일 첫 번째 페이지에서 호출해도 오류는 발생하지 않습니다.

- [`History.forward()`](https://developer.mozilla.org/ko/docs/Web/API/History/forward)

  세션 기록의 바로 앞 페이지로 이동하는 비동기 메서드입니다. 브라우저의 앞으로 가기 버튼을 눌렀을 때, 그리고 `history.go(1)`을 사용했을 때와 같습니다.> **참고:** 세션 기록의 제일 마지막 페이지에서 호출해도 오류는 발생하지 않습니다.

- [`History.go()`](https://developer.mozilla.org/ko/docs/Web/API/History/go)

  현재 페이지를 기준으로, 상대적인 위치에 존재하는 세션 기록 내 페이지로 이동하는 비동기 메서드입니다. 예를 들어, 매개변수로 `-1`을 제공하면 바로 뒤로, `1`을 제공하면 바로 앞으로 이동합니다. 세션 기록의 범위를 벗어나는 값을 제공하면 아무 일도 일어나지 않습니다. 매개변수를 제공하지 않거나, `0`을 제공하면 현재 페이지를 다시 불러옵니다.

- [`History.pushState()`](https://developer.mozilla.org/ko/docs/Web/API/History/pushState)

  주어진 데이터를 지정한 제목(제공한 경우 URL도)으로 세션 기록 스택에 넣습니다. 데이터는 DOM이 불투명(opaque)하게 취급하므로, 직렬화 가능한 모든 JavaScript 객체를 사용할 수 있습니다. 참고로, Safari를 제외한 모든 브라우저는 `title` 매개변수를 무시합니다.

- [`History.replaceState()`](https://developer.mozilla.org/ko/docs/Web/API/History/replaceState)

  세션 기록 스택의 제일 최근 항목을 주어진 데이터, 지정한 제목 및 URL로 대체합니다. 데이터는 DOM이 불투명(opaque)하게 취급하므로, 직렬화 가능한 모든 JavaScript 객체를 사용할 수 있습니다. 참고로, Safari를 제외한 모든 브라우저는 `title` 매개변수를 무시합니다.





