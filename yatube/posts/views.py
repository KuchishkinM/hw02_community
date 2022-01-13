from django.shortcuts import render, get_object_or_404
from .models import Post, Group
from django.http import HttpResponse, HttpRequest


def index(request: HttpRequest) -> HttpResponse:
    template = 'posts/index.html'
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'text': 'Последние обновления на сайте.',
        'title': 'Главная страница проекта Yatube',
        'posts': posts
    }
    return render(request, template, context)


def group_posts(request: HttpRequest, slug) -> HttpResponse:
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    text = f'Записи сообщества {group}.'
    context = {
        'text': text,
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
