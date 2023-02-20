from django.contrib import admin
from .models import *

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'num', 'photo', 'time_create', 'is_published')
    list_display_links = ('num',)
    search_fields = ('num',)
    list_editable = ('is_published',)
    list_filter = ('time_create', 'is_published')

admin.site.register(Post, PostAdmin)
admin.site.register(IpModel)
