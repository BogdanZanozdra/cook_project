
from django.urls import path
from .views import logout_view
from django.contrib.auth import views as auth_views


app_name = 'users_app'

urlpatterns = [
    path('login', auth_views.LoginView.as_view(), name='login'),
    # path('logout', auth_views.auth_logout, name='logout'),
    # path('logout/', auth_views.LogoutView.as_view(), name='home'),
    path('logout', logout_view, name='logout_view')


]

