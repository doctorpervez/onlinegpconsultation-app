# Generated by Django 3.2.6 on 2024-07-10 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('referrals', '0007_alter_referral_access_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referral',
            name='access_code',
            field=models.CharField(default='EpjYDu', max_length=6, unique=True),
        ),
    ]
