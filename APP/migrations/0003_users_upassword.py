# Generated by Django 2.2 on 2019-05-03 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0002_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='upassword',
            field=models.CharField(default='password', max_length=100),
            preserve_default=False,
        ),
    ]