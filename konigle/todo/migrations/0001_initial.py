# Generated by Django 2.0.2 on 2018-06-09 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('todo_id', models.AutoField(primary_key=True, serialize=False)),
                ('todo_heading', models.CharField(max_length=250)),
                ('todo_body', models.TextField()),
            ],
        ),
    ]
