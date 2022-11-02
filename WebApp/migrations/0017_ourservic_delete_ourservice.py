# Generated by Django 4.1.2 on 2022-11-02 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0016_rename_service_ourservice'),
    ]

    operations = [
        migrations.CreateModel(
            name='ourservic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='Dataimage')),
                ('title', models.CharField(max_length=100)),
                ('people', models.CharField(max_length=10)),
                ('discount', models.CharField(max_length=10)),
                ('price', models.CharField(max_length=10)),
                ('lista', models.CharField(max_length=100)),
                ('listb', models.CharField(max_length=100)),
                ('listc', models.CharField(max_length=100)),
                ('listd', models.CharField(blank=True, max_length=100)),
                ('liste', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='ourservice',
        ),
    ]
