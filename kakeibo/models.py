"""
家計簿アプリ
データモデル

Filename models.py
Data.
    Written by 

"""
from django.db import models
from django.conf import settings
from django.utils import timezone

class Category(models.Model):
    """
        カテゴリのクラス
        text:カテゴリ名
    """
    text=models.TextField(max_length=200)
    
    def __str__(self):
        return self.text

class kakeibo(models.Model):
    """
        家計簿クラス
        date:日付
        category:カテゴリ
        money:金額
        memo:メモ
    """
    date=models.DateTimeField(default=timezone.now)
    category= models.ForeignKey(Category,on_delete=models.CASCADE)
    money=models.IntegerField()
    memo=models.TextField(max_length=200)
    
    def __str__(self):
        return "{} {}".format(self.category,str(self.money))

