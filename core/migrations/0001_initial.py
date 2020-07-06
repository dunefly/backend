# Generated by Django 3.0.8 on 2020-07-06 02:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contributor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=15, unique=True)),
                ('email', models.EmailField(max_length=300)),
                ('bio', models.CharField(max_length=1000)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Severity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Severity_choices', models.IntegerField(choices=[(0, 'Low'), (1, 'Medium'), (2, 'High')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_choices', models.IntegerField(choices=[(0, 'Not Started'), (1, 'In Progress'), (2, 'Completed')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=2048)),
                ('author', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Contributor')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=2048)),
                ('author', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Contributor')),
                ('issue', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.Issue')),
            ],
        ),
    ]
