from django.urls import path
from .import views

app_name = "mainApp"

urlpatterns = [
    path("", views.mainView.as_view(),name='mainpage'),
    path("/<int:pk>/", views.TeacherView.as_view()),
    path("login/",views.login_view,name='login'),
    path("signup/", views.signup, name='signup'),
    path("logout/",views.logout,name='logout'),
    path("lan/", views.TeachableUserView.as_view()),
]