from django.contrib import admin

from .models import AttendanceLog, MonthList, PersonList, Author, Book


admin.site.register(AttendanceLog)
admin.site.register(MonthList)
admin.site.register(PersonList)
admin.site.register(Author)
admin.site.register(Book)

