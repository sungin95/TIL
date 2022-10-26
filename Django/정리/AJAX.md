# AJAX

XMLHttpRequest() 이라는 내장 클래스가 있음.

이걸 활용하여 페이지 새로 고침을 하지 않고 페이지 내용을 바꿀 수 있음. 

그런데 이 보다 더 편하게 사용할 수 있는 기능이 있는데 그게 AJAX임.

이게 양식임

```html
<script src="https://unpkg.com/axios/dist/axios.min.js"></script>
<script>
	const URL = 'https://jsonplaceholder.typicode.com/todos/1'
    
    axios.get(URL) // Promise Return 
        .then(res => console.log(res.data.title))
        .catch(err => console.log('Error!’))
</script>
```

문제가 없으면 then 을 작동 시키고 문제가 있으면 catch를 작동시킴. 파이썬의 try-except구문과 비슷하다. 그리고 값은 URL로 보냄. 

```javascript
const URL = 'https://jsonplaceholder.typicode.com/todos/1'

axios.get(URL)
	.then(function (response) {
        console.log(response)
        return response.data
	})
	.then(function (data) {
        return data.title
	})
	.then(function (title) {
        console.log(title)
	})
	.catch(function (error) {
        console.log(error)
	})
	.finally(function () {
        console.log("이건 무조건 실행됩니다.")
	})
```

## 팔로우 만들어 보기

### id를 가져 오기(html과 JS 연결하기)

```html
<!-- accounts/profile.html -->

<form id="follow-form">
	...
</form>
```

```html
<!-- accounts/profile.html -->

<script>
    const form = document.querySelector('#follow-form’)
    form.addEventListener('submit', function (event) {
        event.preventDefault()
            axios({
            method: 'post＇,
            url: `/accounts/${???}/follow/`,
        })
    })
</script>
```

생각해 볼꺼

#### url에 작성할 user pk는 어떻게 작성해야 할까? (userId)

```html
<!-- accounts/profile.html -->

<form id="follow-form" data-user-id="{{ person.pk }}">
	...
</form>

<!-- accounts/profile.html -->
<script>
    const form = document.querySelector('#follow-form’)
    form.addEventListener('submit', function (event) {
        event.preventDefault()
        
        const userId = event.target.dataset.userId
        ...
    })
</script>
```

data-* 란?

[참고 문서](https://developer.mozilla.org/ko/docs/Web/HTML/Global_attributes/data-*)

- 사용자 지정 데이터 특성을 만들어 임의의 데이터를 HTML과 DOM사이에서 교환 할 수 있는 방법

- ```html
  <!-- 사용 예시 -->
  <div data-my-id="my-data"></div>
  <script>
  	const myId = event.target.dataset.myId
  </script>
  ```

- 예를 들어 data-test-value 라는 이름의 특성을 지정했다면 JavaScript에서는 element.dataset.testValue로 접근할 수 있음

- 속성명 작성 시 주의사항 

  - 대소문자 여부에 상관없이 xml로 시작하면 안 됨 
  - 세미콜론을 포함해서는 안됨 
  - 대문자를 포함해서는 안됨

```javascript
axios({
    method: 'post＇,
    url: `/accounts/${userId}/follow/`,
})
```



#### csrftoken은 어떻게 보내야 할까?

[참고 문서](https://docs.djangoproject.com/en/3.2/ref/csrf/)

먼저 hidden 타입으로 숨겨져있는 csrf 값을 가진 input 태그를 선택해야 함(장고가 미리 만들어 놓고 히든까지 시켜 놓은거 같음)

```html
<!-- accounts/profile.html -->

<script>
    const form = document.querySelector('#follow-form＇)
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value <!-- 여기여기 -->
    form.addEventListener('submit', function (event) {
        event.preventDefault()
        const userId = event.target.dataset.userId
        axios({
            method: 'post＇,
            url: `/accounts/${userId}/follow/`,   `
            headers: {'X-CSRFToken': csrftoken,} <!-- 여기여기 -->
        })
</script>
```



### 기능 추가 하기

#### view에 JSON으로 보내게 하기

```python
# accounts/views.py

from django.http import JsonResponse # 여기여기

@require_POST
def follow(request, user_pk):
    if request.user.is_authenticated:
        User = get_user_model()
        me = request.user
        you = User.objects.get(pk=user_pk)
        if me != you:
            if you.followers.filter(pk=me.pk).exists():
                you.followers.remove(me)
                is_followed = False # 여기여기
            else:
                you.followers.add(me)
                is_followed = True # 여기여기
            context = {
            	'is_followed': is_followed,
            }
            return JsonResponse(context) # 여기까지
        return redirect('accounts:profile', you.username)
    return redirect('accounts:login')
```

#### JS에서는...

```html
<script>
    ...
    axios({
        method: 'post＇,
        url: `/accounts/${userId}/follow/`,     `
        headers: {'X-CSRFToken': csrftoken,}
    })
        .then((response) => { <!-- 여기부터 -->
            const isFollowed = response.data.is_followed
            const followBtn = document.querySelector('#follow-form > input[type=submit]’)
            if (isFollowed === true) {
                followBtn.value = '언팔로우’
            } else {
                followBtn.value = '팔로우’
            }
        })
</script>
```



### DB의 값을 비동기로 가져오기

#### id로 연결하기

```html
<!-- accounts/profile.html -->

{% extends 'base.html' %}

{% block content %}
    <h1>{{ person.username }}님의 프로필</h1>
    <div>
        팔로워 : <span id="followers-count">{{ person.followers.all|length }}</span> /
        팔로잉 : <span id="followings-count">{{ person.followings.all|length }}</span>
    </div>
```

#### JS에서 변수로 만들기

```javascript
axios({
    method: 'post＇,
    url: `/accounts/${userId}/follow/`,     `
    headers: {'X-CSRFToken': csrftoken,}
})
    .then((response) => {
        ...
        const followersCountTag = document.querySelector('#followers-count＇)
        const followingsCountTag = document.querySelector('#followings-count')
    })
```

#### view에서 변수화 해서 보내주rh

```python
# accounts/views.py

@require_POST
def follow(request, user_pk):
    ...
        context = {
            'is_followed': is_followed,
            'followers_count': you.followers.count(),
            'followings_count': you.followings.count(),
        }
        return JsonResponse(context)
    return redirect('accounts:profile', you.username)
return redirect('accounts:login')
```

#### 그 값 받아서 최신화 해 주기

```html
<!-- accounts/profile.html -->
<script>
    ...
        axios({
            method: 'post＇,
            url: `/accounts/${userId}/follow/`,   `
            headers: {'X-CSRFToken': csrftoken,}
        })
            .then((response) => {
                ...
                const followersCountTag = document.querySelector('#followers-count＇)
                const followingsCountTag = document.querySelector('#followings-count’)
                followersCountTag.innerText = followersCount
                followingsCountTag.innerText = followingsCount
            })
</script>
```



### 완성된 코드 보기

```html
<!-- accounts/profile.html -->

{% extends 'base.html' %}

{% block content %}
    <h1>{{ person.username }}님의 프로필</h1>
    <div>
        팔로워 : <span id="followers-count">{{ person.followers.all|length }}</span> /
        팔로잉 : <span id="followings-count">{{ person.followings.all|length }}</span>
    </div>

    {% if request.user != person %}
    <div>
        <form id="follow-form" data-user-id="{{ person.pk }}">
            {% csrf_token %}
            {% if request.user in person.followers.all %}
            	<input type="submit" value="언팔로우">
            {% else %}
            	<input type="submit" value="팔로우">
            {% endif %}
        </form>
    <div>
    {% endif %}
...
```

```python
# accounts/views.py

@require_POST
def follow(request, user_pk):
    if request.user.is_authenticated:
        User = get_user_model()
        me = request.user
        you = User.objects.get(pk=user_pk)
        if me != you:
            if you.followers.filter(pk=me.pk).exists():
                you.followers.remove(me)
                is_followed = False
            else:
                you.followers.add(me)
                is_followed = True
            context = {
                'is_followed': is_followed,
                'followers_count': you.followers.count(),
                'followings_count': you.followings.count(),
            }
            return JsonResponse(context)
        return redirect('accounts:profile', you.username)
    return redirect('accounts:login')
```

```javascript
<!-- accounts/profile.html -->
const form = document.querySelector('#follow-form')
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value

form.addEventListener('submit', function (event) {
    event.preventDefault()
    const userId = event.target.dataset.userId
    
    axios({
        method: 'post＇,
        url: `/accounts/${userId}/follow/`,  `
        headers: {'X-CSRFToken': csrftoken,}
    })
        .then((response) => {
            const isFollowed = response.data.is_followed
            const followBtn = document.querySelector('#follow-form > input[type=submit]＇)
            if (isFollowed === true) {
            	followBtn.value = '언팔로우＇
            } else {
            	followBtn.value = '팔로우＇
            }
            const followersCountTag = document.querySelector('#followers-count＇)
            const followingsCountTag = document.querySelector('#followings-count＇)
            const followersCount = response.data.followers_count
            const followingsCount = response.data.followings_count
            followersCountTag.innerText = followersCount
            followingsCountTag.innerText = followingsCount
        })
        .catch((error) => {
        	console.log(error.response)
    })
})
```













자바 스크립트가 중요하다. 



```python
import requests

response = requests.get('https://naver.com')
print(response.text)
```



```javascript
```

자스는 기다리지 않고 실행 (비동기식)



XHR 비동기 요청을 처리해 주는 도구



promiss 도착하면 실행 시켜 줄께 약속



자바스크립트르 먼저 사용한다?

CDN을 해 준다. 



# 좋아요 자바로 보내기

















JSON

타싱 = 영어로 번역

parsing



한국어로 번역 JSON.stringify







비동기 처리

1) 어떤 이벤트 일때 요청을 보낼지
   - form을 작성하면....
   - /articles/<pk>/comments/
2) 서버에서 어떤 응답을JSON으로 보내서 
   - 댓글 정보를 보내서
3) DOM 조작을 어떻게 할지 
   - 댓글 목록을 보여 준다. 