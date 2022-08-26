from django.urls import path
from posts import views


urlpatterns = [
    path("", views.PostListView.as_view(), name="article_list"),
    path("new/", views.PostCreateView.as_view(), name="article_new"),
    path("<int:pk>/", views.PostDetailView.as_view(), name="article_detail"),
    path("<int:pk>/edit/", views.PostUpdateView.as_view(), name="article_edit"),
    path("<int:pk>/delete/", views.PostDeleteView.as_view(), name="article_delete"),
]
