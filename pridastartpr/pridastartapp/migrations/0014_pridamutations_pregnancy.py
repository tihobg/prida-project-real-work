# Generated by Django 4.2.16 on 2025-02-01 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pridastartapp', '0013_alter_pridamutations_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='pridamutations',
            name='pregnancy',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
    ]
