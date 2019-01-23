from django.contrib import admin

# Register your models here.
from blogs.models import BlogPost

admin.site.register(BlogPost)
