# Generated by Django 3.1 on 2020-08-28 02:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('summary', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('stack', models.CharField(max_length=500)),
                ('githubURL', models.URLField()),
                ('liveURL', models.URLField()),
            ],
        ),
        migrations.RenameField(
            model_name='job',
            old_name='summary',
            new_name='project',
        ),
        migrations.AddField(
            model_name='job',
            name='company',
            field=models.CharField(default=True, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='contributions',
            field=models.TextField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='description',
            field=models.TextField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='endDate',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='role',
            field=models.CharField(default='Intern', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='stack',
            field=models.CharField(default='python', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='startDate',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
