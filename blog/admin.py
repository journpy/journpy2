from django.contrib import admin
from .models import Post

# Show images of the model in Django Admin
from django.utils.html import format_html

class ImageAdmin(admin.ModelAdmin):

    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.image.url))

    def image_tag2(self, obj):
        return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.image2.url))

    list_display = [
        'title', 
        'author', 
        'date_added', 
        'body', 
        'body2', 
        'imgname', 
        'imgname2', 
        'image_tag', 
        'image_tag2',
        ]
admin.site.register(Post, ImageAdmin)











