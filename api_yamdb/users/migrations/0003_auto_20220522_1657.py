# Generated by Django 2.2.16 on 2022-05-22 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_confirmation_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='confirmation_code',
            field=models.CharField(max_length=100, null=True, verbose_name='Код подтверждения'),
        ),
    ]