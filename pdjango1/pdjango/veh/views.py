# Create your views here.

##from veh.models import Vehicle
##from django.http import HttpResponse
##from django.shortcuts import render
##
##def listado (request):
##    return render (request, 'veh/listado.html', {})
##    
####    return HttpResponse ("Bienvenido")
####    tablav = Vehicle.objects.all()
####    output = ', '.join([p.motor_code for p in tablav])
####    return HttpResponse(output)
##
##



from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response

from veh.models import *

def main (request):
    vehicle = Vehicle.objects.all()
    paginator = Paginator(vehicle,1)

    try: pagina = int(request.GET.get("page",'1'))
    except ValueError: pagina = 1

    try:
        vehicle = paginator.page(pagina)
    except (InvalidPage, EmptyPage):
        vehicle = paginator.page(paginator.num_pages)

    return render_to_response("listado.html",dict(vehicle = vehicle, usuario = request.user))
