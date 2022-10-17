from django.shortcuts import render, HttpResponseRedirect
from django.forms import inlineformset_factory

from .models import Author, Book


def manage_books(request, author_id):
    author = Author.objects.get(pk=author_id)
    BookInlineFormSet = inlineformset_factory(Author, Book, extra=3, fields=('title', 'test'))
    if request.method == 'POST':
        formset = BookInlineFormSet(request.POST, instance=author)
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect('/')
    else:
        formset = BookInlineFormSet(instance=author)
    return render(request, 'attendance/manage_book.html', {'formset': formset})
