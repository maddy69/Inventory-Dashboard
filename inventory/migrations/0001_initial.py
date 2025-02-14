# Generated by Django 4.2.8 on 2024-06-14 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('description', models.TextField()),
                ('title', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('product_type', models.CharField(max_length=50)),
                ('custom_label_0', models.CharField(max_length=50)),
                ('condition', models.CharField(max_length=50)),
            ],
        ),
    ]
