from django.shortcuts import render

# Create your views here.
def security(request):
    return render(request, 'security.html')
def cctv(request):
    return render(request, 'cctv.html')
def door(request):
    return render(request, 'door.html')
