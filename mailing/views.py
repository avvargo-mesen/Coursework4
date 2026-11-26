from django.shortcuts import render
from .models import Mailing, Client
# Create your views here.

def home(request):
    context = {
        'total_mailings': Mailing.objects.count(),
        'active_mailings': Mailing.objects.filter(status='started').count(),
        'unique_clients': Client.objects.count(),
        }
    return render(request, 'mailing/home.html', context)



