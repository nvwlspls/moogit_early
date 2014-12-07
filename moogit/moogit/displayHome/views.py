from django.shortcuts import render

# Create your views here.
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

def homePage(request):
    if request.method == 'GET':
        #show the shows
        from models import Show2, showOrder
        showsByDate    = Show2.objects.all().order_by('Date')
        next10Shows    = showsByDate[:10]

        # orders = []
        # for show in next10Shows:
        #     bands = show.bands.all()
        #     for band in bands:
        #         order    = showOrder.objects.filter(bandID = band.bandID,  
        #                                             showID = show.show2ID)
        #         if len(order) > 0:
        #             orderNum = order[0].order
        #         else:
        #             orderNum = 0
        #         templist = [band.bandID, show.show2ID, orderNum]
        #         orders.append(templist)

        orders = showOrder.objects.all()
        


        return render_to_response('pages/home.html',
                                {'shows' : next10Shows,
                                 'orders' : orders},
                                context_instance = RequestContext(request))

    if request.method == 'POST':
        return redirect('homePage')
