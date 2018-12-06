# -*- coding: utf-8 -*-
"""lianxi URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^user/', include('df_user.urls')),
    url(r'^goods/', include('df_goods.urls')),
    url(r'^order/', include('df_order.urls')), #订单
    url(r'^cart/',include('df_cart.urls')),     #购物车
    url(r'^',include('df_goods.urls')),
    url(r'^tinymce/', include('tinymce.urls')),     #富文本编辑器
    # url(r'^search/', include('haystack.urls')),     #全文检索
]

if settings.DEBUG:      #配置静态文件路径
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

