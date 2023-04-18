from django.db import models
from .admin import admin


class Image(models.Model):
    title = models.CharField("Наименование", max_length=60, null=True, blank=True)
    img = models.ImageField("Изображение", upload_to='img/', null=True, blank=True)
    alt = models.CharField("Альтернативный текст", max_length=60, null=True, blank=True)

    class Meta:
        verbose_name = "Изображения"
        verbose_name_plural = "Изображение"

    def __str__(self):
        return self.title


class ServicePrice(models.Model):
    title = models.CharField("Наименование", max_length=60, null=True, blank=True)
    price = models.FloatField("Стоимость", null=True, blank=True)

    class Meta:
        verbose_name = "Услуги"
        verbose_name_plural = "Услуга"

    def __str__(self):
        return self.title + " " + str(self.price)


class Service(models.Model):
    title = models.CharField("Наименование", null=True, blank=True,max_length=255)
    direct_description = models.CharField("Краткое описание", null=True, blank=True,max_length=255)
    description = models.TextField("Полное описание", null=True, blank=True,max_length=1000)
    price_list = models.ManyToManyField(ServicePrice,  blank=True, related_name='services')
    images = models.ManyToManyField(Image,  blank=True, related_name='images')

    class Meta:
        verbose_name = "Категории услуг"
        verbose_name_plural = "Категория услуги"

    def __str__(self):
        return self.title


class FeedBack(models.Model):
    title = models.CharField("Наименование", null=True, blank=True,max_length=60)
    surname = models.CharField("Фамилия", null=True, blank=True,max_length=60)
    name = models.CharField("Имя", null=True, blank=True,max_length=60)
    message = models.TextField("Сообщение", null=True, blank=True,max_length=1000)
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Отзывы"
        verbose_name_plural = "Отзыв"

    def __str__(self):
        return self.title


class Support(models.Model):
    name = models.CharField("Имя", null=True, blank=True,max_length=60)
    tel = models.CharField("Телефон", max_length=30, null=True, blank=True)
    message = models.CharField("Сообщение", max_length=500, null=True, blank=True)

    class Meta:
        verbose_name = "Заявки"
        verbose_name_plural = "Заявка"

    def __str__(self):
        return f"{self.name} >-> {self.tel}"


class Page(models.Model):
    main_title = models.CharField("Главный заголовок", max_length=255, null=True, blank=True)
    main_description = models.TextField("Главное описание", max_length=1000, null=True, blank=True)
    title = models.CharField("Дополнительный заголовок", max_length=255, null=True, blank=True)
    service_list = models.ManyToManyField(Service, blank=True, verbose_name="Услуги")
    description = models.TextField("Дополнительное описание", max_length=1000, null=True, blank=True)
    history_title = models.CharField("Заголовок истории", max_length=255, null=True, blank=True)
    history_description = models.TextField("Описание истории", max_length=1000, null=True, blank=True)
    url = models.CharField("Ссылка на страницу описания", max_length=500, null=True, blank=True)
    feedback = models.ManyToManyField(FeedBack, blank=True, verbose_name="Отзывы")

    class Meta:
        verbose_name = "Страницы"
        verbose_name_plural = "Страница"

    def __str__(self):
        return "Страница 1"


for_admin = [Page, Service, ServicePrice, Image, FeedBack, Support]
admin.site.register(for_admin)
