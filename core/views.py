from django.shortcuts import redirect, render
from django.urls import reverse_lazy

# Create your views here.

def home(request):
    if not request.user.is_authenticated:
        return redirect(reverse_lazy('accounts:login'))