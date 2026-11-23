from django.contrib import admin
from .models import Client, Message, Mailing, Attempt

# Register your models here.
@admin.register(Client)
class ClientMailingAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'full_name', 'owner')


@admin.register(Message)
class MessageMailingAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject', 'owner')


@admin.register(Mailing)
class MailingMailingAdmin(admin.ModelAdmin):
    list_display = ('id', 'start_time', 'end_time', 'status', 'message', 'owner')


@admin.register(Attempt)
class CAttemptMailingAdmin(admin.ModelAdmin):
    list_display = ('id', 'attempt_time', 'status', 'mailing')