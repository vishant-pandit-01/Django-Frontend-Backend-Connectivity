from django.shortcuts import render
from chats.models import*

# Create your views here.
def indexpage(request):
    x  =record.objects.all()
    return render(request,"index.html",{'x': x})


