from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='signup'),
    path('login' , views.login , name="login" ),
    path('forgotPassword' , views.reset_password , name="resetPassword" ),
    path('userprofile' , views.profile , name="userprofile" ),
    path('profile_admin',views.profile_admin,name="profile_admin"),
    path('profile',views.profile,name="profile"),
]