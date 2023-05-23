from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.addTodoView, name='add'),
    path('delete/<int:pk>', views.deleteTodoView, name='delete'),
    path('', views.todoappView, name='todolist'),
]