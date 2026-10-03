"""

    家計簿アプリ
    フォームクラス
    
    Filename forms.py
    
"""
from django.forms import ModelForm
from django import forms
from .models import kakeibo

class KakeiboForm(ModelForm):
    """
        家計簿登録画面用のフォーム
        memo メモ
        date 日付
        category カテゴリ
        maney 金額
    """
    class Meta:
        #モデルクラスを指定
        model=kakeibo
        #モデルフィールドを指定
        fields=("memo","date","category","money")
        labels={
            'memo':'メモ',
            'date':'日付',
            'category':'カテゴリ',
            'money':'金額',
        }
        
class kakeiboSearchForm(forms.Form):
    """
        検索用のフォーム
    """
    key_word=forms.CharField(label='検索キーワード',required=False)