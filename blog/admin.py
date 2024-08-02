from django.contrib import admin
from .models import Post

# Show images of the model in Django Admin
from django.utils.html import format_html

class PostAdmin(admin.ModelAdmin):

    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.image.url))

    def image_tag2(self, obj):
        return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.image2.url))

    list_display = [
        'title', 
        'author', 
        'date_modified', 
        'date_created',
        'body', 
        'body2', 
        'imgname', 
        'imgname2', 
        'image_tag', 
        'image_tag2',
        'slug',
        ]
    prepopulated_fields = {
        'slug' : ['title']
        }

admin.site.register(Post, PostAdmin)











