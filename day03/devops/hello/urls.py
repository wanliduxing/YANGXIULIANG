from django.urls import path, re_path
from . import views, views2

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
    # re_path('management/delete/(?P<pk>[0-9]+)?/', views.dele, name='dele'),
    path('management/delete/<int:pk>/', views.dele, name='dele'),
    # re_path('management/modify/(?P<pk>[0-9]+)?/', views.mod, name='mod')
    path('management/modify/<int:pk>/', views.mod, name='mod'),

    # cbv
    path('cbv/management/', views2.managementView.as_view(), name='cbvmanagement'),
    path('cbv/add/', views2.addView.as_view(), name='cbvadd'),
    path('cbv/delete/<int:pk>/', views2.delView.as_view(), name='cbvdel'),
    path('cbv/mod/<int:pk>/', views2.modView.as_view(), name='cbvmod'),
]