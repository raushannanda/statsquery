from tkinter import CASCADE
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
# Create your models here.
# Script validation
def script_injection(value):
    if value.find('<script>') != -1:
        raise ValidationError(_('Script injection in %(value)s'),
                              params={'value': value})

class ExamList(models.Model):
    exam_name = models.CharField(max_length=100,primary_key=True,validators=[script_injection])

    objects = models.Manager()

    def __str__(self):
        return self.exam_name
        

class Year(models.Model):
    year = models.IntegerField(default='',primary_key=True)
    objects = models.Manager()
    def __str__(self):
        return str(self.year)
    

class Solution(models.Model):
    def number():
        no =Solution.objects.count()
        if no == None:
            return 1
        else:
            return no+1
    sno = models.IntegerField(_('S.No.'),unique=True,default=number,primary_key=True)
    exam = models.ForeignKey(ExamList,on_delete=models.CASCADE,validators=[script_injection])

    year = models.ForeignKey(Year,on_delete=models.CASCADE,)
    paper = models.CharField(max_length=1,validators=[script_injection])

    q_no = models.IntegerField()
    question = models.TextField(validators=[script_injection])
    solution = models.TextField(validators=[script_injection])
    last_updated = models.DateField( auto_now=False, auto_now_add=False)
    objects = models.Manager()

    def __str__(self):
        return str(self.sno)
