from django.contrib import admin
from django.urls import path, include
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Blog API",
      default_version='v1',
      description="This documentation list structures all parents endpoints of the api",
      terms_of_service="danquahwilliam89@gmail.com",
      contact=openapi.Contact(email="danquahwilliam89@gmail.com"),
      license=openapi.License(name="William Dreams!"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("user/", include("usersapp.urls")),
    path("blog/", include("blogapp.urls")),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

]
