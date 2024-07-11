from django.contrib import admin
from .models import Member, Attendance, Service, Ministers


admin.site.register(Member)
admin.site.register(Attendance)
admin.site.register(Service)
admin.site.register(Ministers)
