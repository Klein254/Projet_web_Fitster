from django.shortcuts import render, redirect
from .models import User


def index(request):
    return render(request, "index.html")


def blog(request):
    return render(request, "blog.html")


def contact(request):
    return render(request, "contact.html")


def workouts(request):
    return render(request, "workouts.html")


def abs100(request):
    return render(request, "abs-100-dara.html")


def general(request):
    return render(request, "general-workouts.html")


def marathon(request):
    return render(request, "marathon.html")


def running(request):
    return render(request, "running.html")


def total_burn(request):
    return render(request, "total-burn.html")


def fitness(request):
    return render(request, "fitness.html")


def signup(request):
    return render(request, "signup.html")


def insertData(request):
    if request.method == "POST":
        name = request.POST.get('name')
        height = request.POST.get('height')
        weight = request.POST.get('weight')
        age = request.POST.get('age')
        gender = request.POST.get('gender')

        query = User(name=name,
                     height=height,
                     weight=weight,
                     age=age,
                     gender=gender, )
        query.save()
        return redirect("/")


def User_list(request):
    return render(request, "userlist.html")

