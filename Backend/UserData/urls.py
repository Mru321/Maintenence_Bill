from django.urls import path
from . import views

urlpatterns=[
    path('', views.table, name='table'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('welcom/<str:username>/', views.welcome, name='welcome'),
    path('logout/', views.logout_view, name='logout')
]