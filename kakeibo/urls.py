"""
    家計簿アプリ
    URL定義
    
    Filename urls.py
    Date:2025.1.24
    Written by
"""
from django.urls import path
from . import views

app_name='kakeibo'
urlpatterns=[
    path('',views.kakeibo_list,name='kakeibo_list'),
    path('kakeibo/<int:pk>/',views.kakeibo_detail,name='kakeibo_detail'),
]