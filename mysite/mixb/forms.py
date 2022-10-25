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
        # fields = ['plan', 'batch', 'mv', 'scorch', 'fmin', 'fmax', 't10', 't90']


class SgForm(ModelForm):
    class Meta:
        model = TestResult
        fields = ['plan', 'batch', 'sg']
