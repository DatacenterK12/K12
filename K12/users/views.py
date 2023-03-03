from django.shortcuts import get_object_or_404, render

from .models import Company, UserCompany


def test(request):
    user_company = UserCompany.objects.all()
    company = get_object_or_404(Company, pk=1)
    context = {
        'company': company,
    }
    return render(request, "account/test.html", context)
