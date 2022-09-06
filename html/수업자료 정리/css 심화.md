# css 심화



# meta

mata 태그는  html 문서에 대한 메타데이터를 정의합니다. 이건 데이터에 대한 데이터 정보입니다. 

위치: 항상 \<head>  요소 내부에 있음.

주 사용처: 문자 집합, 페이지 설명, 키워드, 문서 작성자 및 뷰포트 설정을 지정하는 데 사용됩니다. (요약하면 부가적인 정보를 알려준다. )

페이지에는 표시가 않되지만 시스템에서 분석 가능.



**검색 엔진에 대한 키워드 정의:**

<meta name="keywords" content="HTML, CSS, JavaScript">


**웹 페이지에 대한 설명을 정의합니다.**

<meta name="description" content="Free Web tutorials for HTML and CSS">


**페이지 작성자 정의:**

<meta name="author" content="John Doe">


**30초마다 문서 새로 고침:**

<meta http-equiv="refresh" content="30">

**웹사이트가 모든 기기에서 잘 보이도록 표시 영역 설정:**

<meta name="viewport" content="width=device-width, initial-scale=1.0">


## 뷰포트 설정

뷰포트는 웹 페이지에서 사용자가 볼 수 있는 영역입니다. 기기에 따라 다릅니다. 컴퓨터 화면보다 휴대전화에서 더 작습니다.

모든 웹 페이지에 다음 `<meta>`요소를 포함해야 합니다.

<meta name="viewport" content="width=device-width, initial-scale=1.0">


이것은 페이지의 크기와 배율을 제어하는 방법에 대한 브라우저 지침을 제공합니다.

부품 은 `width=device-width`장치의 화면 너비를 따르도록 페이지 너비를 설정합니다(장치에 따라 다름).

이 `initial-scale=1.0`부분은 브라우저에서 페이지를 처음 로드할 때 초기 확대/축소 수준을 설정합니다.







