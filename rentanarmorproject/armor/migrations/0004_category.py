# Generated by Django 4.0 on 2021-12-22 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('armor', '0003_rename_title_review_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]