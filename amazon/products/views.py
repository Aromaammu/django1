from django.shortcuts import render
from django.http import HttpResponse
from.models import Items

# Create your views here.
def index(request):
    x=Items.objects.all()
    return render(request,'index.html',{'x':x})

def about(request):
    return HttpResponse("<h1>ABOUT </h1>")
