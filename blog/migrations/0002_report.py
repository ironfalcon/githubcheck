# Generated by Django 3.0 on 2019-12-11 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ldap_login', models.CharField(max_length=50, unique=True)),
                ('github_login', models.CharField(max_length=100, unique=True)),
                ('checked', models.CharField(default='NONE', max_length=6)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
