from django.contrib import admin

from .models import Customer, Item, Schedule, TestResult


class TestResultInline(admin.TabularInline):
    model = TestResult
    extra = 3


class ScheduleAdmin(admin.ModelAdmin):
    inlines = [TestResultInline]


admin.site.register(Customer)
admin.site.register(Item)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(TestResult)
