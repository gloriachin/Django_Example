
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.http import Http404

from .models import Paragraph
from django.urls import reverse
from django.views import generic
#def index(request):
#    return HttpResponse("Hello, this is My Blog.")




class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'latest_paragraph_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Paragraph.objects.order_by('-pub_date')[:5]



class DetailView(generic.DetailView):
    model = Paragraph
    template_name = 'blog/detail.html'