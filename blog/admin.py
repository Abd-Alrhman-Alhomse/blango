from django.contrib import admin
from .models import Tag, Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("title",)}
  list_display = ('summary', 'content')

admin.site.register(Tag)
admin.site.register(Post, PostAdmin)



