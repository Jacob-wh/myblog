"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from blog.views import *

urlpatterns = [
    url(r'^loadRandomApi$' , loadRandomApi),  #加载随机文章
    url(r'^loginlog$' , loginlog),      #访问日志
    url(r'^manage-user$' , manageuser), #管理管理员页面
    url(r'^flink$' , flink),            #留言页面
    url(r'^comment$' , comment),        #评论页面
    url(r'^notice$' , notice),          #公告页面
    url(r'^rootArticle$' , rootArticle),    #管理文章页面
    url(r'^rootIndex$' , rootIndex),       #管理员页面
    url(r'^messages$' , messages),      #留言页面
    url(r'^studyNotes$' , studyNotes),#学习笔记路由
	url(r'^aboutMe$' , aboutMe),  #个人介绍页面
    url(r'^live$' , live),        #生活笔记
    url(r'^base$' , base),          #基页面
    url(r'^qqLogin$' , qqLogin),  #第三方登陆页面
    url(r'^login$',login) ,   #管理员登陆页面
    url(r'^pictures$' , pictures),#相册页面
    url(r'^blogDetail$', blogDetail),  #文章的具体页面
    url(r'^addBlog$', addBlog),#添加博客文章页面
    url(r'^manage$', manage),   #管理员页面
    url(r'^admin/', admin.site.urls),#django 的主页面
    url(r'^$' , home),      #主页面
    url(r'^', error),             #404页面
]
