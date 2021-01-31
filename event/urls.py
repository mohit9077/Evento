from django.urls import path

from . import views
urlpatterns = [
   path('', views.home,name="home"),
   path('about/', views.about,name="about"),
   
    path('hack/', views.hackathons,name="hackathon"),
    path('college/', views.college,name="college"),
    path('news/', views.news,name="news"),
    path('quiz/', views.quizzes,name="quiz"),
    path('workshop/', views.workshops,name="workshop"),
    path('comp/', views.competition,name="comp"),
     path('blog/', views.blog_detail,name="blog"),
     path('logout/', views.logout,name="logout"),
      path('logout_admin/', views.logout_admin,name="logout_admin"),
    
]