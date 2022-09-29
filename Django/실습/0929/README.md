include("articles.urls")),
return render(request, "articles/index.html")
python manage.py makemigrations
title = request.GET.get("title")
