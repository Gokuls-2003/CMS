from django.urls import path
from .import views

urlpatterns = [
    # path("", views.student_application)
    path("", views.my_view),
]
