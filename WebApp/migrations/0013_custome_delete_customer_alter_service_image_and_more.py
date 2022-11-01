# Generated by Django 4.1.2 on 2022-11-01 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0012_service_delete_servic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Custome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=100)),
                ('Last_name', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=100)),
                ('DOBdate', models.DateField()),
                ('Email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
                ('Contact', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'Custome',
            },
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ImageField(blank=True, upload_to='Dataimage'),
        ),
        migrations.AlterField(
            model_name='service',
            name='listd',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='service',
            name='liste',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]