from django.urls import path

from . import views

urlpatterns = [
path('login_user/', views.login_u,name="user"),
path('login_admin/', views.login_a,name="admin"),
path('pass_check_user/',views.pass_check_user,name="l_user"),
path('pass_check_admin/',views.pass_check_admin,name="l_adm"),
path('user_profile/',views.user_profile,name="user_profile"),
path('eventreg/<str:pk>',views.eventreg,name="eventreg"),


]