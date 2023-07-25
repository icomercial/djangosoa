# This file is used to map the URL to the view function
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views


app_name = "polls"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    #path("signup/", views.signup, name="signup"),
    path("login/", auth_views.LoginView.as_view(template_name='registration/login.html'), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    #path("register/", views.register, name="register"),
    #path("profile/", views.profile, name="profile"),
    #path("profile/edit/", views.edit_profile, name="edit_profile"),
    #path("profile/change-password/", views.change_password, name="change_password"),
    #path("profile/delete/", views.delete_profile, name="delete_profile"),
    #path("profile/<int:pk>/", views.profile_detail, name="profile_detail"),
    path("restricted/", views.RestrictedView.as_view(), name="restricted"),
]