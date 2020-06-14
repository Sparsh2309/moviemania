# Generated by Django 3.0.7 on 2020-06-14 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a movie genre', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Thumbnail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumb_1', models.ImageField(height_field='220px', upload_to='media/thumbnail', width_field='180px')),
                ('thumb_2', models.ImageField(height_field='220px', upload_to='media/thumbnail', width_field='180px')),
                ('thumb_3', models.ImageField(height_field='220px', upload_to='media/thumbnail', width_field='180px')),
                ('thumb_4', models.ImageField(height_field='220px', upload_to='media/thumbnail', width_field='180px')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=100)),
                ('movie_poster', models.ImageField(height_field='220px', upload_to='media/movie', width_field='180px')),
                ('cast', models.CharField(max_length=200)),
                ('date_added', models.DateField(auto_now=True)),
                ('imbd_rating', models.CharField(max_length=20)),
                ('resolution', models.CharField(choices=[('1080p', '1080p'), ('720p', '720p'), ('480p', '480p')], max_length=50)),
                ('Link_download', models.CharField(max_length=500)),
                ('genre', models.ManyToManyField(help_text='Select a genre for this movie', to='movie.Genre')),
                ('thumbnail', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='movie.Thumbnail')),
            ],
        ),
    ]