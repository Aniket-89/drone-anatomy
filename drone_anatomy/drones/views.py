from django.shortcuts import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.cache import cache_page

from .models import Drone
from .models import DroneImage
from .models import Feature
from .models import Specification


# @cache_page(60 * 525600)
def drone_list_view(request):
    drones = Drone.objects.all()
    context = {"drones": drones, "page": "Drone Anatomy | Drones"}
    return render(request, "drones/drone-list.html", context)


# @cache_page(60 * 525600)
def drone_detail_view(request, pk):
    try:
        drone = Drone.objects.get(pk=pk)
    except Drone.DoesNotExist:
        return HttpResponseRedirect(reverse("404.html"))

    features = Feature.objects.filter(drone=drone)
    specifications = Specification.objects.filter(drone=drone)
    images = DroneImage.objects.filter(drone=drone)

    context = {
        "page": drone.name,
        "drone": drone,
        "features": features,
        "specifications": specifications,
        "images": images,
    }
    return render(request, "drones/drone-detail.html", context)
