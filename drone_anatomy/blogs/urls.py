from django.urls import path

from . import views

app_name = "drone_anatomy.blogs"

urlpatterns = [
    path("", views.blog_list_view, name="blog-list"),
    path("<int:pk>/", views.blog_detail_view, name="blog-detail"),
]
