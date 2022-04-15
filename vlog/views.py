import errno
from unicodedata import name
from django.shortcuts import render
from vlog.models import PostCategory,Post
from solution.models import ExamList,Solution
from  bson import ObjectId
# Create your views here.
import numpy as np
def Vlog(request):
    examlist = ExamList.objects.all()
    posts = Post.objects.all()[:6]
    postcategory = PostCategory.objects.all()
    ctx = {'postcategory':postcategory,'exams':examlist,'posts':posts}
    return render(request,'blog/index.html',ctx)

def Vloglink(request,slug):
    posts = Post.objects.all()[:6]
    examlist = ExamList.objects.all()
    postcategory = PostCategory.objects.all()
    try:
        ques = PostCategory.objects.get(sno=slug)
        ctx = ctx = {'postcategory':postcategory,'exams':examlist,'posts':posts,'query':ques}
        return render(request,'blog/blogId.html',ctx)
    except PostCategory.DoesNotExist:
        return render(request,'blog/blogwithid.html',{'query':'Nothing to show','active':0,})

def Posts(request,postid):
    allposts = Post.objects.all()[:6]
    post = Post.objects.get(sno = postid)
    catindex = PostCategory.objects.get(name=post.category)
    exl = ExamList.objects.all()
    return render(request,'blog/post.html',{'post':post,'exams':exl,'catindex':catindex.sno,'allposts':allposts})