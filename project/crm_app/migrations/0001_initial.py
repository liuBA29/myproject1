# Generated by Django 4.2.6 on 2023-10-12 16:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catcontragents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=25)),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='Категории контрагентов')),
            ],
            options={
                'verbose_name': 'Категории контрагентов',
                'verbose_name_plural': 'Категории контрагентов',
            },
        ),
        migrations.CreateModel(
            name='Catopportunity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=25)),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='Категории сделок')),
            ],
            options={
                'verbose_name': 'Категории сделки',
                'verbose_name_plural': 'Категории сделок',
            },
        ),
        migrations.CreateModel(
            name='Clientrequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(blank=True, max_length=255, verbose_name='Контактное лицо')),
                ('description', models.CharField(blank=True, max_length=255)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('address', models.CharField(max_length=90, verbose_name='Адрес')),
                ('weight', models.CharField(max_length=90, verbose_name='Вес товара')),
                ('dimensions', models.CharField(max_length=90, verbose_name='Габариты товара')),
                ('type', models.CharField(max_length=90, verbose_name='Тип груза')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Заявка (запрос)',
                'verbose_name_plural': 'Заявки (запросы)',
            },
        ),
        migrations.CreateModel(
            name='Contragents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('photo', models.ImageField(blank=True, upload_to='')),
                ('address', models.TextField(blank=True, verbose_name='Адрес')),
                ('contact', models.CharField(blank=True, max_length=100, verbose_name='Контактное лицо')),
                ('email', models.EmailField(blank=True, max_length=70)),
                ('info', models.CharField(max_length=100, verbose_name='Дополнительная информация')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Время последнего обновления')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='URL')),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='crm_app.catcontragents', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Контрагенты',
                'verbose_name_plural': 'Контрагенты',
            },
        ),
        migrations.CreateModel(
            name='Costs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ammount', models.FloatField(blank=True, null=True, verbose_name='Стоимость')),
                ('currency_name', models.CharField(db_index=True, max_length=25, verbose_name='Валюта')),
                ('slug', models.SlugField(max_length=25, unique=True)),
            ],
            options={
                'verbose_name': 'Валюта',
                'verbose_name_plural': 'Валюта',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=25)),
                ('slug', models.SlugField(max_length=25, unique=True, verbose_name='Страна')),
            ],
            options={
                'verbose_name': 'Страна',
                'verbose_name_plural': 'Страны',
            },
        ),
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_type', models.CharField(db_index=True, max_length=25)),
                ('slug', models.SlugField(max_length=25, unique=True, verbose_name='Documents')),
            ],
            options={
                'verbose_name': 'Документы',
                'verbose_name_plural': 'Документы',
            },
        ),
        migrations.CreateModel(
            name='Quotstatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=25)),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='Статус котировки')),
            ],
            options={
                'verbose_name': 'Статус котировки',
                'verbose_name_plural': 'Статусы котировок',
            },
        ),
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=25)),
                ('slug', models.SlugField(max_length=25, unique=True, verbose_name='Транспорт')),
            ],
            options={
                'verbose_name': 'Транспорт',
                'verbose_name_plural': 'Транспорт',
            },
        ),
        migrations.CreateModel(
            name='QuotationOpportunity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_loading', models.CharField(max_length=90, verbose_name='Адрес загрузки')),
                ('address_unloading', models.CharField(max_length=90, verbose_name='Адрес выгрузки')),
                ('description', models.TextField(blank=True)),
                ('quot_field', models.CharField(max_length=90, verbose_name='Ставка')),
                ('comment', models.TextField(blank=True, verbose_name='Комментарий')),
                ('quotation_result', models.CharField(choices=[('NOT YET', 'Груз не готов'), ('NO', 'Не прошли по цене'), ('OK', 'Прошли по цене')], default='PROJECT', max_length=150)),
                ('quotation_is_approved', models.BooleanField(default=False)),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='URL')),
                ('opportunity_number', models.IntegerField()),
                ('photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('file', models.FileField(blank=True, upload_to='file/%Y/%m/%d/')),
                ('date_loading', models.DateTimeField(verbose_name='Дата загрузки')),
                ('date_unloading', models.DateTimeField(verbose_name='Дата выгрузки')),
                ('is_unloaded', models.BooleanField(default=False, verbose_name='Товар выгружен')),
                ('status', models.CharField(choices=[('PROJECT', 'Проект'), ('CURRENT', (('NEW', 'Новая'), ('TAKEN', 'Принята'), ('IN TRANSIT', 'В пути'), ('UNLOADED NO PROOF', 'Выгружена без подтверждения'))), ('CLOSED', (('UNLOADED WITH PROOF', 'Выгружена с подтверждением'), ('DID NOT HAPPEN', 'Не состоялась')))], default='PROJECT', max_length=150)),
                ('cargo_info', models.TextField(blank=True, verbose_name='Дополнительная информация')),
                ('client_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='crm_app.contragents', verbose_name='Наименование заказчика')),
                ('client_request', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='crm_app.clientrequest')),
                ('cost', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='crm_app.costs', verbose_name='Валюта перевозчика')),
                ('country_unloading', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='crm_app.country')),
                ('transport', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='crm_app.transport')),
            ],
            options={
                'verbose_name': 'Котировка/Сделка',
                'verbose_name_plural': 'Котировки/Сделки',
            },
        ),
        migrations.AddField(
            model_name='contragents',
            name='opportunity',
            field=models.ManyToManyField(blank=True, related_name='opportunity_member', to='crm_app.quotationopportunity', verbose_name='Участник сделки'),
        ),
        migrations.AddField(
            model_name='clientrequest',
            name='client_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='crm_app.contragents', verbose_name='Название компании'),
        ),
        migrations.AddField(
            model_name='clientrequest',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='crm_app.country'),
        ),
        migrations.AddField(
            model_name='clientrequest',
            name='opportunity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='crm_app.quotationopportunity'),
        ),
    ]
