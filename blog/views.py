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
    return HttpResponse("pictures");

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
    return HttpResponse("留言板")

