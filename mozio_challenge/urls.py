from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="API Documentation",
      default_version='v1',
      description="API Documentation Mozio Challenge",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="filipe.almeida@dcomp.ufs.br"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/token/', obtain_auth_token, name='token'),
    path('api/doc/', schema_view.with_ui('swagger', cache_timeout=0), name='doc'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
