from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, render_to_response

from django.http import HttpResponse


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

def homePage(request):
    if request.method == 'GET':
        #show the shows
        from models import Show2, showOrder
        showsByDate    = Show2.objects.all().order_by('Date')
        next10Shows    = showsByDate[:10]

        return render_to_response('pages/home.html',
                                {'shows' : next10Shows},
                                context_instance = RequestContext(request))

    if request.method == 'POST':
        return redirect('homePage')

def modHome(request):
    if request.method == 'GET':
        if request.user.is_authenticated():
            return render_to_response("pages/user.html")
        else:
            return HttpResponse("The user is not is_authenticated")
    else: 
        return redirect('homePage')