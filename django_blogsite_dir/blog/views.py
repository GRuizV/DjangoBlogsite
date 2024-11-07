from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse, HttpRequest
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post



def home(request: HttpRequest) -> HttpResponse:

    context = {
        'posts': Post.objects.all()
    }

    return render(request, 'blog/home.html', context=context)



class PostListView(ListView):

    model = Post
    template_name = 'blog/home.html'    #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']



class PostDetailView(DetailView):

    model = Post



class PostCreateView(LoginRequiredMixin, CreateView):

    model = Post
    fields = ['title', 'content']
    
    # form valid function overridden to set the author to the logged user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    model = Post
    fields = ['title', 'content']
        
    # form valid function overridden to set the author to the logged user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


    def test_func(self):

        """
        This is the test to make sure the author of the post to be updated
        is the same person trying to update the post
        """
        
        post = self.get_object()

        if self.request.user == post.author:
            return True

        return False



class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):

    model = Post
    success_url = '/'   # This is the way to redirecto to home

    def test_func(self):

        """
        This is the test to make sure the author of the post to be updated
        is the same person trying to update the post
        """
        
        post = self.get_object()

        if self.request.user == post.author:
            return True

        return False





def about(request: HttpRequest) -> HttpResponse:

    return render(request, 'blog/about.html', context = {'title': 'About'})












