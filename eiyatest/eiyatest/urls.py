"""eiyatest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from vehicles.views import VehiclesViewSet, VehicleUpdateLocationAPIView
from vehicles.views_full import retrieveVehicles

schema_view = get_schema_view(
    openapi.Info(
        title="eiya API",
        default_version="v1",
        description="Documentación",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    #api endpoint
    path('vehicles/', VehiclesViewSet.as_view({'get':'list'})),
    path('vehicles/create/', VehiclesViewSet.as_view({'post':'create'})),
    path('vehicles/<int:pk>/', VehiclesViewSet.as_view(
        {
            'get':'retrieve',
            'put':'partial_update',
            'delete':'destroy'
        }
    )),
    path('vehicles/updatecity/', VehicleUpdateLocationAPIView.as_view()),
    
    #templates
    path('vehicles/list/', retrieveVehicles),
    
    #Doc
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
