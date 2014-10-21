from django.shortcuts import render

# Create your views here.

import datetime
import csv

# from forms import 
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render_to_response, redirect, render
from django.utils import timezone
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def homePage(request):
	return render_to_response('pages/home.html')

