from django.shortcuts import render, redirect
from . import servise
from .forms import *


def index(request):
    ctx = {
        "i_act": "active"

    }
    return render(request, 'fronted/mentor/index.html', ctx)


def about(request):
    abouts = servise.get_about()
    ctx = {
        "abouts": abouts,
        "a_act": "active"

    }
    return render(request, 'fronted/mentor/about.html', ctx)


def contact(request):
    model = Contact()
    form = ContactForm(request.POST, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            print(form.errors)
    ctx = {
        "form": form,
        "con_act": "active"

    }
    return render(request, 'fronted/mentor/contact.html', ctx)


def details(request):
    courses = servise.get_courses_details()
    ctx = {
        "courses_d": courses,

    }
    return render(request, 'fronted/mentor/courses_details.html', ctx)


def courses(request):
    course = servise.get_courses()
    ctx = {
        "courses": course,
        "c_act": "active",

    }
    return render(request, 'fronted/mentor/courses.html', ctx)


def trainers(request):
    trainer = servise.get_trainer()
    ctx = {
        "trainer": trainer,
        "t_act": "active"

    }
    return render(request, 'fronted/mentor/trainers.html', ctx)


def events(request):
    event = servise.get_events()
    ctx = {
        "event": event,
        "e_act": "active"
    }
    return render(request, 'fronted/mentor/events.html', ctx)


def pricing(request):
    pricings = servise.get_pricing()
    pricing_1 = servise.get_pricing_1()
    ctx = {
        "pricings": pricings,
        "pricing_1": pricing_1,
        'p_active': "active"
    }
    return render(request, 'fronted/mentor/pricing.html', ctx)

