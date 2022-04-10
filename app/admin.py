from django.contrib import admin
from .models import Photo, iCategory
from .models import Room, Booking

# Register your models here.

admin.site.register(iCategory)
admin.site.register(Photo)

admin.site.register(Room)
admin.site.register(Booking)
