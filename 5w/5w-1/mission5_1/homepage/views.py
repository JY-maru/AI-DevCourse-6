from django.shortcuts import render,redirect
from .forms import BurgerForm, BurgerUpdateDelete
from .models import Burger
from django.http import Http404

# Create your views here.
def aboutme(request):
    return render(request, "aboutMe.html", {} )

def burgerGet(request):
    burger_all = Burger.objects.all() 
    if request.method =="POST":
        form = BurgerForm(request.POST) # 완성된 Form을 만들기
        if form.is_valid(): # 채워진 form이 유효시, Model에 저장.
            form.save()
    form = BurgerForm()
        
    return render(request, 'burger.html',{"burger_list": burger_all, 'burger_form':form})

# def burgerAdd(request):
#     if request.method == "POST":
#         form = BurgerForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/burgers')
#     else : 
#         return burgerGet(request)
    
def burgerUpdate(request, pk):
    try:
        burger = Burger.objects.get(name=pk)
    except Burger.DoesNotExist:
        raise Http404(f"{pk} does not Exist")
    
    if request.method == 'PUT':
        form = BurgerForm(request.PUT, instance=burger)
        render(request, 'burger.html', {"burger_name":burger.name})
        if form.is_valid():
            form.save()
            return redirect('/burgers')
    else : 
        form = BurgerForm()
        return render(request, 'burger.html', {"burger_form":form})

def burgerDel(reqest,pk):
    try: burger = Burger.objects.get(name=pk)
    except Burger.DoesNotExist:
        raise Http404(f'{pk} does not exist')
    if reqest.method == 'DELETE':
        form = BurgerUpdateDelete(reqest.DELETE, instance=burger)
        if form.is_valid():
            burger.delete()
    return redirect('/burgers')
