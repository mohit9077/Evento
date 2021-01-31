from django.urls import path

from .import views
urlpatterns = [
    
path('dashboard/',views.hackathons,name="homeadmin"),
path('reg_general/',views.general_reg,name="generalreg_R"),
path('submit_general/',views.general_reg,name="general_reg_P"),
path('update_generalk/<str:pk>',views.update_general,name="update_general"),
path('delete_general/<str:pk>',views.delete_general,name="delete_general"),
path('submit_general/<str:pk>',views.update_general,name="update_genral_post"),
path('studentregistered/<str:title>',views.studentregistered,name="studentregistered"),
]

