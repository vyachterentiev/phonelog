from django.http import HttpResponse

def index(request):
    return HttpResponse("<p style=\"color:red; background-color:black; text-align:center\">Hi there html</p>")

def number(request, id):
    return HttpResponse(f"Page number : {id}")