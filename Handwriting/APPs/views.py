import base64
import os.path

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from .models import WSkills, WordSkills
# Create your views here.


#首页
def index(request):
    data = WSkills.objects.get(SkillName='侧点')
    return render(request, 'BasPrac.html', {'data': data})

#注册
def register(request):
    return render(request, 'register.html')

#登录
def login(request):
    return render(request, 'login.html')

def logout(request):
    return render(request, 'logout.html')

#基础笔画
def BasicPrac(request):
    return render(request, 'BasPrac.html')

def AdPrac(request):
    data = WordSkills.objects.get(SkillName='侧点')
    return render(request, 'AdPrac.html', {'data': data})

#上传图片，媒体文件
def upload(request):
    if request.method == 'POST':
        return render(request, 'upload.html')

    elif request.method == 'GET':
        uname = request.POST.get('uname')
        img = request.FILES.get('icon')
        #print(uname, img)

        return render(request, 'upload.html')

def sava_canvas(request):
    if request.method == 'POST':
        data_url = request.POST.get('dataURL')
        if data_url:
            #解码data_URL
            image_data = base64.b64decode(data_url.split(',')[1])
            #获取保存路径
            sava_path = os.path.join(settings.STATIC_ROOT, 'img', 'written_txt.jpg')
            #保存图像
            with open(sava_path, 'wb') as f:
                f.write(image_data)

            return HttpResponse('')




