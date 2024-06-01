from django.db import models
from django.urls import reverse


class Service(models.Model):
    name = models.CharField(max_length=225)
    description = models.TextField()
    image = models.ImageField(upload_to="core/img/services", default="img/default.png")

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            "drone_anatomy.core:service-detail",
            kwargs={
                "pk": self.pk,
            },
        )


class Partner(models.Model):
    name = models.CharField(max_length=225)
    logo = models.ImageField(upload_to="core/img/partners")

    class Meta:
        verbose_name = "Partner"
        verbose_name_plural = "Partners"

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=225)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name}: {self.email}"


class Newsletter(models.Model):
    subscribed_email = models.EmailField()

    def __str__(self):
        return self.subscribed_email


class Member(models.Model):
    name = models.CharField(max_length=155)
    position = models.CharField(max_length=155)
    image = models.ImageField(upload_to="core/img/members")
    brief = models.TextField(null=True, blank=True)
    linkedin = models.URLField()
    instagram = models.URLField()
    twitter = models.URLField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            "drone_anatomy.core:member-detail",
            kwargs={
                "pk": self.pk,
            },
        )
