# Generated by Django 4.1.2 on 2022-11-01 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0007_alter_topic_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('people', models.CharField(max_length=10)),
                ('discount', models.CharField(max_length=10)),
                ('price', models.CharField(max_length=10)),
                ('lista', models.CharField(max_length=100)),
                ('listb', models.CharField(max_length=100)),
                ('listc', models.CharField(max_length=100)),
                ('listd', models.CharField(max_length=100)),
                ('liste', models.CharField(max_length=100)),
            ],
        ),
    ]
