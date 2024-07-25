from django.contrib import admin
from django.urls import path, include

from django.conf import settings 
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path('users/', include('users.urls')),
    path("", include("blog.urls")),
    path("", include("contact.urls")),
    path("", include("mainapp.urls")),
     
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Django Admin Setting
admin.site.site_header = 'JournPy Administration'
admin.site.index_title = 'Admin Dashboard'