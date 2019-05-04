# Generated by Django 2.2 on 2019-05-02 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('mid', models.AutoField(primary_key=True, serialize=False)),
                ('mname', models.CharField(max_length=100)),
                ('mactor', models.CharField(max_length=255)),
                ('mactress', models.CharField(max_length=255)),
                ('mdirector', models.CharField(max_length=255)),
                ('msummary', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'movies',
            },
        ),
    ]