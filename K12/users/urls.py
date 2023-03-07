from django.urls import path
import django.contrib.auth.views as vs
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.test, name='test'),
    path('logout/',
         vs.LogoutView.as_view(template_name='users/logged_out.html'),
         name='logout'
         ),
    path('signup/', views.SignUp.as_view(), name='signup'),
]