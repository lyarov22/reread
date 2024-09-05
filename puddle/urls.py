from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from django.views.generic.base import RedirectView

urlpatterns = [
    path('favicon.ico/', RedirectView.as_view(url='/static/img/reread-logo.ico', permanent=True), name='favicon'),
    path('i18n/', include('django.conf.urls.i18n')),
    path('rosetta/', include('rosetta.urls')),
    
    path('', include('core.urls')),
    path('', include('item.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('inbox/', include('conversation.urls')),
    path('admin/', admin.site.urls),

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
