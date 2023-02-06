from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Meme

class MemeListView(ListView):
    model = Meme
    template_name = 'memes/meme_list.html'
    context_object_name = 'memes'
    ordering = ['-likes', '-created_at']

class MemeUploadView(CreateView):
    model = Meme
    template_name = 'memes/meme_form.html'
    fields = ['title', 'content', 'photo']
    success_url = '/memes/'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(self, form)


from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

@login_required
def like_meme(request, meme_id):
    meme = get_object_or_404(Meme, id=meme_id)
    meme.likes += 1
    meme.save()
    return JsonResponse({'likes': meme.likes})

@login_required
def dislike_meme(request, meme_id):
    meme = get_object_or_404(Meme, id=meme_id)
    meme.dislikes += 1
    meme.save()
    return JsonResponse({'dislikes': meme.dislikes})
