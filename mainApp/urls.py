from django.urls import path
from .import views

app_name = "mainApp"

urlpatterns = [
    path("", views.mainView.as_view()),
    path("login/",views.login),
    path("logout/",views.logout),
    path("lan/", views.TeachableUserView.as_view()),
    path('<int:pk>/', views.TeacherView.as_view()),
]