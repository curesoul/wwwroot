from django.urls import path

from . import views

urlpatterns = [
    path('<int:author_id>/', views.manage_books, name='manage_books'),
]
