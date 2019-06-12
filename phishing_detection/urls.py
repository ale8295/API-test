from django.urls import path, include
from . import views
from rest_framework import routers
from django.conf.urls import url

router = routers.DefaultRouter()


urlpatterns = [
    path('',include(router.urls)),
    url(r'prueba/',views.prueba.as_view(),name="prueba")
]