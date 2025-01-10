from django.contrib import admin
from .models import Post
# Register your models here. import Post and register so the admin GUI we can see the post data

admin.site.register(Post)



