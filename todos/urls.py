from django.urls import path
from todos.views import todo_list_list

urlspatterns = [
    path("", todo_list_list, name="todo_list_list"),
]
