# Generated by Django 2.0.1 on 2018-05-15 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
