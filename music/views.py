from django.shortcuts import render
from .models import Blog
# Create your views here.
def home(request):
    blog = Blog.objects.all()

    return render(request,'home.html',{'blog':blog})

def detail(request,id):
    blog = Blog.objects.get(id=id)

    return render(request,'detail.html',{'blog':blog})
