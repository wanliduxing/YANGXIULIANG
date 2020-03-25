from django.urls import path
from . import views

# 实现访问 http://ip:8001/hello  或者 http://ip:8001/hello/hello  都可以返回views.index函数处理的结果
urlpatterns = [
    path('hello/', views.index, name='index1'),
    path('', views.index, name='index2')
]