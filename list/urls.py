from django.urls import path
from django.urls.resolvers import URLPattern 
from . import views

urlpatterns= [
    path("",views.index , name="home"),
    path("login/",views.view_login, name="login"),
    path("save_content",views.save_content , name="save_content"),
    path("edit_content/<str:pk>",views.edit_content,name ="edit_content"),
    path("done_todo/<str:pk>",views.done_todo,name ="done_todo"),
    path("delete_todo/<str:pk>",views.delete_todo,name ="delete_todo"),
    path("register/",views.view_register , name="register"),
    path("logout",views.view_logout , name="logout"),
]