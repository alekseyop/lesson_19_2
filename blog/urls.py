from django.urls import path

from blog.apps import BlogConfig

from blog.views import (
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView, BlogListViewAll
)

app_name = BlogConfig.name

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('listAll/', BlogListViewAll.as_view(), name='blog_list_all'),
    path('<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('list/', BlogListView.as_view(), name='blog_list'),
    path('<int:pk>/update/', BlogUpdateView.as_view(), name='blog_update'),
    path('<int:pk>/delete/', BlogDeleteView.as_view(), name='blog_delete'),
    path('blog/create', BlogCreateView.as_view(), name='blog_create')
    ]