from django.shortcuts import render

from .models import Post


def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    title = "Лев Толстой – зеркало русской революции."
    text = "Здесь будет информация о группах проекта Yatube"
    context = {
        'title': title,
        'text': text,
    }
    return render(request, template, context)
