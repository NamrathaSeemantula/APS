from django.contrib import admin
from .models import blogs, blogcomments

# Register your models here.

admin.site.register(blogs)
admin.site.register(blogcomments)