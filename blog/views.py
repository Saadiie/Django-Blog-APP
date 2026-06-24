from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import messages
from django.core.paginator import Paginator
import uuid


# 1. LIST all blogs
def list_blogs(request):
    query = request.GET.get('q')
    blogs = Blog.objects.all().order_by('-created_at')

    if query:
        blogs = blogs.filter(title__icontains=query) | blogs.filter(content__icontains=query)

    paginator = Paginator(blogs, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/list.html', {
        'blogs': page_obj,
        'page_obj': page_obj,
        'query': query
    })


# 2. GET a single blog by ID
def get_blog(request, id):
    blog = get_object_or_404(Blog, id=id)
    return render(request, 'blog/detail.html', {'blog': blog})


# 3. CREATE a new blog
@login_required
def create_blog(request):
    if request.method == 'POST':
        title   = request.POST.get('title')
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


# 4. EDIT a blog
@login_required
def edit_blog(request, id):
    blog = get_object_or_404(Blog, id=id)

    if request.user != blog.author:
        return HttpResponseForbidden("You can only edit your own blog.")

    if request.method == 'POST':
        blog.title   = request.POST.get('title')
        blog.content = request.POST.get('content')
        blog.save()
        messages.success(request, "Blog updated successfully!")
        return redirect('get-blog', id=blog.id)

    return render(request, 'blog/edit.html', {'blog': blog})


# 5. REGISTER
def register(request):
    if request.user.is_authenticated:
        return redirect('list-blogs')

    errors = {}

    if request.method == 'POST':
        email            = request.POST.get('email', '').strip()
        password         = request.POST.get('password', '')
        confirm_password = request.POST.get('confirm_password', '')

        # ── Validate email ──────────────────────────────────────────
        if not email:
            errors['email'] = 'Email is required.'
        elif '@gmail.com' not in email:
            errors['email'] = 'Only Gmail addresses (@gmail.com) are allowed.'
        elif User.objects.filter(email=email).exists():
            errors['email'] = 'An account with this email already exists.'

        # ── Validate passwords ──────────────────────────────────────
        if not password:
            errors['password'] = 'Password is required.'
        elif len(password) < 6:
            errors['password'] = 'Password must be at least 6 characters.'

        if not confirm_password:
            errors['confirm_password'] = 'Please confirm your password.'
        elif password and password != confirm_password:
            errors['confirm_password'] = 'Passwords do not match.'

        # ── If no errors, create user ───────────────────────────────
        if not errors:
            # Auto-generate a unique username from the Gmail prefix
            gmail_prefix = email.split('@')[0]          # e.g. "saad.dev"
            base_username = gmail_prefix.replace('.', '_')  # e.g. "saad_dev"

            username = base_username
            counter  = 1
            while User.objects.filter(username=username).exists():
                username = f"{base_username}_{counter}"
                counter += 1

            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
            )

            login(request, user)
            messages.success(request, f"Welcome to Inkwell! Your username is @{username}")
            return redirect('list-blogs')

        # Re-render with errors and preserve the typed email
        return render(request, 'blog/register.html', {
            'errors': errors,
            'email':  email,
        })

    return render(request, 'blog/register.html')