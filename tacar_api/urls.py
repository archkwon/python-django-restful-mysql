from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api_user.urls')),
    path('', include('api_login.urls')),
    path('', include('api_cust.urls')),
    path('', include('api_order.urls')),
    path('', include('api_location.urls')),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/images/kinpecauto.ico')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

