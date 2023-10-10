from django import forms
from .models import Burger

class BurgerForm(forms.ModelForm): # ModelForm을 상속받는 CoffeeForm 생성
    class Meta:
        model = Burger
        # 어떤 필드를 Form으로부터 받을 지 지정
        fields = ('name','price','is_set')

class BurgerUpdateDelete(forms.ModelForm):
    class Meta:
        model = Burger
        fields = ('name',)
