from django.shortcuts import render

# Create your views here.
def first(request):
    return render(request,'first.html')
def second(request):
    return render(request,'second.html')
def third(request):
    return render(request,'third.html')
def four(request):
    return render(request,'four.html')
