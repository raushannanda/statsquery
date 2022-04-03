from django.shortcuts import render
from .models import Solution
# Create your views here.
def Solution(request):
    return render(request,'solution/index.html')