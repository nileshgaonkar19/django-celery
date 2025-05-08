from django.shortcuts import render
# myapp/views.py
from django.http import JsonResponse
from .tasks import add

def index(request):
    print("Came here!!")
    result = add.delay(5, 7)
    print(str(result.id))
    return JsonResponse({'task_id': result.id})
