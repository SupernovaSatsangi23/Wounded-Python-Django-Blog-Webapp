# Generated by Django 3.0.3 on 2020-10-15 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healtharchive', '0005_auto_20201015_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='humandiseasearchive',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='humandiseasearchive',
            name='name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='humandiseasearchive',
            name='solution',
            field=models.TextField(blank=True, null=True),
        ),
    ]
