# table

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    table, th, td {
        border: 1px solid black;
    }
  </style>
  <link rel="stylesheet" href="">
  <link rel="stylesheet" href="css/style.css">
  <title>HPHK APPAREL</title>
</head>
<body>
    <table>
        <thead>
            <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Major</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>1</td>
                <td>홍길동</td>
                <td>Computer Science</td>
            </tr>
            <tr>
                <td>2</td>
                <td>김철수</td>
                <td>Business</td>
            </tr>
        </tbody>
        <tfoot>
            <tr>
                <td>총계</td>
                <td colspan="2">2명</td>
            </tr>
        </tfoot>
        <caption>1반 학생 명단</caption>
    </table>
</body>
</html>
```

이런 식으로 사용하긴 하지만 _reset을 사용하면 작동을 안한다. 딱히 사용 할거 같지는 않다. 

# form 

\<form>은 정보(데이터)를 서버에 제출하기 위해 사용하는 태그.

\<form> 기본 속성

- action : form을 처리할 서버의 URL(데이터를 보낼 곳)
- method: form을 제출할 때 사용할 HTTP 메서드 (GET 혹은 POST)
- enctype : method가 post인 경우 데이터의 유형
  - application/x-www-form-urlencoded : 기본값
  - multipart/form-data : 파일 전송시 (input type이 file인 경우)

## input

- 다양한 타입을 가지는 입력 데이터 유형과 위젯이 제공됨
- \<input> 대표적인 속성
  - name : form control에 적용되는 이름 (이름/값 페어로 전송됨)
  - value : form control에 적용되는 값 (이름/값 페어로 전송됨)
  - required, readonly, autofocus, autocomplete, disabled 등

```html
<form action="/search" method="GET">
	<input type="text" name="q">
</form>
<!--https://www.google.com/search?q=HTML-->
```

\<input>유형 - 일반

- 일반적으로 입력을 받기 위하여 제공되며 타입별로 HTML기본 검증 혹은 추가 속성을 활용할 수 있음
  - text : 일반 텍스트 입력
  - password : 입력 시 값이 보이지 않고 문자를 특수기호(*)로 표현
  - email : 이메일 형식이 아닌 경우 form 제출 불가
  - number : min max step 속성을 활용하여 숫자 범위 설정 가능
  - file : accept 속성을 활용하여 파일 타입 지정 가능

\<input>유형 - 항목 중 선택

- 일반적으로 label 태그와 함께 사용하여 선택 항목을 적성함
- 동일 항목에 대하여는 name을 지정하고 선택된 항목에 대한 value를 지정해야 함
  - checkbox : 다중 선택
  - radio : 단일 선택

\<input>유형 - 기타

- 다양한 종류의 input을 위한 picker를 제공
  - color : color picker
  - date : date picker
- hidden input을 활용하여 사용자 입력을 받지 않고 서버에 전송되어야 하는 값을 설정
  - hidden : 사용자에게 보이지 않는 input

### label

- label을 클릭하여 input 자체의 초점을 맞추거나 활성화 시킬 수 있음.
  - 사용자는 선택할 수 있는 영역이 늘어나 웹 / 모바일(터치) 환경에서 편하게 사용할 수 있음.
  - label과 input 입력의 관계가 시각적 뿐만 아니라 화면리더기에서도 label을 읽어 쉽게 내용을 확인 할 수 있도록 함.
- \<imput>에 id 속성을, \<laber>에는 for 속성을 활용하여 상호 연관을 시킴.

```html
<label for="agreement">개인정보 수집에 동의합니다.</label>
<input type="checkbox" name="agreement" id="agreement">
```



```html
<div>
    <p>checkbox</p>
    <input id="html" type="checkbox" name="language" value="html">
    <label for="html">HTML</label>
    <input id="python" type="checkbox" name="language" value="python">
    <label for="python">파이썬</label>
    <input id="python" type="checkbox" name="language" value="java">
    <label for="java">자바</label>
    <hr>
</div>
```

![checkbox](C:\Users\dlrke\OneDrive\문서\GitHub\국비지원학원\TIL\html\수업자료 정리\0905.assets\checkbox.JPG)

# html form guide

[html form guide](https://developer.mozilla.org/ko/docs/Learn/Forms)

## 기능 간단히 정리

button : 말 그대로 버튼

datalist : A,B,C,D,E등 선택지를 만들고 박스를 클릭하면 목록이 나오게 할 수 있다. 

optgroup : 선택지(option)를 그룹으로 묶어 보여 줄 수 있다. 

select : datalist랑 차이점이 datalist는 빈칸인데, 이거는 옵션을 선택해 달라고 써 있다. 

option : \<select>, \<optgroup>, \<datalist>랑 같이 쓰여, 선택지를 나타낼 때 사용. 

fieldset : 선택지를 한눈에 보이게 하고 체크 할 수 있다. 

legend : fieldset과 같이 쓰여서 무엇에 대한 체크인지 설명

form : 정보를 제출 할 수 있는 주관식 박스 품

input : 정보 입력 박스

output : for에 input 값을 받아 결과를 나타낼 수 있다. 

label : 사용자 인터페이스 항목의 설명을 나타내고, 주로 input과 같이 쓰여 내가 뭘 쓰고 있는지를 알게 해 줍니다. 

keygen : 모양은 없으나 "\<keygen> 요소의 목적은 사용자를 인증하는 안전한 방법을 제공하는 것입니다. from이 제출되면 개인 키와 공개 키의 두 가지 키가 생성됩니다. 개인 키는 로컬에 저장되고 공개 키는 서버로 전송됩니다. 공개 키는 향후 사용자를 인증하기 위해 클라이언트 인증서를 생성하는 데 사용됩니다. "  이렇게 써 있음.  아직 어느 상황에 써야 하는지는 모르겠음.

meter : 게이지 바를 나타냄. (hp게이지 바랑 비슷함)

progress : 작업의 완료 정도를 표현. meter이랑 비슷한데 뭐가 다른지는 아직 모르겠음. 

textarea : 텍스트 메모장 처럼 네모난 텍스트 창을 만들 수 있다. 



속성은 필요한 순간에 그때그때 예시를 보면서 공부 해 나가면 될거 같다. 

