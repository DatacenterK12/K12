from django.views.generic.base import TemplateView
from django.http import JsonResponse
from .forms import PhoneForm

from . import send_mail


def OrderCall(request):
    form = PhoneForm()
    if request.method == "POST" and request.is_ajax():
        form = PhoneForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data['phone']
            send_mail.send_mail(phone)
            return JsonResponse({"status": "Запрос отправлен!"}, status=200)
        else:
            errors = form.errors.as_json()
            return JsonResponse({"errors": errors}, status=400)


class MainPage(TemplateView):
    template_name = 'info/index.html'


class ServerPlacement(TemplateView):
    template_name = 'info/server_placement.html'


class RentOfServerRacks(TemplateView):
    template_name = 'info/rent_of_server_racks.html'


class RentOfSpaceForEquipment(TemplateView):
    template_name = 'info/rent_of_space_for_equipment.html'


class Crossing(TemplateView):
    template_name = 'info/crossing.html'


class Service(TemplateView):
    template_name = 'info/service.html'


class InternetAccess(TemplateView):
    template_name = 'info/internet_access.html'


class About(TemplateView):
    template_name = 'info/about.html'


class Contact(TemplateView):
    template_name = 'info/contact.html'


class Thanks(TemplateView):
    template_name = 'info/thanks.html'