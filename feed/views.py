from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from posts.models import Post,Category
# Create your views here.

@login_required
def feedview(request):
    context = {}
    list_posts = Post.objects.all()
    category_item = Category.objects.all()
    context['list_posts'] = list_posts
    context['category_item'] = category_item
    current_user = request.user
    context['current_user'] = current_user
    
    return render(request, 'feed/feed.html', context)