from rest_framework.authtoken.views import obtain_auth_token
from . import views
from django.urls import path

urlpatterns=[
    path("login/",obtain_auth_token,name="login"),
    path("register",views.registration_view,name='register'),
]