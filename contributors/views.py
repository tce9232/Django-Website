from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from contributors.models import Contributor

class ContributorView(generic.ListView):
    template_name = 'contributors/contributors.html'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        queryset = Contributor.objects.order_by('name')
        return queryset

def contributor_detail(request, pk):
    contributor = Contributor.objects.get(pk=pk)
    context = {
        "contributor": contributor,
    }

    return render(request, "contributor_detail.html", context)