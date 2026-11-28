from django.urls import path
from . import views
from . views import ClientListView, ClientCreateView, ClientUpdateView, ClientDeleteView, MessageListView, MessageCreateView, MessageUpdateView, MessageDeleteView,MailingListView,MailingCreateView,MailingUpdateView,MailingDeleteView,MailingDetailView

app_name = 'mailing'

urlpatterns = [
     path('', views.home, name='home'),
     path('clients/', ClientListView.as_view(), name='ClientList'),
     path('clients/create/', ClientCreateView.as_view(), name='ClientCreate'),
     path('clients/<int:pk>/update/', ClientUpdateView.as_view(), name='ClientUpdate'),
     path('clients/<int:pk>/delete/', ClientDeleteView.as_view(), name='ClientDelete'),
     path('message/', MessageListView.as_view(), name='MessageList'),
     path('message/create/', MessageCreateView.as_view(), name='MessageCreate'),
     path('message/<int:pk>/update/', MessageUpdateView.as_view(), name='MessageUpdate'),
     path('message/<int:pk>/delete/', MessageDeleteView.as_view(), name='MessageDelete'),
     path('mailing/', MailingListView.as_view(), name='MailingList'),
     path('mailing/create/', MailingCreateView.as_view(), name='MailingCreate'),
     path('mailing/<int:pk>/update/', MailingUpdateView.as_view(), name='MailingUpdate'),
     path('mailing/<int:pk>/delete/', MailingDeleteView.as_view(), name='MailingDelete'),
     path('mailing/<int:pk>/detail/', MailingDetailView.as_view(), name='MailingDetail'),
]

