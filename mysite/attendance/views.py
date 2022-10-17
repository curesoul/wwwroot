from django.shortcuts import render, HttpResponseRedirect
from django.forms import inlineformset_factory

from .models import Author, Book


def manage_books(request, author_id):
    # initial_dict = [
    #     {'batch_no': 1, },
    #     {'batch_no': 2, },
    #     {'batch_no': 3, },
    #     {'batch_no': 4, },
    #     {'batch_no': 5, },
    #     {'batch_no': 6, },
    #     {'batch_no': 7, },
    #     {'batch_no': 8, },
    #     {'batch_no': 9, },
    #     {'batch_no': 10, },
    #     {'batch_no': 11, },
    #     {'batch_no': 12, },
    #     {'batch_no': 13, },
    #     {'batch_no': 14, },
    #     {'batch_no': 15, },
    #     {'batch_no': 16, },
    #     {'batch_no': 17, },
    #     {'batch_no': 18, },
    #     {'batch_no': 19, },
    #     {'batch_no': 20, },
    #     {'batch_no': 21, },
    #     {'batch_no': 22, },
    #     {'batch_no': 23, },
    #     {'batch_no': 24, },
    #     {'batch_no': 25, },
    #     {'batch_no': 26, },
    #     {'batch_no': 27, },
    #     {'batch_no': 28, },
    #     {'batch_no': 28, },
    #     {'batch_no': 28, },
    #     {'batch_no': 28, },
    #     {'batch_no': 28, },
    #     {'batch_no': 21, },
    #     {'batch_no': 22, },
    #     {'batch_no': 23, },
    #     {'batch_no': 24, },
    #     {'batch_no': 25, },
    #     {'batch_no': 26, },
    #     {'batch_no': 27, },
    #     {'batch_no': 28, },
    #     {'batch_no': 29, },
    #     {'batch_no': 30, },
    #     {'batch_no': 31, },
    #     {'batch_no': 32, },
    #     {'batch_no': 33, },
    #     {'batch_no': 34, },
    #     {'batch_no': 35, },
    #     {'batch_no': 36, },
    #     {'batch_no': 37, },
    #     {'batch_no': 38, },
    #     {'batch_no': 39, },
    #     {'batch_no': 40, },
    #     {'batch_no': 41, },
    #     {'batch_no': 42, },
    #     {'batch_no': 28, },
    #     {'batch_no': 28, },
    # ]
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
