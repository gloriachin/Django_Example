
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import get_object_or_404, render
from django.http import Http404

from .models import Paragraph, Title, Subtitle
from django.urls import reverse
from django.views import generic
#def index(request):
#    return HttpResponse("Hello, this is My Blog.")




class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'latest_title_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Title.objects.order_by('-pub_date')



class DetailView(generic.ListView):
    
    template_name = 'blog/detail.html'
    context_object_name = 'latest_subtitle_list'

    @property
    def pk(self):
       return self.kwargs['pk']

    def get_queryset(self):
        print(f"pk = {self.pk}")
        return Subtitle.objects.all().filter(title=self.pk).order_by('-pub_date')



'''
class DetailView(generic.DetailView):
    model = Paragraph
    template_name = 'blog/detail.html'
'''
class ParagraphView(generic.ListView):
    template_name = 'blog/paragraph.html'
    context_object_name = 'latest_paragraph_list'

    @property
    #def pk(self):
    #   return self.kwargs['pk']
    def sub_id(self):
       return self.kwargs['sub_id']
    def get_queryset(self):
        #print(f"pk = {self.pk}")
        print(f"sub_id = {self.sub_id}")
        return Paragraph.objects.all().filter(subtitle=5).order_by('-pub_date')
