# Generated by Django 5.1.3 on 2024-11-28 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Spotlight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media')),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('order_id', models.PositiveIntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Spotlight',
                'verbose_name_plural': 'Spotlights',
                'db_table': 'fasion_spotlight',
                'ordering': ('-id',),
            },
        ),
    ]
