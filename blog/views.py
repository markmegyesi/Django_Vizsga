from django.shortcuts import get_object_or_404, render
from .models import PostModel
from django.views.generic import ListView
from django.contrib.auth.models import User

# function based views
def home(request):
    context = {
        "posts": PostModel.objects.all()
    }

    return render(request, 'blog/home.html', context=context)

class PostListView(ListView):
    model = PostModel
    template_name = 'blog/home.html' 
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class UserPostListView(ListView):
    model = PostModel
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by= 5

    def get_queryset(self):
        user_object = get_object_or_404(User, username=self.kwargs.get('username'))
        data = PostModel.objects.filter(author=user_object)
        return data