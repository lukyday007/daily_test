from django.urls import path 
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('password_change/', views.password_change, name='password_change'),
    path('update_userinfo/', views.update_userinfo, name='update_userinfo'),
    path('cancel/', views.cancel, name='cancel'),
    
]