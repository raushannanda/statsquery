from pickle import TRUE
from django.contrib import admin
from .models import Post,PostCategory
from django.template.defaultfilters import truncatechars
# Register your models here.

def short_post(self):
        return truncatechars(self.post, 35)

class PostCategoryAdmin(admin.ModelAdmin):
    list_display=('sno','name',)
    # list_editable = ('description',)
    # list_per_page = 5
    # search_fields = ('title',)
    # list_filter = ('title',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','post','created',short_post)
    list_filter = ('title','created',)
admin.site.register(PostCategory,PostCategoryAdmin)
admin.site.register(Post,PostAdmin)


