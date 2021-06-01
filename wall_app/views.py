from wall_app.models import *
from django.shortcuts import render, redirect

def my_wall(request):
    logged_user = User.objects.get(id=request.session["userid"])
    messages_by_user = logged_user.message_by_user.all()
    comments_by_user = logged_user.comment_by_user.all()

    context = {
        "user_info": User.objects.get(id=request.session["userid"]),
        'all_messages': messages_by_user,
        'all_comments': comments_by_user
    }
    return render(request, "my-wall.html", context)

def new_message(request):
    if request.method == "POST":
        logged_user = User.objects.get(id=request.session["userid"])

        Message.objects.create(
            message=request.POST["message"],
            user=logged_user
        )
        return redirect('/wall')

def new_comment(request):
    if request.method == "POST":
        logged_user = User.objects.get(id=request.session["userid"])
        messages = Message.objects.filter(user=logged_user)

        Comment.objects.create(
            comment=request.POST["comment"],
            user=logged_user,
            message=messages
        )
        return redirect('/wall')