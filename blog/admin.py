from django.contrib import admin
from .models import Post

# Show images of the model in Django Admin
from django.utils.html import format_html


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):


    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.image.url))


    list_display = [
        'title',
        'author',
        'date_modified',
        'date_created',
        'body',
        'image_name',
        'image_tag',
        'slug',
        ]
    prepopulated_fields = {
        'slug' : ['title']
        }












