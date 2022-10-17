from django.forms import ModelForm, formset_factory

from .models import Customer, Item, Schedule, TestResult


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'