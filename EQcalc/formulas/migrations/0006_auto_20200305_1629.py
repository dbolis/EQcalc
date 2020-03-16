# Generated by Django 3.0.3 on 2020-03-05 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formulas', '0005_formula2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Formula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('form', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Formula1',
        ),
        migrations.DeleteModel(
            name='Formula2',
        ),
    ]