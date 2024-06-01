from django.urls import path

from . import views

app_name = "drone_anatomy.core"

urlpatterns = [
    path("", views.home_view, name="home"),
    path("services/", views.service_list_view, name="service-list"),
    path("services/<int:pk>", views.service_detail_view, name="service-detail"),
    path("contact/", views.contact_form_view, name="contact"),
    path("about/", views.about_us_view, name="about"),
    path("team/<int:pk>", views.member_detail_view, name="member-detail"),
    path("journey", views.journey_view, name="journey"),
    path("whatsapp/", views.whatsapp_redirect, name="whatsapp-redirect"),
    # path("subscribe/", views.newsletter_subscribe, name="newsletter-subscribe")
]
