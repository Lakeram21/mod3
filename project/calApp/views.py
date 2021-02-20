from django.shortcuts import render
import requests
import json
# Create your views here.
from django.http import HttpResponse

# storing into the database
# getting my form
from .forms import SignIn


def home(request):

    return render(request, "index.html")


def search(request):
    val = request.GET['result']

    response = requests.get("https://api.jikan.moe/v3/search/anime?q="+val)
    response.json()
# print(response.json())
    fox = response.json()
    view = fox["results"]

    return render(request, "search.html", {'result': view})


def searchlink(request):

    return render(request, "search.html", )


def get_name(request):

    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():

            return
            HttpResponseRedirect("/login/")
    else:
        form = NameForm()
    return render(request, 'signup.html', {'form': form})


def index(request):
    # placing a dict and having that display on the html
    # it renders the request being called. from the url
    return render(request, "index.html", {'name': "Sa"})


def login(request):

    return render(request, "login.html")


'''
def signup(request):
    signup = "tomatoes"
    return render(request, "signup.html", {'signup': signup})
'''


def form(request):

    form = SignIn()
    # checking if its post and this method add security to the data passed
    if request.method == "POST":

        # pulls the data from the post and saves it in form
        form = SignIn(request.POST)

        # helps to make sure that data is valid if not it will prompt again
        if form.is_valid():

            # then it saves an intsance of this data in the data base
            form.save()

    context = {"form": form}

    return render(request, "signup.html", context)


'''
def add(request):
    # map the result back to a seperate url or you can give it the same

    # request returns an object so we can access it through that get method
    val1 = int(request.GET['num1'])
    val2 = int(request.GET['num2'])
    result = val1 + val2

    # send the result to a different page with the calculated value or it can be send to the same page
    return render(request, "index.html", {'result': result})


def addName(request):
    # get the input from the user
    name = request.GET['nameTeacher']

    # create an instance of the db
    teacher = Teacher()
    # assign the user input to the instance
    teacher.firstName = name
    teacher.save()

    # getting the data from database
    teacher = Teacher.objects.all()

    return render(request, "index.html", {'name': teacher})





'''
