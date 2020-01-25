from django.contrib import admin

# Register your models here.
from .models import Location
from .models import LocationType
from .models import Franchise


admin.site.register(Location)

admin.site.register(Franchise)


admin.site.register(LocationType)