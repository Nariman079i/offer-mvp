from django.db import models


class SMSManager(models.Model):
    title = models.CharField(max_length=60,verbose_name="Заголовок")
    recipient = models.EmailField(max_length=100,verbose_name="Отправитель")
    description = models.CharField(max_length=500, verbose_name="Сообщение")

    def __str__(self):
        return f"{self.recipient} -> {self.title}"

