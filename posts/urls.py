from django.urls import path
from .views import (
        PostListView, 
        PostCreateView,
        PostDetailView,
        PostDeleteView,
        PostUpdateView,
        PostArchiveListView,
        PostDraftListView,
)
urlpatterns = [
        path('list/', PostListView.as_view(), name='posts'),
        path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
        path('new/', PostCreateView.as_view(), name="post_new"),
        path('<int:pk>/delete/', PostDeleteView.as_view(), name="post_delete"),
        path('<int:pk>/edit/', PostUpdateView.as_view(), name="post_edit"),
        path('list_archive/', PostArchiveListView.as_view(), name='posts_archive'),
        path('list_draft/', PostDraftListView.as_view(), name='posts_draft'),
]