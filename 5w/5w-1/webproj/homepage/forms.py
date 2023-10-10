from django import forms

from .models import COFFEE

class CoffeeForm(forms.ModelForm): # ModelForm을 상속받는 CoffeeForm 생성
    class Meta:
        model = COFFEE
        # 어떤 필드를 Form으로부터 받을 지 지정
        fields = ('name','price','is_ice')
        
