from django.shortcuts import render
from blog.models import Post
# Create your views here.

def post_list(request):
    posts = Post.objects.all()

    context = {
        "post_list": posts
    }
    return render(
        request,
        template_name="blog/post_list.html",
        context=context
    )

def post_detail(request, pk):
    post = Post.objects.get(id=pk)

    context = {
        "post": post,
        "published_recently": post.published_recently
    }
    return render(
        request,
        template_name="blog/post_detail.html",
        context=context
    )