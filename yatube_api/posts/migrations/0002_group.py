# Generated by Django 2.2.16 on 2022-03-23 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('slug', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groups', to='posts.Post')),
            ],
        ),
    ]
