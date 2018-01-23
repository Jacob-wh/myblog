from django.shortcuts import render

from django.http import HttpResponse

import requests

import base64  
import json 

import subprocess  
import datetime  
import sys  
import os  
import time  
from pydub import AudioSegment  

from aip import  AipSpeech

import subprocess


# Create your views here.

def home(request):
    return render(request , "home.html");




def manage(request):
    return render(request , "manage.html");


def adManage(request):
    return render(request , "adManage.html");


def get_wave_filename(fileFullName):  
    # MP3文件转换成wav文件  
    # 判断文件后缀，是mp3的，直接处理为16k采样率的wav文件；  
    # 是wav的，判断文件的采样率，不是8k或者16k的，直接处理为16k的采样率的wav文件  
    # 其他情况，就直接返回AudioSegment直接处理  
    fileSufix = fileFullName[fileFullName.rfind('.')+1:]  
    print(fileSufix)  
    filePath = fileFullName[fileFullName.find(os.sep)+1]  
    print(filePath)  
    if fileSufix.lower() == "wav":  
        wavFile = "audio.wav"
        cmdLine = "ffmpeg -i D:\myfile\python\myblog\%s -ar 16000 -ac 1 " %fileFullName  
        cmdLine = cmdLine + "D:\myfile\python\myblog\%s" %wavFile  
        print(cmdLine)  
        ret = subprocess.run(cmdLine)
        print("ret code:%i" %ret.returncode)  
        return wavFile
    else:  
        return fileFullName



def test(request):
    print (os.path.abspath("a.wav"));
    # wavFile = get_wave_filename("a.wav") ;
    audioObj = AudioSegment.from_wav("a.wav" , "wav");
    audioObj.set_channels(1);
    audioObj.set_frame_rate(16000);
    audioObj.export("aa.wav" , "wav");
    d = open('aa.wav', 'rb').read()
    APP_ID = '10573104'
    API_KEY = 'iGPGdtRjwadhpRdsG89iSIrp'
    SECRET_KEY = '1c169dc662f8bfdf88f73fe3e8a1940d'
    
    aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    
    print ("hhhhhhhhhhhhhhhhhhhhhh")
    # 识别本地文件
    #目前支持的格式较少，原始 PCM 的录音参数必须符合 8k/16k 采样率、16bit 位深、单声道，支持的格式有：pcm（不压缩）、wav（不压缩，pcm编码）、amr（压缩格式）。
    result = aipSpeech.asr(d, 'wav', 16000, {'lan': 'zh',});
    print (result);
    # print result['result'][0]
    return HttpResponse(result);
    