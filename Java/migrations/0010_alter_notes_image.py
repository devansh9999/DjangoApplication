# Generated by Django 3.2.8 on 2021-11-01 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Java', '0009_alter_notes_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
    ]
