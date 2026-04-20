from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_trainees, name='trainee_list'),
    path('add/', views.add_trainee, name='trainee_add'),
    path('update/<int:id>/', views.update_trainee, name='trainee_update'),
    path('delete/<int:id>/', views.delete_trainee, name='trainee_delete'),
    path('details/<int:id>/', views.trainee_details, name='trainee_details'),
]
