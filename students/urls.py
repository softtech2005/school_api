from django.urls import path
from .views import StudentListCreateView, StudentDetailView

urlpatterns = [
    path('Students/', StudentListCreateView.as_view()),
    path('Students/<int:pk>/', StudentDetailView.as_view()),
]