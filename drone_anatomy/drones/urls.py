from django.urls import path

from . import views

app_name = "drone_anatomy.drones"

urlpatterns = [
    path("", views.drone_list_view, name="drone-list"),
    path("<int:pk>/", views.drone_detail_view, name="drone-detail"),
]
