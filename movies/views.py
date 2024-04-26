from django.shortcuts import render, redirect
from .models import Movie, WatchListMovie
import requests

# Create your views here.

def index(request):
    
    return render(request,'movies/index.html')

def search(request):
    
    url = f'https://moviesdatabase.p.rapidapi.com/titles/search/keyword/{keyword}'