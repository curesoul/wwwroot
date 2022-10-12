from django.contrib import admin

from .models import AttendanceLog, MonthList, PersonList


admin.site.register(AttendanceLog)
admin.site.register(MonthList)
admin.site.register(PersonList)

