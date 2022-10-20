from django.urls import path
from django.shortcuts import redirect

from . import views


# Useful for development
def redirect_about(request):
    return redirect("/code-combat-server/")


urlpatterns = [
    path("code-combat-server/", views.submit, name="submit"),
    path("code-combat-server/i-win", views.winner),
    path("code-combat-server/histogram/time/<int:id>", views.histogram_time, name="histogram_time"),
    path("code-combat-server/histogram/complexity/<int:id>", views.histogram_complexity, name="histogram_complexity"),
]
