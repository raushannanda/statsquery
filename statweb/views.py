
from django.shortcuts import render
from vlog.models import Post
def home(request):
    posts = Post.objects.all()[:5]
    ctx={'posts':posts}
    return render(request,'home/index.html',ctx)

def privacy(request):
    return render(request,'home/privacy.html')

def terms(request):
    return render(request,'home/terms.html')

def contact(request):
    return render(request,'home/contact.html')

def about(request):
    return render(request,'home/about.html')