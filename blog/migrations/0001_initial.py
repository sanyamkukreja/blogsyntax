# Generated by Django 4.1.3 on 2022-12-06 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=13)),
                ('content', models.TextField()),
                ('timeStamp', models.DateTimeField(blank=True)),
            ],
        ),
    ]
