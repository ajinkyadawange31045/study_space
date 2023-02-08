from django.urls import path
from . import views

urlpatterns = [
    path("discussion-forum", views.forum, name="Forum"),
    path("discussion/<int:myid>/", views.discussion, name="Discussions"),
    # path("register/", views.UserRegister, name="Register"),
    # path("login/", views.UserLogin, name="Login"),
    # path("logout/", views.UserLogout, name="Logout"),
    # path("myprofile/", views.myprofile, name="Myprofile"),
]
