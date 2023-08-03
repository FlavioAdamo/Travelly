from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.urls import (
    path,
    include,
)


urlpatterns = [
    path('admin/', admin.site.urls),

    #authentication
    path('api/auth/', include('authentication.urls')),

    #apps
    path('api/', include('trips.urls')),
    path('api/', include('cities.urls')),
    path('api/', include('hotels.urls')),

    #doumentation
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
