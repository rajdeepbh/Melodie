# Generated by Django 2.1.5 on 2019-01-22 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommend', '0003_auto_20190122_1540'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listen',
            old_name='song',
            new_name='container',
        ),
        migrations.RemoveField(
            model_name='appuser',
            name='listens',
        ),
        migrations.AddField(
            model_name='appuser',
            name='listens',
            field=models.ManyToManyField(to='recommend.Listen'),
        ),
    ]