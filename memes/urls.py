from django.urls import path
from .views import MemeListView, MemeUploadView
from .views import like_meme, dislike_meme
urlpatterns = [
    path('memes/', MemeListView.as_view(), name='meme_list'),
    path('upload/', MemeUploadView.as_view(), name='meme_upload'),
    path('like/<int:meme_id>/', like_meme, name='like_meme'),
    path('dislike/<int:meme_id>/', dislike_meme, name='dislike_meme'),

]
