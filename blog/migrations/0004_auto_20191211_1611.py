# Generated by Django 3.0 on 2019-12-11 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20191211_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='github_login',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]