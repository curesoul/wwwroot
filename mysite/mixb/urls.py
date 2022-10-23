from django.urls import path

from . import views

app_name = 'mixb'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pp_id>/', views.details, name='details'),
    path('add-result/<int:schedule_id>/', views.add_result, name='add_result'),
    path('test/<int:schedule_id>/<int:batch_no>/', views.test, name='test'),
]
