# Generated by Django 3.0.3 on 2020-03-10 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formulas', '0006_auto_20200305_1629'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formula',
            name='form',
        ),
        migrations.AddField(
            model_name='formula',
            name='express1',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formula',
            name='express2',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formula',
            name='express3',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formula',
            name='express4',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formula',
            name='param1',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formula',
            name='param2',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formula',
            name='param3',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formula',
            name='param4',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
