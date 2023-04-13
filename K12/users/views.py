from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CreationForm
from .models import Company


def test(request):
    company = get_object_or_404(Company, pk=1)
    context = {
        'company': company,
    }
    return render(request, "account/test.html", context)


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('info:index')
    template_name = 'users/signup.html'
