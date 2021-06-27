from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.core.paginator import Paginator
import datetime


from .models import Course, University, User

# Create your views here.

def index(request):
    return render(request, "UCAS_clear/index.html")

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("homepage"))
        else:
            return render(request, "UCAS_clear/login.html", {
                "message": "Invalid email and/or password."
            })
    else:
        return render(request, "UCAS_clear/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "UCAS_clear/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "UCAS_clear/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "UCAS_clear/register.html")


def homepage(request):

    courses = Course.objects.order_by('?')[:100]

    paginator = Paginator(courses, per_page=20)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    context = {

        'courses':page_obj.object_list,
        'paginator':paginator,
    }
    return render(request, "UCAS_clear/homepage.html", context)


def course(request, pk):

    course = Course.objects.get(id=pk)

    context = {

        'course':course,
    }

    return render(request, "UCAS_clear/course-detail.html", context)


def userpage(request):

    return render(request, "UCAS_clear/userpage.html")