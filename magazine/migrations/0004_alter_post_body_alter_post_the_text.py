# Generated by Django 4.0.4 on 2022-06-13 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0003_alter_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(default=' '),
        ),
        migrations.AlterField(
            model_name='post',
            name='the_text',
            field=models.CharField(max_length=150),
        ),
    ]