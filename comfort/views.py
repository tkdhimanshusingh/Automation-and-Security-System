from django.shortcuts import render

# Create your views here.
def comfort(request):
    return render(request, 'comfort.html')
def led1(request):
    return render(request, 'led1.html')
def led2(request):
    return render(request, 'led2.html')
def fan(request):
    return render(request, 'fan.html')