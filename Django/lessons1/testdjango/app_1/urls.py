from django.urls import include, path
from . import views

urlpatterns = [
    path('1', views.url1),
    path('1', views.url2)
]