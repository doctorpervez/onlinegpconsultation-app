# Generated by Django 3.2.6 on 2024-07-10 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('referrals', '0006_alter_referral_access_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referral',
            name='access_code',
            field=models.CharField(default='IVzMNG', max_length=6, unique=True),
        ),
    ]
