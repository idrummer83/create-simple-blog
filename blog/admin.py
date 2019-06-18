from django.contrib import admin
from .models import Post, Author
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass