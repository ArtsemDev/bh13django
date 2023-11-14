from django.contrib import admin

from .models import Category, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    list_editable = ("slug", )
    prepopulated_fields = {
        "slug": ("name", )
    }


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "is_published")
    list_filter = ("category", "is_published")
    date_hierarchy = "date_created"
    list_editable = ("category", "is_published")
    search_fields = ("title", "descr")
    search_help_text = "Заголовок или описание"
    prepopulated_fields = {
        "slug": ("title", "category")
    }
