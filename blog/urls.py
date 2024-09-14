from django.urls import path
import blog.views as blog_views

urlpatterns = [
    path("", blog_views.post_list, name="post-list"),
    path("<int:pk>", blog_views.post_detail, name="post-detail")
]