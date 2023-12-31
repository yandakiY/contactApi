# Generated by Django 4.2.6 on 2023-10-23 00:07

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='Id')),
                ('Contact', models.CharField(max_length=200, verbose_name='Contacts')),
                ('telephone', models.TextField(verbose_name='Telephone')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
