from django.urls import path
from auth import views
urlpatterns=[
    path('Login/',views.Login.as_view(),name="Login"),
    path("", views.Home,name="Home"),
]