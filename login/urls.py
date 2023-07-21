from django.urls import path
from .views import login_form,logout_view

urlpatterns = [
    path('',login_form,name="login form"),
    path('logout/',logout_view,name="logout form")
]

