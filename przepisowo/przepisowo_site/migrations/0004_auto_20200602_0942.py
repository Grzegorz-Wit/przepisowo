# Generated by Django 3.0.6 on 2020-06-02 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('przepisowo_site', '0003_auto_20200602_0929'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='name',
            new_name='title',
        ),
    ]
