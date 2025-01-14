from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls')),
    path('', include('main.urls')),
    path('news/', include('news.urls')),
    path('calculator/', include('calculator.urls')),
    path('docs/', include('docs.urls')),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
