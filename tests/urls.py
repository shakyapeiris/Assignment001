from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.index, name="index"),
    path("student/<int:std_id>", view=views.getStudentReport, name="student"),
]