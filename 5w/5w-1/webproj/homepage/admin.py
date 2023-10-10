from django.contrib import admin
from .models import COFFEE
# 모델을 자유롭게 관리 
# superUser page에서 모델을 관리가능 

# Register your models here.
admin.site.register(COFFEE) # 관리자 페이지에 관리할 모델로 추가
