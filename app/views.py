from django.shortcuts import render

# Create your views here.
def morning(request):
    return render(request,'morning.html')

def night(request):
    return render(request,'night.html')

def evening(request):
    return render(request,'evening.html')