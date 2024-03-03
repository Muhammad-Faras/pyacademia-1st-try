from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from posts.models import Post
# Create your views here.

@login_required
def feedview(request):
    context = {}
    list_posts = Post.objects.all()
    context['list_posts'] = list_posts
    return render(request, 'feed/feed.html', context)