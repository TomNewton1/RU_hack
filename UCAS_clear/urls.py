from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('homepage', views.homepage, name='homepage'),
    path('userpage', views.userpage, name='userpage'),
    path('course-detail', views.coursedetail, name='course-detail'),
]