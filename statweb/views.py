
from django.shortcuts import render,redirect 
from vlog.models import Post

from .forms import SubscribeForm
from .forms import ContactForm
from vlog.models import SubEmail
from vlog.models import Contact



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
    fm = ContactForm()
    ctx = {'form':fm}
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            e = Contact()
            e.email = form.cleaned_data['email']
            e.message = form.cleaned_data['message']
            e.save()
            return render(request,'home/thanks.html')
    else:    
        return render(request,'home/contact.html',ctx)

def about(request):
   return render(request,'home/about.html')