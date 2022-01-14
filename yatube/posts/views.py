from django.shortcuts import render, get_object_or_404
from .models import Post, Group
from django.http import HttpResponse, HttpRequest

COUNT_OF_POSTS_INDEX = 10
COUNT_OF_POSTS_GROUP = 10


def index(request: HttpRequest) -> HttpResponse:
    template = 'posts/index.html'
    posts = Post.objects.all()[:COUNT_OF_POSTS_INDEX]
    context = {
        'text_h1': 'Последние обновления на сайте.',
        'title': 'Главная страница проекта Yatube',
        'posts': posts
    }
    return render(request, template, context)


def group_posts(request: HttpRequest, slug) -> HttpResponse:
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = (Post.objects.filter(group=group)[:COUNT_OF_POSTS_GROUP])
    title = f'Записи сообщества {group.title}.'
    context = {
        'title': title,
        'text_h1': 'Лев Толстой – зеркало русской революции.',
        'text_p': 'Группа тайных поклонников графа.',
        'group': group,
        'posts': posts,
    }

    return render(request, template, context)
