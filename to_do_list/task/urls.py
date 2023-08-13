from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.add_task, name = 'home'),
    path('incomplete/', views.incomplete_tasks, name = 'incomplete'),
    path('complete/', views.complete_tasks, name = 'complete'),
    path('add_task/', views.add_task, name = 'add'),
    path('delete_task/<int:id>', views.delete_task, name = 'delete'),
    path('edit_task/<int:id>', views.edit_task, name = 'edit'),
    path('make_complete/<int:id>', views.make_complete, name = 'make_complete'),
]