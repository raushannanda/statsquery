
from django.shortcuts import render,redirect
from vlog.models import Post

from .forms import SubscribeForm
from vlog.models import SubEmail


def home(request):
    fm = SubscribeForm()
    posts = Post.objects.all()[:5]
    ctx={'posts':posts,'form':fm}
    if request.method == "POST":
        form = SubscribeForm(request.POST)
        if form.is_valid():
            e = SubEmail()
            e.email = form.cleaned_data['email']
            e.save()
            return redirect(home)
    else:   
        return render(request,'home/index.html',ctx)

def privacy(request):
    return render(request,'home/privacy.html')

def terms(request):
    return render(request,'home/terms.html')

def contact(request):
    return render(request,'home/contact.html')

def about(request):
    return render(request,'home/about.html')