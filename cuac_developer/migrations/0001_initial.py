# Generated by Django 4.2.7 on 2024-05-24 11:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cuac_core', '0023_company_activation_date_company_archived_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.IntegerField(default=0)),
                ('hours_elapsed', models.IntegerField(default=0)),
                ('created', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('expiration', models.DateTimeField(blank=True, null=True)),
                ('active', models.BooleanField()),
                ('invoiced', models.BooleanField()),
                ('charged', models.BooleanField()),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cuac_core.company')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('time', models.IntegerField(default=0)),
                ('assignee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('batch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cuac_developer.batch')),
            ],
        ),
    ]
