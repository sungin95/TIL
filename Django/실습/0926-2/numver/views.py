import random
from django.shortcuts import render

# Create your views here.
def is_odd_even(request, number):
    if number == 0:
        A = "0"
    elif number % 2 == 0:
        A = "짝수"
    elif number % 2 == 1:
        A = "홀수"
    content = {
        "num": number,
        "odd_even": A,
    }

    return render(request, "is_odd_even.html", content)


def is_odd_even_alert(request):

    return render(request, "is_odd_even_alert.html")


def calculate(request, number, number2):
    A = number + number2
    B = number - number2
    C = number * number2
    if number2 == 0:
        D = "무한"
    else:
        D = number // number2
    content = {
        "num1": number,
        "num2": number2,
        "addition": A,
        "subtraction": B,
        "multiplication": C,
        "division": D,
    }
    return render(request, "calculate.html", content)


def previous_life(request):

    return render(request, "previous_life.html")


def previous_life_check(request):
    A = ["아이언맨", "타노스", "스파이터맨", "시민", "스폰지밥", "해리포터"]
    B = random.choice(A)
    name = request.GET.get("name")
    context = {
        "pre_life": B,
        "name": name,
    }
    return render(request, "previous_life_check.html", context)


def index(request):

    return render(request, "index.html")


def lipsum(request):

    return render(request, "lipsum.html")


def lipsum_check(request):
    paragraphs = request.GET.get("paragraphs")
    words = request.GET.get("words")
    arr = ["바나나", "짜장면", "포도", "딸기", "사과"]
    words = int(words)
    paragraphs = int(paragraphs)
    random_words = []
    random_paragraphs = []
    cnt = 0
    while True:
        if cnt == paragraphs:
            break
        cnt += 1
        random_paragraphs.append("A")
    cnt = 0
    while True:
        if cnt == words:
            break
        cnt += 1
        A = random.choice(arr)
        random_words.append(A)
    context = {
        "paragraphs": random_paragraphs,
        "words": random_words,
    }
    return render(request, "lipsum_check.html", context)
