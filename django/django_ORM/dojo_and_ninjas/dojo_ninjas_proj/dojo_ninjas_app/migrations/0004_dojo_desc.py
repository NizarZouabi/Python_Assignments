# Generated by Django 4.2.6 on 2024-06-11 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas_app', '0003_ninja_delete_ninjas'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojo',
            name='desc',
            field=models.TextField(default='Hello Ninja'),
        ),
    ]
