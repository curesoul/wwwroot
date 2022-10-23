from django.shortcuts import render, get_object_or_404
from django.forms import formset_factory
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

from .models import Customer, Item, Schedule, TestResult
from .forms import CustomerForm, TestForm


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


def add_result(request, schedule_id):
    schedule = get_object_or_404(Schedule, pk=schedule_id)
    try:
        current_batch = schedule.testresult_set.get(pk=request.POST['batch'])
    except(KeyError, TestResult.DoesNotExist):
        return render(request, 'mixb/add-result.html', {
            'schedule': schedule,
            'error_message': "没有选择订单",
        })
    else:
        schedule.testresult_set.add(current_batch)
        return HttpResponseRedirect(reverse('schedule:add_result', args=(schedule.id,)))


def test(request, schedule_id, batch_no):
    schedule = get_object_or_404(Schedule, pk=schedule_id)
    form = TestForm(initial={'plan': schedule.id, 'batch': batch_no})
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('mixb:test', args=(schedule_id, batch_no+1)))
    context = {
        'form': form,
    }
    return render(request, 'mixb/test.html', context)
