from ast import NotEq
from operator import eq
from django.shortcuts import render
from numpy import not_equal
from .models import Solution
from .models import ExamList
from .models import Year
# Create your views here.
def Solutions(request):
    exams = ExamList.objects.all()
    
    ctx = {'exams':exams}
    return render(request,'solution/index.html',ctx)

def Solutionyears(request,examname):
    if request.GET.get('exam') != None:
        year = request.GET.get('year')
        paper = request.GET.get('exam')
        solutions = Solution.objects.filter(exam=examname,year=year,paper=paper).order_by('q_no')
        
        ctx = {'solutions':solutions}
        return render(request,'solution/solved.html',ctx)
    elif request.GET.get('exam') == None and request.GET.get('year') != None:
            year = request.GET.get('year')
            solutions = Solution.objects.filter(exam=examname,year=year).order_by('q_no')
            ctx = {'solutions':solutions}
            return render(request,'solution/solved.html',ctx)
    else:
        years = Year.objects.all()
        ctx = {"years":years,"examname":examname}
        return render(request,'solution/years.html',ctx)