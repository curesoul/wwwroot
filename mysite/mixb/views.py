from django.shortcuts import render, get_object_or_404

from .models import Customer, Item, Schedule, TestResult


def index(request):
    schedules = Schedule.objects.all()
    context = {
        'schedules': schedules
    }
    return render(request, 'mixb/index.html', context)


def details(request, pp_id):
    detail = get_object_or_404(Schedule, pk=pp_id)
    return render(request, 'mixb/detail.html', {'detail': detail})