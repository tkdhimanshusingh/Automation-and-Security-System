from django.shortcuts import render

# Create your views here.
def safety(request):
    return render(request, 'safety.html')
def lpg(request):
    return render(request, 'lpg.html')
def temp(request):
    return render(request, 'temp.html')
