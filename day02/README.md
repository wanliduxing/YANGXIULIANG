#### 简单的用户管理系统实现用户的增删改查
>urls部分
```python
urlpatterns = [
    path('hello/', views.index, name='index'),
    path('', views.index, name='index'),
    re_path('(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/', views.index, name='index'),
    path('list/', views.list, name='list'),
    path('test/', views.test, name='test'),
    path('userlist/', views.userlist, name='userlist'),
    path('management/', views.management, name='management'),
    path('management/add/', views.add, name='add'),
    path('management/add/addsuccess/', views.addsuccess, name='addsuccess'),
    path('management/<int:id>/dele/', views.dele, name='dele'),
    path('management/<int:id>/dele/delesuccess/', views.delesuccess, name='delesuccess'),
    path('management/<int:id>/mod/', views.mod, name='mod'),
    path('management/<int:id>/mod/modsuccess/', views.modsuccess, name='modsuccess'),
]
```
>views部分
```python
# 查看
def management(request):
    users = User.objects.all()
    return render(request, 'management.html', {'users': users})

# 新增
def add(request):
    return render(request, 'add.html')

# 新增成功后入库
def addsuccess(request):
    print(request.POST)
    data = request.POST
    name = data.get("name")
    password = data.get("password")
    sex = data.get("sex")
    User.objects.create(name=name, password=password, sex=sex)
    return render(request, 'addsuccess.html')


# 删除确认
def dele(request, id):
    user = User.objects.all().filter(id=id)
    print(user)
    return render(request, 'dele.html', {'user': user})

# 删除成功，执行删库
def delesuccess(request, id):
    User.objects.filter(id=id).delete()
    return render(request, 'delesuccess.html')

# 修改确认
def mod(request, id):
    user = User.objects.all().filter(id=id)
    return render(request, 'mod.html', {'user': user})

# 修改成功，执行update
def modsuccess(request, id):
    print(request.POST)
    res = request.POST
    name = res.get("name")
    id = request.POST.get("id")
    password = res.get("password")
    sex = res.get("sex")
    User.objects.filter(id=id).update(name=name, password=password, sex=sex)
    return render(request, 'modsuccess.html', {'user': name})
```
>实现效果：
##### 查看所有——
![avatar](https://cdn.jsdelivr.net/gh/YanYuHanYun/image/406d460cbba23e21721c76aec752409e.png)
##### 新增用户——
![avatar](https://cdn.jsdelivr.net/gh/YanYuHanYun/image/c4de25c75e7c8e5f266fb7b7f92eb158.png)
![avatar](https://cdn.jsdelivr.net/gh/YanYuHanYun/image/8c4c5857d035ecf74c6475559a4a3f0f.png)
![avatar](https://cdn.jsdelivr.net/gh/YanYuHanYun/image/68e67b3e1e22ee10e7a866d536048675.png)
##### 修改用户——
![avatar](https://cdn.jsdelivr.net/gh/YanYuHanYun/image/1cfcbd17ec77015c9f86c3566ef28a7e.png)
![avatar](https://cdn.jsdelivr.net/gh/YanYuHanYun/image/d7ac3b026830679181b47aae99c63bc0.png)
![avatar](https://cdn.jsdelivr.net/gh/YanYuHanYun/image/623bf556712b80564d1a6f704e6b8cfd.png)
##### 删除用户——
![avatar](https://cdn.jsdelivr.net/gh/YanYuHanYun/image/9c8d4851b7fba5f17c5ff9c2aaa05e02.png)
![avatar](https://cdn.jsdelivr.net/gh/YanYuHanYun/image/fdb362a26bfcce0f8e6096a8a3014d50.png)
![avatar](https://cdn.jsdelivr.net/gh/YanYuHanYun/image/d0838eaa1bf432a86b800ce1f8567ca1.png)