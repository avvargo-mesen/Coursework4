from django.urls import path
from . import views
from . views import ClientListView, ClientCreateView, ClientUpdateView, ClientDeleteView

app_name = 'mailing'

urlpatterns = [
     path('', views.home, name='home'),
     path('clients/', ClientListView.as_view(), name='ClientList'),
     path('clients/create/', ClientCreateView.as_view(), name='ClientCreate'),
     path('clients/<int:pk>/update/', ClientUpdateView.as_view(), name='ClientUpdate'),
     path('clients/<int:pk>/delete/', ClientDeleteView.as_view(), name='ClientDelete'),
]