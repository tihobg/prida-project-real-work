# Generated by Django 4.2.16 on 2025-01-25 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pridastartapp', '0010_alter_pridamutations_age_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pridamutations',
            name='age',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pridamutations',
            name='birth_year',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
