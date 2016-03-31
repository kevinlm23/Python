# Create your views here.

from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response

from veh.models import *

def main (request):
    vehicle = Vehicle.objects.all().order_by("-fecha")
    paginator = Paginator(vehicle,1)

    try: pagina = int(request.GET.get("page",'1'))
    except ValueError: pagina = 1

    try:
        vehicle = paginator.page(pagina)
    except (InvalidPage, EmptyPage):
        vehicle = paginator.page(paginator.num_pages)

    return render_to_response("listado.html",dict(vehicle = vehicle, usuario = request.user))
