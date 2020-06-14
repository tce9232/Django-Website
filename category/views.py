from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from home.models import Post


def category_view(request, category, pk):
    post = Post.objects.filter(categories__name__contains=category).order_by(
        '-created_on'
    )
    context = {
        "category": category,
        "post": post
    }

    return render(request, "category/categories.html", context)
