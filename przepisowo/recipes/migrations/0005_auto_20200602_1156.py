# Generated by Django 3.0.6 on 2020-06-02 11:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("recipes", "0004_auto_20200602_0942"),
    ]

    operations = [
        migrations.AddField(
            model_name="recipe",
            name="preparation_time_in_minutes",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="ingredient",
            name="name",
            field=models.CharField(default="", max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="ingredient",
            name="unit",
            field=models.CharField(blank=True, default="", max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="recipe",
            name="author",
            field=models.ForeignKey(
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="recipes",
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="recipe",
            name="description",
            field=models.TextField(default=""),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="recipe",
            name="image",
            field=models.ImageField(blank=True, default="", upload_to=""),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="recipe",
            name="publish",
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name="recipe",
            name="subname",
            field=models.CharField(blank=True, default="", max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="recipe",
            name="title",
            field=models.CharField(default="", max_length=200),
            preserve_default=False,
        ),
    ]
