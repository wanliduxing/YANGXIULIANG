"""devops URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# 从hello app中定义一个views.py模块index函数来处理hello这个用户请求
from hello import views

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    # 如果hello总入口直接指向具体的app的具体方法，一旦app过多，路由过多，主入口不堪重负，要分而治之
    # 当你访问hello的时候，我不知道具体方法，而是告诉你去hello的app的urls.py
    # path('hello/', views.index)
    path('hello/', include('hello.urls'))
]
