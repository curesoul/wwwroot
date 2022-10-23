from django.forms import ModelForm, formset_factory

from .models import Customer, Item, Schedule, TestResult


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


class TestForm(ModelForm):
    class Meta:
        model = TestResult
        fields = '__all__'
