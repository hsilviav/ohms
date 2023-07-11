from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import CustomUser

def is_logged_in(request: HttpRequest) -> bool:
    return request.user.is_authenticated

