"""
    家計簿アプリ
    admin用の設定
    
    Filename admin.py
    Date:2025.1.17
    Written by
"""
from django.contrib import admin
from .models import Category
from .models import kakeibo

admin.site.register(Category)
admin.site.register(kakeibo)
