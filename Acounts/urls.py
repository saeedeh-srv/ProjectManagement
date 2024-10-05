from django.urls import path
from .views import LoginUser, ProfileUser, RegisterUser,LogoutUser,ChangePassword,UpdateProfile

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginUser.as_view(), name='user_login'),
    path('profile/', ProfileUser.as_view(), name='user_profile'),
    path('register/', RegisterUser.as_view(), name='user_register'),
    path('logout/', LogoutUser.as_view(), name='user_logout'),
    path('change/password/', ChangePassword.as_view(), name='user_change_password'),
    path('update/profile/', UpdateProfile.as_view(), name='update_profile'),


]
