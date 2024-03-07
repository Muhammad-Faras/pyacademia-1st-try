from django.shortcuts import render,redirect,get_object_or_404
from .models import Post
from .forms import PostCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden,HttpResponseRedirect
from django.urls import reverse
# Create your views here.

@login_required
def create_posts_view(request):
    if request.method == 'POST':
        form = PostCreationForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('feed:feed')
        else:
            # Print form errors for debugging
            print(form.errors)
    else:
        form = PostCreationForm()
    return render(request, 'feed/create_post.html', {'form': form})

    """_summary_
    posts lists function is used in feed -> views.py to show posts on feed app 
    """
@login_required
def update_posts_view(request,id):
    context = {}
    post_to_update = get_object_or_404(Post, pk=id, author = request.user)
    
    if request.method == 'POST':
        form = PostCreationForm(request.POST, instance=post_to_update)
        if form.is_valid():
            form.save()
            return redirect('feed:feed')
        else:
            form = PostCreationForm(instance=post_to_update)
    else:
        form = PostCreationForm(instance=post_to_update)
         
    
    context['form'] = form
    context['post_to_update'] = post_to_update
    
    return render(request, 'feed/update_post.html',context)
@login_required
def detail_posts_view(request, id):
    context={}
    post_to_update = get_object_or_404(Post, pk=id)
    context['post_to_update'] = post_to_update
    
    return render(request, 'feed/post_detail.html', context)
@login_required
def delete_posts_view(request,id):
    post_delete = get_object_or_404(Post, pk=id, author=request.user)
    post_delete.delete()
    
    return redirect('feed:feed')


@login_required
def my_postsview(request):
    context = {}
    my_posts = Post.objects.filter(author=request.user)
    context['my_posts'] = my_posts
    return render(request, 'feed/my_posts.html', context)


@login_required
def post_category_view(request,cats):
    context = {}
    post_categories = Post.objects.filter(category=cats)
    context['cats'] = cats
    context['post_categories'] = post_categories
    return render(request, 'feed/posts_category.html', context)    


def post_like_view(request, id):
    post = get_object_or_404(Post, id=id)
    
    # Check if the current user has already liked the post
    if request.user in post.likes.all():
        # If the user has already liked the post, remove the like
        post.likes.remove(request.user)
        print('likes...', post.likes.count())
        
    else:
        # If the user hasn't liked the post, add the like
        post.likes.add(request.user)
        print('likes...', post.likes.count())
    post.save()
    
    return redirect('feed:feed')