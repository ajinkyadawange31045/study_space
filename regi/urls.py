# from django.urls import path
# from .views import edit_profile

# urlpatterns = [
    # path('edit_profile/<int:pk>', edit_profile, name='edit_profile'),
    
# ]



from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from regi.views import user_signup, user_login, user_logout,user_change_pass,user_profile,edit_profile


urlpatterns = [
    path('signup/',user_signup,name='signup'),
    path('login/',user_login,name='login'),
    path('logout/',user_logout,name='logout'),
    path('profile/', user_profile, name="profile"),
    path('user_change_pass/', user_change_pass, name="change_pass"),
    path('edit_profile/<int:pk>', edit_profile, name='edit_profile'),
]