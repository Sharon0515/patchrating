"""patchrating URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from ratingapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.experiment_intro, name='experiment_intro'),      # 实验内容告知和教学
    path('enter_info/', views.enter_info, name='enter_info'),       # 输入年龄、性别和被试编号
    path('experiment/<int:tester_id>/', views.experiment, name='experiment'),       # 正式实验界面
    path('thank_you/', views.thank_you, name='thank_you'),  # 感谢页面
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)