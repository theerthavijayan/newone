from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup, name="signup"),
    path('home', views.home, name="home"),
    path('login',views.login, name="login"),
    path('logout',views.logout, name="logout"),
    path('subscribe', views.subscribe, name = 'index'),
]



#ujcniieuoiuladjq