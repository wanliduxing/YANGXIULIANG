from django.shortcuts import render, redirect
from django.http import HttpResponse, QueryDict
from django.contrib import messages
from hello.models import User


# from hello.modeles import User


# Create your views here.

# def index(request):
#     return HttpResponse("<p>Hello World,Hello Django!</p>")

# def index(request):
#     year = request.GET.get("year", "2020")
#     month = request.GET.get("month", "01")
#     return HttpResponse("year is %s,month is %s" % (year, month))

# def index(request, **kwargs):
#     print(kwargs)
#     year = kwargs.get('year')
#     month = kwargs.get('month')
#     return HttpResponse("year is %s,month is %s" % (year, month))

# def index(request):
#     print(request.scheme)
#     print(request.method)
#     print(request.headers)
#     print(request.path)
#     print(request.META)
#     print(request.GET)
#     data = request.GET
#     year = data.get("year", "2019")
#     month = data.get("month", "05")
#     if request.method == 'POST':
#         print(request.method)
#         print(request.body)
#         print(QueryDict(request.body).dict())
#         print(request.POST)
#         data = request.POST
#         year = data.get("year", "2019")
#         month = data.get("month", "05")
#     return HttpResponse("year is %s,month is %s" % (year, month))

def index(request):
    classname = "DevOps"
    books = ['Python', 'Java', 'Django']
    user = {'name': 'kk', 'age': 18}
    userlist = [{'name': 'kk', 'age': 18}, {'name': 'rock', 'age': 19},
                {'name': 'mage', 'age': 20}]
    return render(request, "hello/hello.html",
                  {'classname': classname, 'books': books, 'user': user, 'userlist': userlist})


def list(request):
    users = [
        {'username': 'kk1', 'name_cn': 'kk1', 'age': 18},
        {'username': 'kk2', 'name_cn': 'kk2', 'age': 19},
        {'username': 'kk3', 'name_cn': 'kk3', 'age': 20},
    ]
    return render(request, 'hello/userlist.html', {'users': users})


def test(request):
    return render(request, "hello/test.html")


def userlist(request):
    users = User.objects.all()
    return render(request, 'index.html', {'users': users})


def management(request):
    users = User.objects.all()
    return render(request, 'management.html', {'users': users})


def add(request):
    return render(request, 'add.html')


def addsuccess(request):
    print(request.POST)
    data = request.POST
    name = data.get("name")
    password = data.get("password")
    sex = data.get("sex")
    User.objects.create(name=name, password=password, sex=sex)
    return render(request, 'addsuccess.html')



def dele(request, id):
    user = User.objects.all().filter(id=id)
    print(user)
    return render(request, 'dele.html', {'user': user})


def delesuccess(request, id):
    User.objects.filter(id=id).delete()
    return render(request, 'delesuccess.html')


def mod(request, id):
    user = User.objects.all().filter(id=id)
    return render(request, 'mod.html', {'user': user})


def modsuccess(request, id):
    print(request.POST)
    res = request.POST
    name = res.get("name")
    id = request.POST.get("id")
    password = res.get("password")
    sex = res.get("sex")
    User.objects.filter(id=id).update(name=name, password=password, sex=sex)
    return render(request, 'modsuccess.html', {'user': name})