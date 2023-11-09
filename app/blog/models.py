from django.db import models
from django.utils.timezone import now


class Category(models.Model):
    name = models.CharField(
        max_length=32,
        null=False,
        blank=False,
        unique=True,
        verbose_name="название",
    )
    slug = models.SlugField(
        max_length=32,
        null=False,
        blank=False,
        unique=True,
        verbose_name="URL",
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = "категория"
        verbose_name_plural = "категории"


class Post(models.Model):
    title = models.CharField(
        max_length=128,
        null=False,
        blank=False,
        verbose_name="заголовок"
    )
    descr = models.TextField(
        null=False,
        blank=False,
        verbose_name="описание"
    )
    is_published = models.BooleanField(
        default=False,
        null=False,
        blank=False,
        verbose_name="опубликовано"
    )
    date_created = models.DateTimeField(
        default=now,
        null=False,
        blank=False,
        verbose_name="дата создания"
    )
    slug = models.SlugField(
        max_length=128,
        null=False,
        blank=False,
        unique=True,
        verbose_name="URL"
    )
    category = models.ForeignKey(
        to="Category",
        on_delete=models.PROTECT,
        null=False,
        blank=False,
        db_index=True
    )

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ["category", "title"]
        verbose_name = "пост"
        verbose_name_plural = "посты"
