from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("candidates/", include("candidates.urls")),
    path("admin/", admin.site.urls),
]
