from django.urls import path

from blog.apps import BlogConfig
from blog.views import (
    BlogCreateView,
    BlogDeleteView,
    BlogDetailView,
    BlogListView,
    BlogUpdateView,
)

app_name = BlogConfig.name

urlpatterns = [
    path("", BlogListView.as_view(), name="blog_list"),
    path("new/", BlogCreateView.as_view(), name="blog_create"),
    path("<int:pk>/update", BlogUpdateView.as_view(), name="blog_update"),
    path("<int:pk>/detail", BlogDetailView.as_view(), name="blog_detail"),
    path("<int:pk>/delete", BlogDeleteView.as_view(), name="blog_delete"),
]
