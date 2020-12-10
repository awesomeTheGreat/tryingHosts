from django.db import models
from django.utils.text import slugify


class Category(models.Model):

    name = models.CharField(max_length=50)
    slug = models.SlugField(blank=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def save(self, *args, **kwargs):

        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Question(models.Model):

    question = models.CharField(max_length=100)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.question
