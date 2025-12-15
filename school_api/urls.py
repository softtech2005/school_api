from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def home(request):
    return JsonResponse({
        "status": "ok",
        "message": "School API is running"
    })

urlpatterns = [
    path("", home),                # ROOT endpoint
    path("admin/", admin.site.urls),
    path("api/", include("students.urls")),
]
