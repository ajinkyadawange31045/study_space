# Generated by Django 4.1.5 on 2023-01-27 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='content',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='branch',
            name='name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='college',
            name='desc',
            field=models.CharField(blank=True, max_length=330),
        ),
        migrations.AlterField(
            model_name='college',
            name='name',
            field=models.CharField(blank=True, max_length=60),
        ),
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='about',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='books_drive_link',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='content',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='resources',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='reviews',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='postforimage',
            name='content',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='postforimage',
            name='title',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='semester',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='semester',
            name='name',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]