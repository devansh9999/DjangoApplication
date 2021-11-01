from django.urls import path
from Java import views
urlpatterns=[
    path("Questions/Notes",views.NotesView.as_view(),name="NotesView"),
    path("Questions/", views.Questions.as_view(), name="Questions"),
    path("AddData/", views.ADD_DATA.as_view(),name="AddData"),
    path("logout/", views.logout.as_view(),name="Logout"),
    path("Notes/",views.Notes.as_view(),name="Notes"),
    
    # path("Login/", views.Login.as_view(), name="Login")
]