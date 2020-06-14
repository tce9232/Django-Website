from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from home.models import Post

class ArchiveView(generic.ListView):
    template_name = 'articles/archive.html'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        queryset = Post.objects.order_by('-created_on')
        return queryset

class ArticleView(generic.ListView):
    template_name = 'articles/article.html'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Post
def article_detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        "post": post,
    }

    return render(request, "articles/article_detail.html", context)