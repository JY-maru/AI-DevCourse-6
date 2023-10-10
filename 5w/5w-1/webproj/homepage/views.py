from django.shortcuts import HttpResponse, render
from .models import COFFEE
from .forms import CoffeeForm

# 앱 내 뷰 관리

# Create your views here.
def index(request):
    nums = [1,2,3,4,5,6,7]

    #return HttpResponse("<h1>Hello World!</h1>")
    return render(request, 'index.html', {"my_list" : nums}) # 딕셔너리 내용으로 html에 내용 추가.

def coffee_view(request):
    cofffee_all = COFFEE.objects.all() # .get(), .filter()
    # 만약 request가 POST :
        # POST를 바탕으로 Form을 완성.
        # Form이 유효 -> 저장
    if request.method =="POST":
        form = CoffeeForm(request.POST) # 완성된 Form을 만들기
        if form.is_valid(): # 채워진 form이 유효시, Model에 저장.
            form.save()
    form = CoffeeForm()
    return render(request, 'coffee.html',{"coffee_list": cofffee_all, 'coffee_form':form})
