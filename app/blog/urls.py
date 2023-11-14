from django.urls import path

from .views import CategoryListView, CategoryDetailView, PostListView, PostDetailView

urlpatterns = [
    path("", CategoryListView.as_view()),
    path("<slug:slug>/", PostListView.as_view()),
    path("<slug:category_slug>/<slug:post_slug>/", PostDetailView.as_view()),
]
