from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def RegisterUserView(request):
    context = {
        "some_var": "something"
    }
    return render(request, "register_user.html", context)

def UserDetailView(request):
    context = {
        "user_id": "0"
    }
    return render(request, "user_detail.html", context)


def UsersList(request):
    return HttpResponse("Here will be a list of users")
