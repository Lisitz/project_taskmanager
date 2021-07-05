from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('create/', views.create, name='create'),
    path('<int:task_id>/delete/', views.delete_task, name='delete'),
    path('<int:task_id>/', views.task_detail, name='detail'),

]

