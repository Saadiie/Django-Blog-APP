from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog

# ── 1. LIST all blogs ──────────────────────────────────────
def list_blogs(request):
    blogs = Blog.objects.all().order_by('-created_at')
    return render(request, 'blog/list.html', {'blogs': blogs})


# ── 2. GET a single blog by ID ─────────────────────────────
def get_blog(request, id):
    blog = get_object_or_404(Blog, id=id)
    return render(request, 'blog/detail.html', {'blog': blog})


# ── 3. CREATE a new blog ───────────────────────────────────
def create_blog(request):
    if request.method == 'POST':
        title   = request.POST.get('title')
        content = request.POST.get('content')
        author  = request.POST.get('author')
        Blog.objects.create(title=title, content=content, author=author)
        return redirect('list-blogs')
    return render(request, 'blog/create.html')