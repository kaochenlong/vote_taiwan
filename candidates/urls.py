from django.urls import path
from . import views

app_name = "candidates"

urlpatterns = [
    path("", views.index, name="index"),
    path("new", views.new, name="new"),
    path("<id>", views.show, name="show"),
]
