# Generated by Django 4.2.18 on 2025-01-20 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='referred_by',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
