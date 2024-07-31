from datetime import datetime
from django.shortcuts import render

def index(request):
    context = {}
    context["Today"] = datetime.today()
    return render(request , "index.html" , context)