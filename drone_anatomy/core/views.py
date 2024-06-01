import urllib.parse

from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.cache import cache_control

from drone_anatomy.blogs.models import Blog
from drone_anatomy.drones.models import Drone

from .forms import ContactForm
from .models import Contact
from .models import Member
from .models import Partner
from .models import Service


@cache_control(max_age=31536000)
def home_view(request):
    """
    Renders the home page view.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered home page HTML response.

    Raises:
        Exception: If an error occurs while retrieving the drones, services, or partners, a 500 error page is rendered.
    """
    try:
        drones = Drone.objects.all()
        services = Service.objects.all()
        partners = Partner.objects.all()
        blogs = Blog.objects.all()[:2]
        context = {
            "page": "Drone Anatomy | Home",
            "drones": drones,
            "services": services,
            "partners": partners,
            "blogs": blogs,
        }
        return render(request, "core/home.html", context)
    except Exception:
        return render(request, "500.html")


def team_view(request):
    pass


def about_us_view(request):
    members = Member.objects.all()

    context = {"page": "About Us", "members": members}
    return render(request, "core/about.html", context)


def member_detail_view(request, pk):
    member = Member.objects.get(pk=pk)

    context = {"member": member}
    return render(request, "core/member-detail.html", context)


def service_list_view(request):
    """
    Renders the service list view.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered service list HTML response.

    Raises:
        Exception: If an error occurs while retrieving the services, a 500 error page is rendered.
    """
    try:
        services = Service.objects.all()
        drones = Drone.objects.all()[:3]

        context = {"services": services, "page": "Services", "drones": drones}
        return render(request, "core/service-list.html", context)
    except Exception:
        return render(request, "500.html")


def service_detail_view(request, pk):
    """
    Retrieves a specific service based on the provided primary key.

    Parameters:
        request (HttpRequest): The HTTP request object.
        pk (int): The primary key of the service to retrieve.

    Returns:
        HttpResponse: The rendered service detail HTML response.

    Raises:
        DoesNotExist: If the service with the provided primary key does not exist, a 404 error page is rendered.
    """
    try:
        service = Service.objects.get(pk=pk)
    except Service.DoesNotExist:
        return render(request, "404.html")

    context = {"service": service, "page": f"services | {service.name}"}
    return render(request, "core/service-detail.html", context)


def contact_form_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            try:
                Contact.objects.create(name=name, email=email, message=message)
                return redirect("thank_you_page")  # Redirect to a thank you page
            except Exception as e:
                print("Error saving message:", str(e))

    else:
        form = ContactForm()
    return render(request, "core/contact.html", {"form": form, "page": "Contact Us"})


# def newsletter_subscribe(request):
#     if request.method == "POST":
#         form = NewsletterForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data('email')
#             Newsletter.objects.create(subscribed_email=email)
#             if request.is_ajax():
#                 return JsonResponse({'message': 'Thank you for subscribing to our newsletter!'})
#     else:
#         form = NewsletterForm()
#     return render(request, 'core/home.html', {'form': form})


def whatsapp_redirect(request):
    phone_number = "919507207645"
    whatsapp_url = f"https://wa.me/{phone_number}"
    message = "Hello"
    encoded_message = urllib.parse.quote(message)
    whatsapp_url += f"?text={encoded_message}"
    return redirect(whatsapp_url)


def journey_view(request):
    return render(request, "core/journey.html", {"page": "Our Journey"})
