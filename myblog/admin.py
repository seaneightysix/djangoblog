from django.contrib import admin
from myblog.models import Genre
from myblog.models import Post

admin.site.register(Genre)
admin.site.register(Post)