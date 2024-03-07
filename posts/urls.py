from django.urls import path
from .views import (
    create_posts_view,
    detail_posts_view,
    update_posts_view,
    delete_posts_view,
    my_postsview,
    post_category_view,
    post_like_view,
)

app_name = 'posts'

urlpatterns = [
    path('create/', create_posts_view, name='create_posts'),
    path('update/<int:id>/', update_posts_view, name='update_post'),
    path('detail/<int:id>', detail_posts_view, name='detail_post'),
    path('delete/<int:id>', delete_posts_view, name='delete_post'),
    path('my-posts/', my_postsview, name='my_posts'),
    path('category/<str:cats>/', post_category_view, name='post_category'),
    path('post_like/<int:id>',post_like_view, name='post_like'),
] 