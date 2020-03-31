from django.urls import path, re_path
from . import views

app_name = 'hello'

# 实现访问 http://ip:8001/hello  或者 http://ip:8001/hello/hello  都可以返回views.index函数处理的结果
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