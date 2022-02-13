# Generated by Django 4.0.2 on 2022-02-13 22:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0002_alter_movie_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='director_list_view', to='movie_app.director'),
        ),
        migrations.AlterField(
            model_name='review',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='director_detail_view', to='movie_app.movie'),
        ),
    ]
