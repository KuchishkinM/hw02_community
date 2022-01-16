from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, get_object_or_404

from .models import Post, Group

COUNT_OF_POSTS = 10


def index(request: HttpRequest) -> HttpResponse:
    template = 'posts/index.html'
    posts = Post.objects.select_related('group')[:COUNT_OF_POSTS]
    context = {
        'text_h1': 'Последние обновления на сайте.',
        'title': 'Главная страница проекта Yatube',
        'posts': posts
    }
    return render(request, template, context)


def group_posts(request: HttpRequest, slug) -> HttpResponse:
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = (Post.objects.select_related('group', 'author')
                 .filter(group=group)[:COUNT_OF_POSTS])
    title = f'Записи сообщества {group.title}.'
    context = {
        'title': title,
        'text_h1': f'Посты группы {group.title}',
        'text_p': f'Группа тайных поклонников графа - {group.title}.',
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
