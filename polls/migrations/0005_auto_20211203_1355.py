# Generated by Django 3.2.9 on 2021-12-03 04:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20211203_1318'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='polls.comment'),
        ),
        migrations.DeleteModel(
            name='Reply',
        ),
    ]