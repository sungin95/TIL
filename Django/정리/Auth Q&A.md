# Auth Q&A

Q. accounts.User에 만들고 시작하는지? 왜 auth.User를 사용하지 않는지?

* settings.py: AUTH_USER_MODEL
* accounts앱에 AbstractUser를 상속받아서 빈 껍데기(pass)

내 생각: 장고가 미리 제공은 해 주지만 가져오는 사람마다 필요한 정보가 다르기 때문에 

샘 말 듣고: 수정 가능한 코드로 만들기 위해. (이걸 안하고 수정하려면 기존의 데이터를 삭제해야 한다. )



Q. class상속이란?

속성이나 메서드를 덧씌우는것



Q. get_user_model의 사용 이유?

{% url 'articles:index' %}  를 사용하는 이유와 비슷하다. 

(그러니까 미래에 있을지 모르는 수정을 위해서라고 이해 할면 되는 걸까?)