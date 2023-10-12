# Generated by Django 4.2.6 on 2023-10-12 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientrequest',
            name='opportunity',
        ),
        migrations.AlterField(
            model_name='clientrequest',
            name='client_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='Название компании'),
        ),
        migrations.RemoveField(
            model_name='clientrequest',
            name='country',
        ),
        migrations.AddField(
            model_name='clientrequest',
            name='country',
            field=models.ManyToManyField(blank=True, to='crm_app.country'),
        ),
    ]
