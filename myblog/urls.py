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
	url(r'^aboutMe/$' , aboutMe),  #个人介绍页面
    url(r'^base/$' , base),
    url(r'^qqLogin/$' , qqLogin),  #第三方登陆页面
    url(r'^login/$',login) ,   #管理员登陆页面
    url(r'^pictures/$' , pictures),#相册页面
    url(r'^blogDetail/$', blogDetail),  #文章的具体页面
    url(r'^addBlog/$', addBlog),#添加博客文章页面
    url(r'^manage/$', manage),   #管理员页面
    url(r'^$' , home),      #主页面
    url(r'^', error),             #404页面
    # url(r'^admin/', admin.site.urls),#django 的主页面
]
