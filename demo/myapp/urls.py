from django.urls import path
from . import views  # Ensure views.py is being imported correctly

urlpatterns = [
    path('', views.home, name='home'),  # Replace 'home' with an actual view function
    path('todos/', views.todos, name="Todos")
]
