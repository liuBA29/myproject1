from django.db import models


class Documents(models.Model):
    doc_type = models.CharField(max_length=25, db_index=True)
    slug = models.SlugField(max_length=25, db_index=True, unique=True, verbose_name='Documents')

    def __str__(self):
        return self.doc_type

    class Meta:
        verbose_name = "Документы"
        verbose_name_plural = "Документы"
#--------------------------------------------------------------- 2

class Transport(models.Model):
    name = models.CharField(max_length=25, db_index=True)
    slug = models.SlugField(max_length=25, db_index=True, unique=True, verbose_name='Транспорт')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Транспорт"
        verbose_name_plural = "Транспорт"

#===================================================== 3
class Costs(models.Model):
    ammount = models.FloatField(blank=True, null=True, verbose_name='Стоимость')
    currency_name = models.CharField(max_length=25, db_index=True, verbose_name='Валюта')
    slug = models.SlugField(max_length=25, db_index=True, unique=True)

    def __str__(self):
        return self.slug

    class Meta:
        verbose_name = "Валюта"
        verbose_name_plural = "Валюта"

#========================================================
class Country(models.Model):
    name = models.CharField(max_length=25, db_index=True)
    slug = models.SlugField(max_length=25, db_index=True, unique=True, verbose_name='Страна')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Страна"
        verbose_name_plural = "Страны"

  #=================================================== 4
class Catcontragents(models.Model):
    name = models.CharField(max_length=25, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True, unique=True, verbose_name='Категории контрагентов')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категории контрагентов"
        verbose_name_plural = "Категории контрагентов"




#------------------------------------------------------------4

class Catopportunity(models.Model):
    name = models.CharField(max_length=25, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True, unique=True, verbose_name='Категории сделок')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категории сделки"
        verbose_name_plural = "Категории сделок"
#---------------------------------------------------------------5

class Quotstatus(models.Model):
    name = models.CharField(max_length=25, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True, unique=True, verbose_name='Статус котировки')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Статус котировки"
        verbose_name_plural = "Статусы котировок"


##########################CHILDREN##############################  1


class Contragents(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    photo = models.ImageField(blank=True)
    address = models.TextField(blank=True, verbose_name='Адрес')
    contact = models.CharField(max_length=100, blank=True, verbose_name='Контактное лицо')
    email = models.EmailField(max_length=70, blank=True)
    info = models.CharField(max_length=100, verbose_name='Дополнительная информация')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время последнего обновления')
    cat = models.ForeignKey(Catcontragents, on_delete=models.PROTECT, verbose_name='Категория')
    slug = models.SlugField(max_length=100, db_index=True, unique=True, verbose_name='URL')
    opportunity = models.ManyToManyField('QuotationOpportunity', blank=True, verbose_name='Участник сделки', related_name="opportunity_member")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name= "Контрагенты"
        verbose_name_plural="Контрагенты"


#--------------------------------------------------------   4




#-----------------------------------------------
class Clientrequest(models.Model):
    contact = models.CharField(max_length=255, blank=True, verbose_name='Контактное лицо')
    client_name = models.CharField(max_length=255, blank=True, verbose_name='Название компании')
    description = models.CharField(max_length=255, blank=True)

    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")

   # country_loaded = models.ForeignKey(Country, on_delete=models.PROTECT)
    address = models.CharField(max_length=90, verbose_name='Адрес')
    country = models.ManyToManyField(Country, blank=True)


    weight = models.CharField(max_length=90, verbose_name='Вес товара')
    dimensions = models.CharField(max_length=90, verbose_name='Габариты товара')
    type = models.CharField(max_length=90, verbose_name='Тип груза')
    slug = models.SlugField(max_length=100, db_index=True, unique=True, verbose_name='URL')

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Заявка (запрос)"
        verbose_name_plural = "Заявки (запросы)"

#================================  5
class QuotationOpportunity(models.Model):
    RESULT_CHOICES = (
        ('NOT YET', 'Груз не готов'),
        ('NO', 'Не прошли по цене'),
        ('OK', 'Прошли по цене'),
    )

    client_request = models.ForeignKey(Clientrequest, on_delete=models.PROTECT)
    #quot = models.FloatField(blank=True, null=True)
    client_name = models.ForeignKey(Contragents, on_delete=models.PROTECT, verbose_name='Наименование заказчика')
   # supplyer_name = models.ForeignKey(Contragents, on_delete=models.PROTECT, verbose_name='Наименование перевозчика')
    transport = models.ForeignKey(Transport, on_delete=models.PROTECT)
  #  country_loading = models.ForeignKey(Country, on_delete=models.PROTECT)
    address_loading = models.CharField(max_length=90, verbose_name='Адрес загрузки')
    country_unloading = models.ForeignKey(Country, on_delete=models.PROTECT)
    address_unloading = models.CharField(max_length=90, verbose_name='Адрес выгрузки')
    description = models.TextField(blank=True)
    quot_field=models.CharField(max_length=90, verbose_name='Ставка')
    comment=models.TextField(blank=True, verbose_name='Комментарий')

    quotation_result = models.CharField(max_length=150, choices=RESULT_CHOICES, default="PROJECT")
    quotation_is_approved = models.BooleanField(default=False)
    slug = models.SlugField(max_length=100, db_index=True, unique=True, verbose_name='URL')


    #class Opportunity(models.Model):
    STATUS_CHOICES = [
        ('PROJECT', 'Проект'),
        ('CURRENT', (
            ('NEW', 'Новая'),
            ('TAKEN', 'Принята'),
            ('IN TRANSIT', 'В пути'),
            ('UNLOADED NO PROOF', 'Выгружена без подтверждения'),
        )
            ),
        ('CLOSED', (
             ('UNLOADED WITH PROOF', 'Выгружена с подтверждением'),
            ('DID NOT HAPPEN', 'Не состоялась'),
        )
         ),
    ]
    opportunity_number = models.IntegerField()
    photo = models.ImageField(blank=True, upload_to="photos/%Y/%m/%d/")
    file = models.FileField(blank=True, upload_to="file/%Y/%m/%d/")

    # supplyer = models.ForeignKey(Contragents, on_delete=models.PROTECT, verbose_name='Наименование перевозчика')

     # cient_currency = models.ForeignKey(Currency, on_delete=models.PROTECT, verbose_name='Валюта заказчика')
    cost = models.ForeignKey(Costs, on_delete=models.PROTECT, verbose_name='Валюта перевозчика')
    date_loading = models.DateTimeField(verbose_name='Дата загрузки')
    date_unloading = models.DateTimeField(verbose_name='Дата выгрузки')
    is_unloaded = models.BooleanField(default=False, verbose_name='Товар выгружен')

    status = models.CharField(max_length=150, choices=STATUS_CHOICES, default="PROJECT")
    cargo_info = models.TextField(blank=True, verbose_name='Дополнительная информация')

    def __str__(self):
        return self.quotation_result

    class Meta:
        verbose_name = "Котировка/Сделка"
        verbose_name_plural = "Котировки/Сделки"


