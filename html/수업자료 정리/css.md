# css

!important

![우선순위](css.assets/우선순위-16618427444938.JPG)

## 길이

em

```css
.a { font-size: 1 em; } /* 상위 기본 길이 16, 기본*1.5 24px */
```

ren

```css
.a { font-size: 1.0rem; } /* 상위 기본 길이 16, 16px */
```

## 투명도

rgba()

```css
rgba(0,0,0,0.5)
```

## margin, padding

![box_sizing](css.assets/box_sizing-16618427180082.JPG)



![margin1234](css.assets/margin1234-16618427353015.JPG)



# 디스플레이

display: block

막는다? 내 영역에 못 올라온다. 

div는 오른쪽을 모두 마진을 채워서 블록을 한다.



display: inline

줄 바꿈이 일어나지 않는다. 

가운데 정렬(내가 아는건 flex)

![인라인블록](css.assets/인라인블록-166184275432011.JPG)

display: inline-block

두가지 요소를 갖고 있음(flex를 쓰면 되는데 왜 이걸 쓰는지 그 차이를 모르겠음.)



display: none

공간도 부여 되지 않음.

# 정렬

text-align ??? 사진도 이동 시킬 수 있네?



## 글자간의 간격

letter-spacing

word-spacing









# CSS Position

## 박스 겹치기

- relative : 사람 눈에만 이동, 실제 위치는 그대로. (주로 absolute와 함께 사용)
- absolute : 집을 나가버림.ㅋㅋㅋ 해당 공간은 빈 공간으로 처리가 됨. 부모에 relative를 써 주어야 한다. (주로 이미지 안에 버튼을 만들때 사용)
- fixed 공간 노 (공간이 없으므로 맨 상단 제외 주로 이걸 사용)
- sticky 처음에는 공간 화면 이동하면 fixed (맨 위 상단 메뉴를 처음에 공간을 주었다가 나중에는 사라지는 방식으로 사용)



Float left

float: left;

이런게 존재한다. 나중에 다시 설명. 

# FLOX BOX

축이라는 개념을 만든다. 

메인축과 교차축이 생긴다. 

부모에 지정하면 자식은 flex요소가 된다. 

![flex-1](css.assets/flex-1.JPG)



왜 나왔는가?

1. 수직 정렬 
2. 아이템의 너비와 높이 혹은 간격을 동일하게 배치

![flex-정리](css.assets/flex-정리.JPG)

wrap 뛰쳐 나가지 못하게. 



flex-grow 남은 영역을 아이템에 분배

order 배치 순서





```css
* {
    box-sizing: border-box;
}
```



# 문제 풀면서 까먹었던거 정리 

```css
.flew {  
    flex-flow: column wrap;  
    flex-direction: column;
	flex-wrap: ;
    flex-flow: column-reverse wrap-reverse;
}
```



구글 스타일 가이드	

```css
<head>
  <meta charset="UTF-8">
  <meta name="description" content="Free Web tutorials">
  <meta name="keywords" content="HTML, CSS, JavaScript">
  <meta name="author" content="John Doe">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
```

