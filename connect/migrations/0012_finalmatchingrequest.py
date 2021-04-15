# Generated by Django 3.1.7 on 2021-04-15 16:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('connect', '0011_initialmatchingrequest'),
    ]

    operations = [
        migrations.CreateModel(
            name='FinalMatchingRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('final_req_users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='finalmatch', to='connect.request')),
            ],
            options={
                'ordering': ['-updated'],
            },
        ),
    ]