# Generated by Django 5.1.3 on 2024-11-28 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media')),
                ('name', models.CharField(max_length=250)),
                ('role', models.CharField(max_length=250)),
                ('order_id', models.PositiveIntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Team Member',
                'verbose_name_plural': 'Team Members',
                'db_table': 'fasion_team_member',
                'ordering': ('-id',),
            },
        ),
    ]
