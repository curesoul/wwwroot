from django.shortcuts import render, get_object_or_404
from django.forms import formset_factory
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

from .models import Customer, Item, Schedule, TestResult
from .forms import CustomerForm, TestForm, SgForm


def index(request):
    schedules = Schedule.objects.all()
    batch_no = 1
    context = {
        'schedules': schedules,
        'batch_no' : batch_no,
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


# def test(request, schedule_id, batch_no):
#     schedule = get_object_or_404(Schedule, pk=schedule_id)
#     form = TestForm(initial={'plan': schedule.id, 'batch': batch_no})
#     if request.method == 'POST':
#         form = TestForm(request.POST)
#         if form.is_valid():
#             form.save()
#             batch_no = int(request.POST['batch'])
#             return HttpResponseRedirect(reverse('mixb:test', args=(schedule_id, batch_no+1)))
#     context = {
#         'form': form,
#         'detail': schedule,
#     }
#     return render(request, 'mixb/test.html', context)

def test(request, schedule_id, batch_no):
    schedule = get_object_or_404(Schedule, pk=schedule_id)
    try:
        batch_result = TestResult.objects.get(plan=schedule_id, batch=batch_no)
        form = TestForm(initial={'plan': schedule.id, 'batch': batch_no}, instance=batch_result)
        types = 'edit'
    except:
        form = TestForm(request.POST or None, initial={'plan': schedule.id, 'batch': batch_no})
        types = 'create'

    if types == 'create':
        if request.method == 'POST':
            form = TestForm(request.POST)
            if form.is_valid():
                form.save()
                batch_no = int(request.POST['batch'])
                return HttpResponseRedirect(reverse('mixb:test', args=(schedule_id, batch_no+1)))
    if types == 'edit':
        if request.method == 'POST':
            form = TestForm(request.POST, instance=batch_result)
            if form.is_valid():
                form.save()
                batch_no = int(request.POST['batch'])
                return HttpResponseRedirect(reverse('mixb:test', args=(schedule_id, batch_no+1)))

    context = {
        'form': form,
        'detail': schedule,
    }
    return render(request, 'mixb/test.html', context)


def test_sg(request, schedule_id, batch_no):
    schedule = get_object_or_404(Schedule, pk=schedule_id)
    try:
        batch_result = TestResult.objects.get(plan=schedule_id, batch=batch_no)
        form = SgForm(initial={'plan': schedule.id, 'batch': batch_no}, instance=batch_result)
        types = 'edit'
    except:
        form = SgForm(request.POST or None, initial={'plan': schedule.id, 'batch': batch_no})
        types = 'create'

    if types == 'create':
        if request.method == 'POST':
            form = SgForm(request.POST)
            if form.is_valid():
                form.save()
                batch_no = int(request.POST['batch'])
                return HttpResponseRedirect(reverse('mixb:test_sg', args=(schedule_id, batch_no+1)))
    if types == 'edit':
        if request.method == 'POST':
            form = SgForm(request.POST, instance=batch_result)
            if form.is_valid():
                form.save()
                batch_no = int(request.POST['batch'])
                return HttpResponseRedirect(reverse('mixb:test_sg', args=(schedule_id, batch_no+1)))

    context = {
        'form': form,
        'detail': schedule,
    }
    return render(request, 'mixb/test_sg.html', context)

