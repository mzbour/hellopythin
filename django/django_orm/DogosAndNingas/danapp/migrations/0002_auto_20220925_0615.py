# Generated by Django 2.2.4 on 2022-09-25 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('danapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ninja',
            name='ninja',
        ),
        migrations.AddField(
            model_name='ninja',
            name='dojo',
            field=models.ForeignKey(default='aaa', on_delete=django.db.models.deletion.CASCADE, related_name='dojo', to='danapp.Dojo'),
            preserve_default=False,
        ),
    ]
