from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, QueryDict, Http404
from django.contrib import messages
import traceback
from .models import User


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
    keyword = request.GET.get("keyword", "")
    print(keyword)
    users = User.objects.all()
    if keyword:
        users = users.filter(name__icontains=keyword)
        print(users)
    return render(request, 'management.html', {'users': users, 'keyword': keyword})


def add(request):
    msg = {}

    if request.method == "POST":
        try:
            data = request.POST.dict()
            print(data)
            User.objects.create(**data)
            msg = {"code": 0, "result": "恭喜你，添加用户成功！！"}
        except:
            msg = {"code": 1, "errmsg": "抱歉！添加用户失败： %s" % traceback.format_exc()}
    return render(request, 'add.html', {"msg": msg})


def dele(request, **kwargs):
    msg = {}
    print(kwargs)
    pk = kwargs.get("pk")
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        raise Http404

    if request.method == "POST":
        try:
            User.objects.get(pk=pk).delete()
            msg = {"code": 0, "result": "恭喜你，删除用户成功！！"}
        except:
            msg = {"code": 1, "errmsg": "抱歉！删除用户失败： %s" % traceback.format_exc()}
    return render(request, 'dele.html', {'user': user, 'msg': msg})

def mod(request, **kwargs):
    msg = {}
    print(kwargs)
    pk = kwargs.get("pk")
    user = get_object_or_404(User, pk=pk)

    if request.method == "POST":
        try:
            data = request.POST.dict()
            print(data)
            User.objects.filter(pk=pk).update(**data)
            msg = {"code": 0, "result": "恭喜你，更新用户信息成功！！"}
        except:
            msg = {"code": 1, "errmsg": "抱歉！更新用户信息失败： %s" % traceback.format_exc()}
    return render(request, 'mod.html', {'user': user, 'msg': msg})
