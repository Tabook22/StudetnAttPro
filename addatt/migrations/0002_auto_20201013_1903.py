# Generated by Django 3.1.2 on 2020-10-13 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('addatt', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='email_name',
            new_name='email',
        ),
    ]
