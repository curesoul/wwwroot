from django.shortcuts import render, HttpResponseRedirect
from django.forms import inlineformset_factory

from .models import Author, Book


def manage_books(request, author_id):
    initial_dict = []
    keys = range(1, 51)
    for i in keys:
        initial_dict += [{'batch_no': i}]

    author = Author.objects.get(pk=author_id)
    BookInlineFormSet = inlineformset_factory(Author, Book, extra=50, fields=('batch_no', 'title', 'test'))
    if request.method == 'POST':
        formset = BookInlineFormSet(request.POST, initial=initial_dict, instance=author)
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect('/')
    else:
        formset = BookInlineFormSet(initial=initial_dict, instance=author)
    return render(request, 'attendance/manage_book.html', {'formset': formset})
