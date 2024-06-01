from django.contrib import admin

from .models import Contact
from .models import Member
from .models import Newsletter
from .models import Partner
from .models import Service

# Register your models here.
admin.site.register(Service)
admin.site.register(Partner)
admin.site.register(Contact)
admin.site.register(Newsletter)
admin.site.register(Member)
