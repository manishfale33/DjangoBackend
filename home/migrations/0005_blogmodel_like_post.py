# Generated by Django 4.2.1 on 2023-06-02 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogmodel',
            name='like_post',
            field=models.IntegerField(default=0),
        ),
    ]
