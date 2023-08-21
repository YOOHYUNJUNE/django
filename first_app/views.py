from django.shortcuts import render
import random
import requests
from faker import Faker

# Create your views here.
def index(request):
    return render(request, 'index.html')

def hello(request):
    username = '유현준'
    result = {
        'username': username,
    }
    return render(request, 'hello.html', result)

def lunch(request):
    menus = ['라면', '김밥', '치킨', '돈가스']
    pick = random.choice(menus)
    result = {
        'pick': pick,
    }
    return render(request, 'lunch.html', result)

def lotto(request):
    nums = range(1, 46)
    lotto = sorted(random.sample(nums, 6))
    URL = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1081'
    respones = requests.get(URL)
    data = respones.json()
    
    no1 = data['drwtNo1']
    no2 = data['drwtNo2']
    no3 = data['drwtNo3']
    no4 = data['drwtNo4']
    no5 = data['drwtNo5']
    no6 = data['drwtNo6']
    lotto_nums = [no1, no2, no3, no4, no5, no6]

    num = set(lotto) & set(lotto_nums)
    
    result = {
        'lotto': lotto,
        'lotto_nums' : lotto_nums,
        'num': num,
    }
    return render(request, 'lotto.html', result)

def greeting(request, name):
    result = {
        'name': name,
    }
    return render(request, 'greeting.html', result)

def cube(request, num):
    result = {
        'num': num,
        'cube': num ** 3,
    }
    return render(request, 'cube.html', result)

def posts(request):
    fake = Faker()
    fake_posts = []
    for i in range(100):
        fake_posts.append( fake.text() )
    result = {
        'posts': fake_posts,
    }
    return render(request, 'posts.html', result)