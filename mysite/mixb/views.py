from django.shortcuts import render, get_object_or_404
from django.forms import formset_factory

from .models import Customer, Item, Schedule, TestResult
from .forms import CustomerForm


def index(request):
    schedules = Schedule.objects.all()
    context = {
        'schedules': schedules
    }
    return render(request, 'mixb/index.html', context)


def details(request, pp_id):
    detail = get_object_or_404(Schedule, pk=pp_id)
    return render(request, 'mixb/detail.html', {'detail': detail})


def formsettest(request):
    TestFormSet = formset_factory(
        form=CustomerForm,
        extra=3
    )
    if request.method == 'POST':
        formset = TestFormSet(request.POST)
        if formset.is_valid():
            data = repr
