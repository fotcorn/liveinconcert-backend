# Generated by Django 2.0.6 on 2018-06-25 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('liveinconcert', '0007_auto_20161004_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventrsvp',
            name='rsvp',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No'), ('not_yet_answered', 'No yet answered')], max_length=20),
        ),
    ]
