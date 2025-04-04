# Generated by Django 4.2.16 on 2025-01-23 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pridastartapp', '0002_pridamutations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pridamutations',
            name='fvl_hetero',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='pridamutations',
            name='fvl_homo',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='pridamutations',
            name='fvl_ng',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='pridamutations',
            name='mthfr_hetero',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='pridamutations',
            name='mthfr_homo',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='pridamutations',
            name='mthfr_ng',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='pridamutations',
            name='pai_hetero',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='pridamutations',
            name='pai_homo',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='pridamutations',
            name='pai_ng',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='pridamutations',
            name='prothr_hetero',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='pridamutations',
            name='prothr_homo',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='pridamutations',
            name='prothr_ng',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
    ]
