from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import messages
from django.core.paginator import Paginator

# ── 1. LIST all blogs ──────────────────────────────────────
def list_blogs(request):
    query = request.GET.get('q')

    blogs = Blog.objects.all().order_by('-created_at')

    # 🔍 SEARCH LOGIC
    if query:
        blogs = blogs.filter(title__icontains=query) | blogs.filter(content__icontains=query)

    # 📄 PAGINATION
    paginator = Paginator(blogs, 5)  # 5 blogs per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/list.html', {
        'blogs': page_obj,
        'page_obj': page_obj,
        'query': query
    })


# ── 2. GET a single blog by ID ─────────────────────────────
def get_blog(request, id):
    blog = get_object_or_404(Blog, id=id)
    return render(request, 'blog/detail.html', {'blog': blog})


# ── 3. CREATE a new blog ───────────────────────────────────
@login_required
def create_blog(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        Blog.objects.create(
            title=title,
            content=content,
            author=request.user,  
            image=request.FILES.get('image') 
        )
        messages.success(request, "Blog created successfully!")
        return redirect('list-blogs')

    return render(request, 'blog/create.html')



@login_required
def edit_blog(request, id):

    blog = get_object_or_404(Blog, id=id)

    # Only author can edit
    if request.user != blog.author:
        return HttpResponseForbidden("You can only edit your own blog.")

    if request.method == 'POST':
        blog.title = request.POST.get('title')
        blog.content = request.POST.get('content')
        blog.save()
        messages.success(request, "Blog updated successfully!")
        return redirect('get-blog', id=blog.id)

    return render(request, 'blog/edit.html', {'blog': blog})

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # create user
        user = User.objects.create_user(
            username=username,
            password=password
        )

        # auto login after signup
        login(request, user)

        return redirect('list-blogs')

    return render(request, 'blog/register.html')