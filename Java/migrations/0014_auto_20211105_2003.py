# Generated by Django 3.2.8 on 2021-11-05 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Java', '0013_rename_notes_doubts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adddata',
            name='Question',
            field=models.TextField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='adddata',
            name='Solution',
            field=models.TextField(max_length=10000),
        ),
    ]
