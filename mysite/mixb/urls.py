from django.urls import path

from . import views

app_name = 'mixb'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pp_id>/', views.details, name='details'),

]
