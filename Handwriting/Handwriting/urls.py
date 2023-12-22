
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from APPs.views import *

urlpatterns = [
    #首页
    path('', index),
    path('index/', index),
    #基础笔画
    path('BasicPrac/', BasicPrac),

    path('AdPrac/', AdPrac),

    # 登录、注销
    path('login/', login),
    path('logout/', login),
    path('admin/', admin.site.urls),

    #上传
    path('upload/', upload, name='upload'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
