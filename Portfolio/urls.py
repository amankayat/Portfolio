
from django.contrib import admin
from django.urls import path,include,re_path as url
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from django.conf import settings
from django.views.static import serve
urlpatterns = [
     url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),

    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
]
urlpatterns+=staticfiles_urlpatterns()
urlpatterns+=static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)