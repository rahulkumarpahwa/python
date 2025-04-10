from django.shortcuts import render , HttpResponse

# Create your views here.

def index (request):
    context = {
        "variable" : "Rahul Kumar"
    }
    return render(request, 'index.html', context)
    # return HttpResponse("this is home page")

def about (request):
    return HttpResponse("this is about page")