from django.shortcuts import render
from todos.admin import TodoList


def todo_list_list(request):
    todos = TodoList.objects.all()
    context = {"todo_list": todos}
    return render(request, "todos/list.html", context)
