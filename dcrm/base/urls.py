from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('', views.login_page, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path('register/', views.register_user, name="register"),
    path('record/<str:pk>/', views.cust_rec, name="record"),
    path('delete/<str:pk>/', views.delete_cust, name="delete"),
    path('add_record/', views.add_record, name="add_record"),
    path('update_record/<str:pk>/', views.update_record, name="update_record"),
    
]
