from django.contrib import admin

# Register your models here.
from .models import USer
from .models import UserType

# from.models import Sender,Receiver

# from.models import Manager,PostPerson,Staff
# admin.site.register(Sender)
admin.site.register(UserType)
admin.site.register(USer)

# admin.site.register(Receiver)
# admin.site.register(Manager)
# admin.site.register(PostPerson)
# admin.site.register(Staff)

"""
class USerAdmin(admin.ModelAdmin):
    readonly_fields = ('highlighted')


admin.site.register(USer, USerAdmin)
"""