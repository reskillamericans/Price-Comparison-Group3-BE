from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, Welcome to the Price Comparison Tool.")

# Create your views here.
