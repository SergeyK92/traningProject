# Generated by Django 4.2.2 on 2023-06-28 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('educational', '0002_question_votes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='votes',
        ),
    ]
