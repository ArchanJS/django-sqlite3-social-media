from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    path("", views.homeFunc,name="home"),
    path("login", views.loginFunc,name="login"),
    path("logout", views.logoutFunc,name="logout"),
    path("signup", views.signupFunc,name="signup"),
    path("createpost",views.createPost,name="createpost"),
    path("edit/<str:postTitle>",views.editPost,name="editpost"),
    path("update/<str:postTitle>",views.updatePost,name="updatepost"),
    path("delete/<str:postTitle>",views.deletePost,name="deletepost")
]