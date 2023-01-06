from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('add/', views.addBoard_view, name='add_room'),
    path('<int:pk>/', views.room_view, name='room'),
    path('<int:pk>/add/', views.addPin_view, name='add_pin'),

    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
