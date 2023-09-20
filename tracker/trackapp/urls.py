from django.urls import path , include 
from . import views 

urlpatterns = [
    path("", views.index , name='index'),
    path("create", views.create , name="create"),
    path('piechart/', views.pie_chart, name='pie_chart'),
    # path('adminpage', views.adminpage , name='adminpage'),
    path('login/', views.custom_login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('data/', views.data_display, name='data_display'),
    path('piechart/', views.pie_chart, name='pie_chart'),

]


