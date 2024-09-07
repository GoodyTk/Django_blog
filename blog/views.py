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