from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='mainapp/')),
    path('mainapp/', include('mainapp.urls', namespace='mainapp')),
    path('authapp/', include('authapp.urls', namespace='authapp')),
    path("social_auth/", include("social_django.urls", namespace="social")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)