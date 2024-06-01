from django.contrib import admin

from .models import Drone
from .models import DroneImage
from .models import Feature
from .models import Specification

admin.site.register(Drone)
admin.site.register(Feature)
admin.site.register(Specification)
admin.site.register(DroneImage)
