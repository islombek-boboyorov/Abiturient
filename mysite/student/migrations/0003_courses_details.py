# Generated by Django 3.2.4 on 2021-06-08 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20210608_1643'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('price', models.IntegerField(default=0)),
                ('pupils_count', models.IntegerField(default=0)),
                ('time', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='image/')),
                ('description', models.TextField()),
                ('subject', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'courses_info',
            },
        ),
    ]
