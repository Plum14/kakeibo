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
    path('kekeibo/add/', views.KakeiboCreateView.as_view(), name='kakeibo_add'),
    path('kakeibo/<int:pk>/update/',views.KakeiboUpdateView.as_view(),name='kakeibo_update'),
    #path('kakeibo/<int:pk>/',views.kakeibo_detail,name='kakeibo_detail'),
    path('kakeibo/<int:pk>/',views.kakeibo_detail,name='kakeibo_detail'),
    path('kakeibo/<int:pk>/delete/',views.KakeiboDeleteView.as_view(),name='kakeibo_delete'),
]