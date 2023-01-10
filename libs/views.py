from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django.views.generic import ListView, DetailView
from libs.models import *
from libs.views import *

# Create your views here.
class index(ListView):
    model = t_sign
    template_name = 'index.html'
    queryset= t_sign.objects.filter()
    context_object_name = 'data'

class SearchView(ListView):
    model = t_sign
    template_name = 'index.html'
    context_object_name = 'data'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return t_sign.objects.filter(title__icontains=query).order_by('-id')

def showresults(request):
    if request.method == 'POST':
        dateFrom = request.POST.get('dateFrom')
        searchresult = t_sign.objects.raw("""SELECT s.id, s.title 
                                            from libs_t_sign s
                                            WHERE %s BETWEEN s.dateFrom AND s.dateTo """, [dateFrom])
        
        context = {
            'data': searchresult
        }
        template = "search.html"
        return render (request, template, context)
    else:
        
        template = "search.html"
        return render (request, template)
