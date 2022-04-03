from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
# Create your models here.
# Script validation
def script_injection(value):
    if value.find('<script>') != -1:
        raise ValidationError(_('Script injection in %(value)s'),
                              params={'value': value})

class PostCategory(models.Model):
    def number():
        no =PostCategory.objects.count()
        if no == None:
            return 1
        else:
            return no+1
    sno = models.IntegerField(_('sno'),unique=True,default=number)
    name = models.CharField(max_length=50,unique=True,null=False,primary_key=True,validators=[script_injection,])

    description = models.TextField(validators=[script_injection,])

    objects = models.Manager()

    def __str__(self):
        return self.name



class Post(models.Model):
    def number():
        no =Post.objects.count()
        if no == None:
            return 1 
        else:
            return no+1
    sno = models.IntegerField(_('sno'),unique=True,default=number)
    title = models.CharField(max_length=300,primary_key=True,validators=[script_injection,])

    category = models.ForeignKey(PostCategory,on_delete=models.SET_NULL,null=True)
    author = models.CharField(max_length=50,validators=[script_injection,])

    post = models.TextField(validators=[script_injection])
    created = models.DateField( auto_now=False, auto_now_add=False)
    last_updated = models.DateField( auto_now=False, auto_now_add=False)

    objects = models.Manager()


