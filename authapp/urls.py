from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('signup',views.signup,name='signup'),
    path('login1',views.login1,name='login1'),
    path('about',views.about,name='about'),
    path('usercreate',views.usercreate,name='usercreate'),
    path('loginauth',views.loginauth,name='loginauth'),
    path('logout',views.logout,name='logout'),
    path('adminhome',views.adminhome,name='adminhome'),
]