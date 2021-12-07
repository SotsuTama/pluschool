from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('data_test', views.data_test, name='data_test'),
    path('carender_manage', views.carender_manage, name='carender_manage'),
]