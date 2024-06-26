# Generated by Django 4.2.6 on 2024-06-15 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='authors',
            name='notes',
            field=models.TextField(default='empty'),
        ),
        migrations.AlterField(
            model_name='authors',
            name='books',
            field=models.ManyToManyField(related_name='books', to='books_authors_app.books'),
        ),
        migrations.AlterField(
            model_name='books',
            name='desc',
            field=models.TextField(default='empty'),
        ),
    ]
