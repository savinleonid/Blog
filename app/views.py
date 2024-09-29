from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Post


def post_list(request):
    post_list = Post.objects.all().order_by('-created_at')
    posts_per_page = request.GET.get('posts_per_page', 5)  # По умолчанию 5 постов на страницу
    paginator = Paginator(post_list, posts_per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'app/post_list.html', {'page_obj': page_obj, 'posts_per_page': posts_per_page})
