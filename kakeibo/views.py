"""
    家計簿アプリ
    表示用の機能作成
    
    Filename views.py
    Date:2025.1.24
    Written by
"""
from django.shortcuts import render,reverse
from django.views.generic import View,DetailView,CreateView,UpdateView,DeleteView,ListView
from django.utils import timezone
from .models import kakeibo
from .form import KakeiboForm,kakeiboSearchForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

class kakeiboListView(ListView):
#    def get(self,request,*arg,**kwargs):
    """
        Get request 用の処理
        家計簿一覧を表示する
    """
    model=kakeibo
    template_name='kakeibo/kakeibo_list.html'
    paginate_by=5
    
    def get_queryset(self):
        """
            検索条件の設定
        """
        #フォームを設定
        form=kakeiboSearchForm(self.request.GET or None)
        self.form=form
        
        #フォームが指定したキーワードを取得
        queryset=super().get_queryset()
        if form.is_valid():
            key_word=form.cleaned_data.get('key_word')
            
            if key_word:
                for word in key_word.split():
                    queryset=queryset.filter(Q(memo__icontains=word) |Q(category__text__icontains=word))
        #家計簿データを取得
        return queryset
    
    def get_context_data(self,**kwargs):
        """
            コンテキストの設定
        """
        context=super().get_context_data(**kwargs)
        context['form']=self.form
        return context
    
kakeibo_list=kakeiboListView.as_view()

class kakeiboDetailView(DetailView):
    model=kakeibo
    template_name= "kakeibo/kakeibo_detail.html"
    
kakeibo_detail=kakeiboDetailView.as_view()

class KakeiboCreateView(LoginRequiredMixin,CreateView):
    """
        ブログ記事作成用のビュー
    """
    model=kakeibo #対象とするモデル
    form_class=KakeiboForm #使用するフォームクラス
    template_name="kakeibo/kakeibo_add.html" #テンプレート
    
    def form_valid(self,form):
        #ユーザを追加
        form.instance.author=self.request.user
        
        return super().form_valid(form)
    
    def get_success_url(self):
        """一覧画面にリダイレクトする"""
        return reverse('kakeibo:kakeibo_list')
    
class KakeiboUpdateView(LoginRequiredMixin,UpdateView):
    """
        変更ページのビュー
    """
    model=kakeibo
    form_class=KakeiboForm
    template_name='kakeibo/kakeibo_update.html'
    
    def get_success_url(self):
        """詳細画面にリダイレクトする"""
        return reverse('kakeibo:kakeibo_detail',args=(self.object.id,))
    
class KakeiboDeleteView(LoginRequiredMixin,DeleteView):
    """
        削除用のビュー
    """
    model=kakeibo
    template_name='kakeibo/kakeibo_delete.html'
    def get_success_url(self):
        """一覧ページにリダイレクトする"""
        return reverse('kakeibo:kakeibo_list')