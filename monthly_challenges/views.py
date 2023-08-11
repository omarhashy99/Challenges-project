from django.http import  HttpResponseRedirect
from django.urls import reverse

def index(request):   
    redirect_path = reverse("main_page") # /challenge/
    return HttpResponseRedirect(redirect_path)
