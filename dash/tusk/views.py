from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, "Index.html")

def display_login(request):
    return render(request, "Login.html")

def display_register(request):
    return render(request, "Register.html")

def home(request):
    return render(request, "Home.html")

def test(request):
    return render(request, "Test.html")

def profile(request):
    return render(request, "Profile.html")

def bookmarks(request):
    return render(request, "Bookmark.html")