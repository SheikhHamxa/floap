from django.contrib import admin

# Register your models here.
from.models import Package, PackageStatus, PackageRates, PackageBilling
admin.site.register(Package)
admin.site.register(PackageStatus)
admin.site.register(PackageRates)
admin.site.register(PackageBilling)
