from django.shortcuts import redirect, render
from blog.decorators import allowed_user
from blog.forms import BlogForm
from blog.models import blog
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="login")
@allowed_user(allowed_roles=["Doctor"])
def create(request):
    if request.method == "POST":
        form = BlogForm(request.POST,request.FILES)
        context = {"form":form}
        if form.is_valid():
            blogs = blog()
            blogs.title = form.cleaned_data.get("title")
            blogs.image = form.cleaned_data.get("image")
            blogs.category = form.cleaned_data.get("category")
            blogs.author = request.user
            blogs.draft = form.cleaned_data.get("draft")
            blogs.summary = form.cleaned_data.get("summary")
            blogs.content = form.cleaned_data.get("content")
            blogs.save()
            return redirect("Blogs")
        else:
            return render(request,"blog/create.html",context)
    else:
        form = BlogForm()
        context = {"form":form}
        return render(request,"blog/create.html",context)

@login_required(login_url="login")
def blogs(request):
    if request.user.groups.all()[0].name == "Patient":
        getBlogs = blog.objects.filter(draft=0)
    else:
        getBlogs = blog.objects.filter(author=request.user)
    context = {"blogs":getBlogs}
    return render(request,"blog/blog.html",context)

@login_required(login_url="login")
def displayBlog(request,pk):
    blogs = blog.objects.get(id=pk)
    context = {"blog":blogs}
    return render(request,"blog/displayBlog.html",context)
