from django.shortcuts import render, redirect
from posts.models import UserPostsModel
from django.http import HttpResponse


# Create your views here.

def create_post(request):
    try:
        if not request.user.is_authenticated:
            return redirect("login_view")
        if request.method == "POST":
            print(request.POST)
            title = request.POST['title']
            description = request.POST['description']
            media = request.FILES['img']
            user = request.user
            UserPostsModel.objects.create(
                title=title,
                description=description,
                media=media,
                user=user
            )

        return render(request, 'user/home.html')
    except Exception as e:
        return HttpResponse(f"Something went wrong, {str(e)}")


def update_post(request, id):
    if not request.user.is_authenticated:
        return redirect("login_view")
    query = UserPostsModel.objects.get(id=id)
    if request.user != query.user:
        return HttpResponse("Only Post author can edit the POST")

    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        query.title = title
        query.description = description
        query.save()

        try:
            query.media = request.FILES["img"]
            query.save()
            return render(request, 'user/home.html')
        except:
            pass
    return render(request, "posts/update_post.html", {"post": query})


def delete_post(request, id):
    if not request.user.is_authenticated:
        return redirect("login_view")
    query = UserPostsModel.objects.get(id=id)
    if request.user != query.user:
        return HttpResponse("Only Post Author can edit the POST")
    query.delete()
    return redirect("home_view")
