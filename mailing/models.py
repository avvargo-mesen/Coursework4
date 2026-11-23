from django.db import models
from django.utils import timezone
from django.db.models import ForeignKey
from django.conf import settings


# Create your models here.

class Client(models.Model):
    '''Модель Клиент - возвращает мейл'''
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=150)
    comment = models.TextField(blank=True, null=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

class Message (models.Model):
    '''Модель Сообщение - возвращает тему письма'''
    subject = models.CharField(max_length=255)
    body = models.TextField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"

class Mailing(models.Model):
    '''Модель Рассылка - возвращает стаус отправки'''
    STATUS_CHOICES = [
        ('created', 'Создана'),
        ('started', 'Запущена'),
        ('finished', 'Завершена'),
    ]
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(choices=STATUS_CHOICES, max_length=20, default='created')
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    recipients = models.ManyToManyField(Client)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"Рассылка {self.id} от {self.start_time}"

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"

    def update_status(self):
        now = timezone.now()
        if now < self.start_time:
            status = 'created'
        elif self.start_time <= now <= self.end_time:
            status = 'started'
        else:
            status = 'finished'
        if self.status != status:
            self.status = status
            self.save(update_fields=['status'])

class Attempt(models.Model):
    '''Модель Попытка - возвращает количество попыток'''
    STATUS_CHOICES = [
        ('success', 'Успешно'),
        ('failed', 'Не успешно'),
    ]

    attempt_time = models.DateTimeField()
    status = models.CharField(choices=STATUS_CHOICES, max_length=20)
    server_response = models.TextField(blank=True, null=True)
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE)

    def __str__(self):
        return f"Попытка {self.id} от {self.attempt_time}"

    class Meta:
        verbose_name = "Попытка"
        verbose_name_plural = "Попытки"





