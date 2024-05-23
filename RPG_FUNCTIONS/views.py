from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)

from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import GamePostForm
from .models import GamePost, GameUser


# Create your views here.


class GamePostList(ListView):
    model = GamePost
    template_name ='Gameposts.html'
    context_object_name = 'GamePosts'


class GamePostDetail(DetailView):
    model = GamePost
    template_name = 'Post_Detail.html'
    context_object_name = "post"


class GamePostUpdate(LoginRequiredMixin, UpdateView):
    form_class = GamePostForm
    model = GamePost
    template_name = 'GamePost_Create.html'
    success_url = reverse_lazy('All_Posts')

class GamePostCreate(LoginRequiredMixin, CreateView):
    model = GamePost
    form_class = GamePostForm
    template_name = 'GamePost_Create.html'
    success_url = reverse_lazy('All_Posts')

    def form_valid(self, form):
        post = form.save(commit=False)
        GameUser.objects.get_or_create(user_link=self.request.user)
        post.link_GameUser = self.request.user.gameuser
        post.save()
        return super().form_valid(form)






