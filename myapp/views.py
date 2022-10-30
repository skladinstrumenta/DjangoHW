from random import randint

from django.shortcuts import render

def index(request):
    data = {
        "number": randint(0, 100),
        "my_list": [1, 23, 44]
    }
    return render(request, 'index.html', data)

def article(request, id):
    return render(request, 'article.html', {'id': id})
