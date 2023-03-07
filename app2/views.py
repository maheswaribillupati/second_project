from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def app2_first(request):
    return HttpResponse("<h1>it is the first view of the app2</h1>")
def app2_second(request):
    return HttpResponse("<h1><marquee>it is the second view of the app2</marquee></h1>")