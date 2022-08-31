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



