# Generated by Django 4.1.5 on 2023-01-13 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messageboard', '0002_message_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='postmessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, unique=True)),
                ('content', models.TextField()),
            ],
            options={
                'db_table': 'postmessage',
            },
        ),
    ]