from django.http import JsonResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def load_more(request):
    # Your logic here
    data = {"message": "This is the loaded content."}
    return JsonResponse(data)
