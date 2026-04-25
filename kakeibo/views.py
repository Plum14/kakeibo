"""
    家計簿アプリ
    表示用の機能作成
    
    Filename views.py
    Date:2025.1.24
    Written by
"""
from django.shortcuts import render
from django.views.generic import View,DetailView
from django.utils import timezone
from .models import kakeibo

class kakeiboListView(View):
    def get(self,request,*arg,**kwargs):
        """
            Get request 用の処理
            ブログ記事一覧を表示する
        """
        context ={}
        posts=kakeibo.objects.all()
        context['posts']=posts
        return render(request,"kakeibo/kakeibo_list.html",context)
    
kakeibo_list=kakeiboListView.as_view()

class kakeiboDetailView(DetailView):
    model=kakeibo
    template_name= "kakeibo/kakeibo_detail.html"
    
kakeibo_detail=kakeiboDetailView.as_view()