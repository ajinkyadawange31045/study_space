# Generated by Django 4.1.5 on 2023-01-27 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_alter_branch_content_alter_branch_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postforimage',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]