from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from posts.models import UserPostsModel


# Create your views here.
def index(request):
    return render(request, 'user/index.html')


def home_view(request):
    if request.user.is_authenticated:
        user_posts_query = UserPostsModel.objects.all()
        context = {
            "username": request.user.username,
            "is_user_login": True,
            "user_posts_query":user_posts_query
        }
    else:
        context = {
            "username": "UnAuthorized User",
            "is_user_login": False
        }
    return render(request, 'user/home.html', context)


def register_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        if password != confirm_password:
            context = {
                "error": True,
                "error_message": "Password does not match"
            }
            return render(request, "user/register.html", context)

        user = get_user_model().objects.create(username=username, email=email)
        user.set_password(password)
        user.save()
        return redirect("login_view")

    return render(request, "user/register.html")


def login_view(request):
    if request.method == "POST":
        # print(request.POST)
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home_view")
        else:
            return render(request, "users/login.html", context={'error_message': "Invalid Username or Password"})
    else:
        return render(request, "user/login.html")


def logout_view(request):
    logout(request)
    return redirect("login_view")
