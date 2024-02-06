from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(req):
    return render(req, 'tests/index.html', {})


def getStudentReport(req, std_id):
    return HttpResponse(f"Student id is {std_id}")