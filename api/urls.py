from django.urls import path
from django.shortcuts import redirect

from . import views


# Useful for development
def redirect_about(request):
    return redirect("/the-great-code-off/")


urlpatterns = [
    path("the-great-code-off/", views.submit, name="submit"),
    path("the-great-code-off/i-win", views.winner),
    path("the-great-code-off/histogram/time/<int:id>", views.histogram_time, name="histogram_time"),
    path("the-great-code-off/histogram/complexity/<int:id>", views.histogram_complexity, name="histogram_complexity"),
    path("the-great-code-off/histogram/memory/<int:id>", views.histogram_memory, name="histogram_memory"),
]
