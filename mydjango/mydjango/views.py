from django.shortcuts import render


# Create your views here.

# 1
def about(request):
    return render(request, "about.html", {})

#2
def login(request):
    return render(request, "login.html", {})

#3
def dash(request):
    return render(request, "dash.html", {})


