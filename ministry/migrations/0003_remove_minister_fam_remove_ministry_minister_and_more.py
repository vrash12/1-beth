# Generated by Django 5.0.2 on 2024-03-30 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ministry', '0002_availability_schedule'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='minister',
            name='fam',
        ),
        migrations.RemoveField(
            model_name='ministry',
            name='minister',
        ),
        migrations.AddField(
            model_name='minister',
            name='is_youth_minister',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='ministry',
            name='ministers',
            field=models.ManyToManyField(related_name='ministries', to='ministry.minister'),
        ),
    ]
