from django.urls import path, include
from .views import user_login, user_logout, signup_view, user_profile, editUserInfo

urlpatterns = [
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('signup/', signup_view, name='signup'),
    path('userprofile/', user_profile, name='userprofile'),
    path('editUserInfo/', editUserInfo, name='editUserInfo'),

    path('', include('django.contrib.auth.urls')),

]
