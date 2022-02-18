from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.hashers import make_password
from pages.models import CustomUser
from pages.models import Post

# Create your views here.

#Login
def loginFunc(request):
    if not request.user.is_anonymous:
        return redirect('/')
    print(request.user.is_anonymous)
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        print(username)
        print(password)
        user=authenticate(username=username,password=password)
        print("user ", user)
        login(request,user)
        return redirect("/")

    return render(request,"login.html")

#Signup
def signupFunc(request):

#username: randomguy, password: random@123

    if request.method=="POST":
        username=request.POST.get("username")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        password=request.POST.get("password")
        cpassword=request.POST.get("cpassword")
        if password!=cpassword:
            return redirect("/")
        else:
            user=CustomUser(username=username,email=email,phone=phone,password=make_password(password))
            user.save()
            print(user)
            return redirect("/login")
    elif request.user.is_anonymous:
        print(request.user.is_anonymous)
        return render(request,"signup.html")
    else:
        return redirect("/")

#Home
def homeFunc(request):
    if request.user.is_anonymous:
        return redirect("/login")
    posts=Post.objects.all()
    context={
        "posts":posts,
        "username":request.user.username
    }
    return render(request,"home.html",context)

#Logout
def logoutFunc(request):
    print(request.user)
    if request.user.is_anonymous is not None:
        logout(request)
    return redirect("/login")

#CREATE POSt
def createPost(request):
    if request.method=="POST":
        postedBy=request.user
        postTitle=request.POST.get("posttitle")
        description=request.POST.get("description")
        post=Post(postedBy=postedBy,postTitle=postTitle,description=description)
        post.save()
    return redirect("/")

#EDIT POST
def editPost(request,postTitle):
    if request.user.is_anonymous:
        return redirect("/login")
    post=Post.objects.get(postTitle=postTitle)
    print(post.postedBy.username)
    print(request.user.username)
    if request.user.username != post.postedBy.username:
        return redirect("/")
    return render(request,"edit.html",{"post":post,"postTitle":postTitle})

#UPDATE POST
def updatePost(request,postTitle):
    if request.method=="POST":
        if request.user.is_anonymous:
            return redirect("/login")
        post=Post.objects.get(postTitle=postTitle)
        post.postTitle=request.POST.get("posttitle")
        post.description=request.POST.get("description")
        post.save()
    return redirect("/")

#DELETE POST
def deletePost(request,postTitle):
    if request.user.is_anonymous:
        return redirect("/login")
    post=Post.objects.get(postTitle=postTitle)
    print("Hello")
    if post.postedBy.username==request.user.username:
        posts=Post.objects.filter(postTitle=postTitle)
        print(posts)
        Post.objects.filter(postTitle=postTitle).delete()
    return redirect("/")