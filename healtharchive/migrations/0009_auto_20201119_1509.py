# Generated by Django 3.0.3 on 2020-11-19 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healtharchive', '0008_homepageviews'),
    ]

    operations = [
        migrations.AddField(
            model_name='animaldiseasearchive',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='animal_disease_archive/'),
        ),
        migrations.AddField(
            model_name='animalinjuryarchive',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='animal_injury_archive/'),
        ),
        migrations.AddField(
            model_name='humandiseasearchive',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='human_disease_archive/'),
        ),
        migrations.AddField(
            model_name='humaninjuryarchive',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='human_injury_archive/'),
        ),
        migrations.AddField(
            model_name='humanpsychologyarchive',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='human_psychology_archive/'),
        ),
    ]