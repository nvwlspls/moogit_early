from django.shortcuts import render, render_to_response


# Create your views here.

import datetime
import csv

# from forms import 
from django.http           import HttpResponse
from django.template       import RequestContext, loader
from django.shortcuts      import get_object_or_404, render_to_response, redirect, render
from django.utils          import timezone
from django.contrib        import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.views.generic import TemplateView, View, ListView, \
    UpdateView, DeleteView, CreateView, FormView



class homePage(View):

    def get(self, request, *arg, **kwargs):
        from models import Show2
        showsByDate    = Show.objects.all().order_by('Date')
        next10Shows    = showsByDate[10:]
        return render_to_response('pages/home.html', 
                                 {'shows' :next10Shows}, 
                                  context_instance = RequestContext(request))

# def homePage(request):
#   if request.method == 'GET':
#       #show the shows
#       from models import Show
#       showsByDate    = Show.objects.all().order_by('Date')
#       next10Shows    = showsByDate[10:]

#       return render_to_response('pages/home.html',
#                               {'shows' : next10Shows},
#                               context_instance = RequestContext(request))

#   if request.method == 'POST':
#       return redirect('homePage')