from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.generic.base import TemplateView

from .forms import PhoneForm


def order_call(request):
    form = PhoneForm()
    if request.method == "POST":
        form = PhoneForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data['phone']
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            send_mail(
                f'Заказ обратного звонка - {subject}',
                f'{subject}\n{name}\n{str(phone)}',
                'flexa@k12.spb.ru',
                ['ep@k12.spb.ru', ]
            )
            return JsonResponse({"status": "Запрос отправлен!"}, status=200)
        return JsonResponse({"errors": 'Слишком многа букав!!!!'}, status=400)
    return JsonResponse({"Method not alowed"}, status=500)


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
