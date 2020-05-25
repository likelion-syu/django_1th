from django.shortcuts import render

# Create your views here.
def home(reqest):
    return render(reqest, "blog/index.html")