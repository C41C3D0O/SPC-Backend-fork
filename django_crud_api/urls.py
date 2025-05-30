"""
URL configuration for django_crud_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.urls import re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls.static import static

schema_view = get_schema_view(
   openapi.Info(
      title="Documentacion proyecto SPC",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="santi2080@hotmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Rutas de las apps de autenticación y registro de usuarios
    path('registro_usuarios/', include('registro_usuarios.urls')),
    path('api/', include('autenticacion.urls')),
    path('proyecciones/', include('proyecciones.urls')),
    path('api/', include('uploads.urls')),
    path('api/', include('proyecciones.urls')),

    # Rutas de las proyecciones
    path('proyeccion/', include('proyecciones.urls')),
    path('comportamiento/', include('proyecciones.urls')),
    path('cursos/', include('proyecciones.urls')),
    
    # Rutas para la documentación de la API
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redocs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
] 


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)