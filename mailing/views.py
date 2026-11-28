from django.shortcuts import render
from .models import Mailing, Client
from .forms import ClientForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

def home(request):
    context = {
        'total_mailings': Mailing.objects.count(),
        'active_mailings': Mailing.objects.filter(status='started').count(),
        'unique_clients': Client.objects.count(),
        }
    return render(request, 'mailing/home.html', context)

class ClientListView(ListView):
    model = Client
    template_name = 'mailing/client_list.html'

class ClientCreateView(CreateView):
    model = Client
    template_name = 'mailing/client_form.html'
    form_class = ClientForm
    success_url = reverse_lazy('mailing:ClientList')

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.owner = self.request.user
        return super().form_valid(form)

class ClientUpdateView(UpdateView):
    model = Client
    template_name = 'mailing/client_form.html'
    form_class = ClientForm
    success_url = reverse_lazy('mailing:ClientList')


class ClientDeleteView(DeleteView):
    model = Client
    template_name = 'mailing/client_confirm_delete.html'
    success_url = reverse_lazy('mailing:ClientList')
