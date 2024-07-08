# Generated by Django 3.2.6 on 2024-06-12 15:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('consultations', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Referral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referred_to_clinician', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=200)),
                ('reason', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('access_code', models.CharField(default='Jb7rVD', max_length=6, unique=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consultations.patient')),
                ('referring_clinician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='referrals_made', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]