from django.shortcuts import render
from django.shortcuts import render,redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate
# from rest_framework.authtoken.models import Token
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.authentication import TokenAuthentication
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_GET
import os

@require_GET
def data(request):
    n = request.GET.get('n')
    m = request.GET.get('m')
    # n=request.POST['n']
    # m=request.POST['m']
    # fp="D:\Django\1.txt"

    if n is None:
        return JsonResponse({'error': 'Parameter n is required'}, status=400)
    file_main_path="D:\Django"
    file_path = f'{file_main_path}\{n}.txt'
    # file_path=fp
    if m is not None:
        try:
            m = int(m)
            with open(file_path, 'r') as file:
                lines = file.readlines()
                if 1 <= m <= len(lines):
                    return JsonResponse({'response': lines[m-1]})
                else:
                    return JsonResponse({'error': 'Invalid line number'}, status=400)
        except ValueError:
            return JsonResponse({'error': 'Invalid line number'}, status=400)
    else:
        try:
            with open(file_path, 'r') as file:
                content = file.read()
                return JsonResponse({'response': content})
        except FileNotFoundError:
            return JsonResponse({'error': 'File not found'}, status=404)


# Create your views here.