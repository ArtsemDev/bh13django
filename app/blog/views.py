from django.views.generic import ListView, DetailView
from django.http import Http404

from .models import Category, Post


# @require_GET()
# def index(request):
#     objs = Category.objects.all().order_by("name")
#     return render(
#         request=request,
#         template_name="blog/index.html",
#         context={
#             "categories": objs
#         }
#     )


class CategoryListView(ListView):
    template_name = "blog/index.html"
    model = Category
    queryset = Category.objects.order_by("name")
    context_object_name = "categories"


class CategoryDetailView(DetailView):
    model = Category
    template_name = "blog/category_detail.html"
    context_object_name = "category"


class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    queryset = model.objects.filter(is_published=True)

    def get_queryset(self):
        return self.queryset.filter(category__slug=self.request.path_info.split("/")[-2])


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    slug_url_kwarg = "post_slug"
    queryset = model.objects.filter(is_published=True)
    context_object_name = "post"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category__slug=self.request.path_info.split("/")[-3])
        queryset = queryset.select_related("category")
        if not queryset:
            raise Http404()
        return queryset
