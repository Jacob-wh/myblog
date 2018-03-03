from django.shortcuts import render
from django.http import HttpResponse
import base64  
import json 
import subprocess  
import datetime  
import sys  
import os  
import time  
import subprocess
from PIL import Image
import sys
from io import TextIOBase
from xml import dom , sax , parsers , etree
from flask import Flask


# Create your views here.
#主页
def home(request):
    return render(request , "home.html");

def error(request):
    return HttpResponse("404,页面不存在哦。。。。")

#管理员页面
def manage(request):
    return render(request , "manage.html");

#添加文章路由实现
def addBlog(request):
    return render(request , "addBlog.html");

#相册
def pictures(request):
    return render(request , "pictures.html");

#博客详情
def blogDetail(request):
    return render(request , "blogDetail.html")

def login(request):
    return HttpResponse("login")

def qqLogin(request):

    return HttpResponse("qqLogin")

def base(request):
    return render(request , "base.html")
	
def aboutMe(request):
	return render(request , "aboutMe.html");

def live(request):
    return render(request , "live.html");


def studyNotes(request):
    return render(request , "studyNotes.html");

def messages(request):
    return render(request , "message.html")


def rootIndex(request):
    return render(request , "index.html")

def rootArticle(request):
    return render(request , "article.html")


def notice(request):
    return render(request , "notice.html")

def comment(request):
    return render(request , "comment.html")
#留言返回页面
def flink(request):
    return render(request , "flink.html")

def loginlog(request):
    return render(request , "loginlog.html")

def manageuser(request):
    return render(request , "manage-user.html")
#加载随机文章在主页面上
def loadRandomApi(request):
    try:
        sqlcount = "select count(*) from article";
        sql = "select * from article order by rand() limit 10";
    except Exception as identifier:
        print(identifier);
