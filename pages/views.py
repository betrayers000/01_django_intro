from django.shortcuts import render
import random
import datetime

# Create your views here.
def index(request):
    return render(request, 'index.html')

def dinner(request):
    menu = ['중식', '한식', '양식', '베트남식']
    pick = random.choice(menu)
    context = {
        'pick': pick,
        'menu': menu,
    }
    return render(request, 'dinner.html', context) 

def image(request):
    context = {
        'image_url': "https://picsum.photos/200",
    }
    return render(request, 'image.html', context)

def greeting(request, name):
    context = {
        'name': name,
    }
    return render(request, 'greeting.html', context)

def cube(request, num):
    cubic = num ** 3
    context = {
        'num': num,
        'cubic': cubic,
    }
    return render(request, 'cube.html', context)

def mul(request, num1, num2):
    multi = num1 * num2
    context ={
        'num1': num1,
        'num2': num2,
        'multi': multi,
    }
    return render(request, 'mul.html', context)

def dtl(request):
    menus = ['한식', '중식', '양식', '일식']

    sentence = 'Life is short you need python'
    messages = {
        'apple': '사과',
        'banana': '바나나',
        'peach': '복숭아',
    }
        
    now = datetime.datetime.now()
    empty = []
    context = {
        'menus': menus,
        'now': now,
        'messages': messages,
        'setence': sentence,
        'empty': empty, 
    }

    return render(request, 'dtl.html', context)

def christmas(request):
    now = datetime.datetime.now().strftime("%m-%d")
    mx = datetime.datetime(2019, 12, 25).strftime("%m-%d")
    if now == mx :
        result = True 
    else : 
        result = False
    context = {
        'result': result
    }
    return render(request, 'christmas.html', context)
    