from django.contrib import admin
from .models import Solution,ExamList,Year
# Register your models here.
class YearAdmin(admin.ModelAdmin):
    list_display = ('year',)

class SolutionAdmin(admin.ModelAdmin):
    list_display = ('sno','exam','year','paper','q_no',)
admin.site.register(Solution,SolutionAdmin)
admin.site.register(ExamList)
admin.site.register(Year,YearAdmin)
