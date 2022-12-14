# Generated by Django 2.2.4 on 2022-10-03 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('desc', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('liked_users', models.ManyToManyField(related_name='liked_books', to='login.User')),
                ('uploader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uploaded_books', to='login.User')),
            ],
        ),
    ]
