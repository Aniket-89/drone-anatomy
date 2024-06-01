from django.db import models
from django.urls import reverse


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    body = models.TextField()
    category = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    banner = models.ImageField(
        upload_to="blogs/banner",
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"
        ordering = ["-pub_date"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            "drone_anatomy.blogs:blog-detail",
            kwargs={
                "pk": self.pk,
            },
        )

    def get_similar_posts(self):
        return Blog.objects.filter()
