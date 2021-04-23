from xhtml2pdf import pisa
import datetime
from django.template.loader import get_template
# from django.template import Context
from django.http import HttpResponse
from django.conf import settings
import os
from django.shortcuts import render, get_object_or_404
from .models import Shipment


def home(request):
    return render(request, "shipments/index.html", {})


def about(request):
    return render(request, "shipments/about.html", {})


def contact(request):
    return render(request, "shipments/contact.html", {})


def services(request):
    return render(request, "shipments/services.html", {})


def truckloads(request):
    return render(request, "shipments/truckloads.html", {})


def ltl(request):
    return render(request, "shipments/ltl.html", {})


def intermodal(request):
    return render(request, "shipments/intermodal.html", {})


def air(request):
    return render(request, "shipments/air.html", {})


def ocean(request):
    return render(request, "shipments/ocean.html", {})


# def track(request, tracking_number=None):
#     if tracking_number != None:
#         shipment = get_object_or_404(Shipment, tracking_number=tracking_number)
#         data = {
#             "shipment": shipment
#         }
#         return render(request, "shipments/track.html", data)
#     else:
#         return render(request, "shipments/track.html", {})


def track(request):
    if request.GET.get('tracking_number'):
        shipment = request.GET.get('tracking_number')
        shipment = get_object_or_404(Shipment, tracking_number=shipment)
        shipment_statuses = shipment.histories.all()
        data = {
            "shipment": shipment,
            "shipment_statuses": shipment_statuses
        }
        return render(request, "shipments/track.html", data)
        # else:
    return render(request, "shipments/track.html", {})


def result(request):
    if request.GET.get('tracking_number'):
        shipment = request.GET.get('tracking_number')
        shipment = get_object_or_404(Shipment, tracking_number=shipment)
        shipment_statuses = shipment.histories.all()

        data = {
            "shipment": shipment,
            "shipment_statuses": shipment_statuses
        }

        template = get_template('shipments/result.html')
        html = template.render(data)

        file = open('consignment.pdf', "w+b")
        pisaStatus = pisa.CreatePDF(html.encode('utf-8'), dest=file,
                                    encoding='utf-8')

        file.seek(0)
        pdf = file.read()
        file.close()
        return HttpResponse(pdf, 'application/pdf')
    else:
        return render(request, "shipments/result.html", {})
