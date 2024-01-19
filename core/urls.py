from django.contrib import admin
from django.urls import path
from main import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
]

url_main = [
    path('', views.home, name='home'),
    path('extract_code/', views.extract_code, name='extract_code'),
    path('download/<str:nome_arquivo>/', views.download, name='download'),
    path('format_json/', views.format_json, name='format_json'),
]

urlpatterns += url_main

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)